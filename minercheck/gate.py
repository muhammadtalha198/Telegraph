"""Register gate: is this miner's answer the RIGHT answer to its catalog intent, right now?

The Intent Catalog decides what "right" means (intents/_catalog.json, tiers in
intents/_catalog_policy.yaml):

  unverifiable  catalog Verifiable=No                  -> BLOCKED (catalog reason quoted)
  judgment      catalog Class NON-DETERMINISTIC          -> SKIP (no deterministic truth; LLM judge)
  required      everything else                          -> needs intents/<INTENT>.yaml bound to the
                catalog row; no spec = FAIL "no spec for catalog intent X"

For a required intent with a spec:
  1. the miner must be mapped to a spec source (sources[].miner.slug)
  2. that source's kind must be allowed by the catalog Description (catalog.allowed_kinds),
     e.g. a CEX order book is not "liquidity across decentralized pools"
  3. call the miner exactly as the node does (YAML) or as captured (sample URL, no YAML)
  4. E1/E5/E2/E4/E5 on its answer, then E3 against independent sources (or the official
     record holder when the spec marks one as authority)
  5. every catalog facet marked required must be present in the miner's answer
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, urlencode

import yaml

from .catalog import Catalog, CatalogEntry
from .errors import MinerCheckError
from .fetch import Fetcher, Request
from .normalize import Geocoder, normalize
from .spec import IntentSpec, Registry
from .validate import Candidate, validate
from .verify import verify


@dataclass
class GateResult:
    verdict: str                       # PASS | FAIL | BLOCKED | SKIP
    lines: list[str] = field(default_factory=list)
    reason: str = ""
    catalog_intent: str = ""
    coverage: list[dict] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.verdict in ("PASS", "SKIP")


def node_request(doc: dict) -> tuple[str, str]:
    """(method, url) as the node builds it from a miner YAML's first endpoint + input_schema defaults."""
    ep = (doc.get("endpoints") or [{}])[0] or {}
    base = str(ep.get("endpoint_base_url") or doc.get("base_url") or "")
    if not base.startswith("http"):
        raise MinerCheckError("YAML base_url missing/invalid")
    path = str(ep.get("external_path") or ep.get("path") or "")
    method = str(ep.get("method") or "GET").upper()
    props = ((doc.get("input_schema") or {}).get("properties")) or {}
    params = {k: v["default"] for k, v in props.items() if isinstance(v, dict) and v.get("default") not in (None, "")}
    for k in list(params):
        ph = "{" + k + "}"
        if ph in path:
            path = path.replace(ph, quote(str(params.pop(k)), safe=""))
    url = base.rstrip("/") + (("/" + path.lstrip("/")) if path and path != "/" else "/")
    if params:
        url += ("&" if "?" in url else "?") + urlencode(params)
    return method, url


def spec_for(entry: CatalogEntry, reg: Registry) -> IntentSpec | None:
    return next((s for s in reg.specs.values() if (s.catalog or {}).get("intent") == entry.intent), None)


def facet_status(spec: IntentSpec, cand: Candidate) -> list[dict]:
    """Which catalog Description facets this answer actually carries."""
    out = []
    for f in (spec.catalog or {}).get("facets") or []:
        cov = str(f.get("covered_by", "none"))
        if cov == "value":
            present = cand.status == "valid"
        elif cov.startswith("extra:"):
            present = cov[6:] in cand.extras
        elif cov.startswith("entity:"):
            present = cov[7:] in cand.entity_seen
        elif cov.startswith("input:"):
            present = True               # the question itself carries it
        else:
            present = False
        out.append({"facet": f["text"], "covered_by": cov, "required": bool(f.get("required")),
                    "present": present, "note": f.get("note", "")})
    return out


def gate_miner(yaml_path: Path | None, intent: str, reg: Registry, *, fetcher: Fetcher,
               geocoder: Geocoder | None = None, slug: str | None = None, url: str | None = None,
               catalog: Catalog | None = None) -> GateResult:
    cat = catalog or Catalog(reg.directory)
    entry = cat.entry(intent)
    if entry is None:
        return GateResult("FAIL", [f"FAIL  {intent} is not an Intent Catalog intent (or alias in _catalog_policy.yaml)"],
                          reason="not a catalog intent")
    head = [f"catalog {entry.intent} [{entry.cls}, {entry.scoring_path}] tier={entry.tier}",
            f"        Description: {entry.description}"]
    if entry.tier == "unverifiable":
        why = f"catalog marks {entry.intent} Verifiable=No: {entry.verifiability_reason}"
        return GateResult("BLOCKED", head + [f"BLOCKED  {why}"], why, entry.intent)
    if entry.tier == "judgment":
        why = (f"catalog Class {entry.cls} ({entry.scoring_path}): no deterministic answer; "
               "the LLM judge decides against the catalog Description")
        return GateResult("SKIP", head + [f"SKIP  {why}"], why, entry.intent)
    spec = spec_for(entry, reg)
    if spec is None:
        why = f"no spec for catalog intent {entry.intent} (tier required: {entry.tier_reason})"
        return GateResult("FAIL", head + [f"FAIL  {why}. Add intents/<INTENT>.yaml bound to it (docs/INTENT_SPEC_GUIDE.md)."],
                          why, entry.intent)

    doc: dict = {}
    if yaml_path is not None:
        try:
            doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError) as e:
            raise MinerCheckError(f"cannot read {yaml_path}: {e}") from None
    slug = slug or str(doc.get("slug") or "")
    src = spec.by_miner(slug)
    if src is None:
        why = f"{spec.path.name if spec.path else spec.intent} has no source with miner.slug: {slug}"
        return GateResult("FAIL", head + [f"FAIL  {why}. Map it (url, value rules, kind, miner.question) first."],
                          why, entry.intent)
    allowed = (spec.catalog or {}).get("allowed_kinds") or []
    if allowed and src.kind not in allowed:
        why = (f"{slug} is a {src.kind} source; the catalog Description ({entry.description!r}) and Data Source Type "
               f"({entry.data_source_type!r}) need one of: {', '.join(allowed)}")
        return GateResult("FAIL", head + [f"FAIL  wrong kind of source: {why}"], why, entry.intent)

    if doc:
        method, call = node_request(doc)
    elif url:
        method, call = "GET", url
    else:
        raise MinerCheckError("need a miner YAML or a sample URL")
    lines = head + [f"spec    {spec.intent} source={src.id} kind={src.kind} publisher={src.publisher}"
                    + (" (authority)" if src.authority else ""),
                    f"call    {method} {call[:160]}"]
    if method != "GET":
        why = f"YAML declares {method}; only GET miners can be called as the node calls them"
        return GateResult("FAIL", lines + [f"FAIL  {why}"], why, entry.intent)

    norm = normalize(spec, dict(src.miner_question), reg.shared, geocoder)
    cand = Candidate(source=src)
    cand.fetch = fetcher.fetch(Request(call, timeout_s=src.timeout_s, headers=dict(src.headers)), cache_ttl_s=0)
    validate(spec, cand, norm)
    res = verify(spec, dict(src.miner_question), fetcher=fetcher, shared=reg.shared, geocoder=geocoder,
                 extra_candidates=[cand])
    for c in res.candidates:
        mark = "->" if c is cand else "  "
        val = "-" if c.parsed is None else str(c.parsed.display)[:28]
        lines.append(f"{mark} {c.source.id:16} {c.doc_format or '-':5} {val:>28}  {c.consensus or c.status}"
                     + (f"  [{c.layer}] {c.reason}" if c.status != "valid" else ""))
    cov = facet_status(spec, cand)
    covered = [f["facet"] for f in cov if f["present"]]
    lines.append(f"facets  {len(covered)}/{len(cov)} of the Description in this answer: "
                 + "; ".join(f"{'+' if f['present'] else '-'} {f['facet']}" for f in cov))
    if cand.status != "valid":
        why = f"[{cand.layer}] {cand.reason}"
        return GateResult("FAIL", lines + [f"FAIL  miner answer is not right: {why}"], why, entry.intent, cov)
    missing = [f["facet"] for f in cov if f["required"] and not f["present"]]
    if missing:
        why = f"catalog Description requires {', '.join(repr(m) for m in missing)}; {slug} does not return it"
        return GateResult("FAIL", lines + [f"FAIL  {why}"], why, entry.intent, cov)
    if res.verified and cand in res.agreeing:
        basis = "official record holder" if res.basis == "authority" else "independent sources"
        return GateResult("PASS", lines + [f"PASS  verified by {basis}: {res.answer_text}"], "", entry.intent, cov)
    if res.verified:
        why = f"answer {cand.parsed.display} disagrees with the verified answer {res.value}"
        return GateResult("FAIL", lines + [f"FAIL  {why}"], why, entry.intent, cov)
    why = f"could not verify: {res.reason}"
    return GateResult("BLOCKED", lines + [f"BLOCKED  answer is well-formed but {why}"], why, entry.intent, cov)
