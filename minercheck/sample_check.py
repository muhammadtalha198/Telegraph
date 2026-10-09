"""Deterministic check of a captured sample (apiOutputSamples/*.md), used by auto_review before
the LLM judge. The Intent Catalog decides what "right" means; the same validators as the live
gate run on the captured body, with the clock set to the sample's captured_at.

Returns ('valid' | 'rejected', reason), or None when a deterministic verdict is not possible
(judgment intent, no spec yet, miner not mapped, sample asked a different question). None
means the LLM judge decides, and it is given the catalog Description, not the sample's.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlparse

import yaml

from .catalog import Catalog
from .fetch import FetchResult
from .gate import facet_status, node_request, spec_for
from .normalize import normalize
from .spec import ROOT, Registry
from .validate import Candidate, validate


def _same(a: str, b: str) -> bool:
    x, y = urlparse(a.strip()), urlparse(b.strip())
    p = lambda u: unquote(u.path).rstrip("/") or "/"  # noqa: E731
    return (x.hostname, p(x), sorted(parse_qsl(x.query))) == (y.hostname, p(y), sorted(parse_qsl(y.query)))


def _yaml_for(slug: str) -> Path | None:
    hits = sorted((ROOT / "intentYamls").rglob(f"{slug}.yaml"))
    return hits[0] if hits else None


def check_sample(meta: dict, raw: str, *, slug: str, intent: str, reg: Registry | None = None,
                 cat: Catalog | None = None) -> tuple[str, str] | None:
    reg = reg or Registry()
    cat = cat or Catalog(reg.directory)
    entry = cat.entry(intent)
    if entry is None:
        return None
    if entry.tier == "unverifiable":
        return "rejected", f"catalog: {entry.intent} is Verifiable=No ({entry.verifiability_reason})"
    if entry.tier != "required":
        return None
    spec = spec_for(entry, reg)
    src = spec.by_miner(slug) if spec else None
    if src is None:
        return None
    allowed = (spec.catalog or {}).get("allowed_kinds") or []
    if allowed and src.kind not in allowed:
        return "rejected", (f"catalog: {entry.intent} is {entry.description!r}; {slug} is a {src.kind} source "
                            f"(needs {', '.join(allowed)})")
    url = str(meta.get("request_url", ""))
    ypath = _yaml_for(slug)
    if ypath is not None:
        try:
            _m, node_url = node_request(yaml.safe_load(ypath.read_text(encoding="utf-8")) or {})
        except Exception:  # noqa: BLE001 - a broken YAML is validate_miner_yaml's job
            return None
        if not _same(url, node_url):
            return None          # the sample is not this miner's question; the register gate catches that
    try:
        when = datetime.fromisoformat(str(meta.get("captured_at", "")).replace("Z", "+00:00"))
    except ValueError:
        when = datetime.now(timezone.utc)
    norm = normalize(spec, dict(src.miner_question), reg.shared)
    cand = Candidate(source=src)
    cand.fetch = FetchResult("ok", url, 200, {"content-type": str(meta.get("content_type", ""))},
                             raw.encode("utf-8"), fetched_at=when)
    validate(spec, cand, norm)
    if cand.status != "valid":
        return "rejected", f"minercheck [{cand.layer}] {cand.reason}"
    missing = [f["facet"] for f in facet_status(spec, cand) if f["required"] and not f["present"]]
    if missing:
        return "rejected", f"catalog {entry.intent}: Description requires {', '.join(repr(m) for m in missing)}; not in this answer"
    return "valid", f"minercheck {spec.intent}: {cand.parsed.detail}"


def catalog_context(intent: str) -> dict | None:
    """What the LLM judge must be told the intent means (the catalog row, not the sample's notes)."""
    try:
        e = Catalog().entry(intent)
    except Exception:  # noqa: BLE001 - index missing: the judge falls back to the sample text
        return None
    if e is None:
        return None
    return {"intent": e.intent, "description": e.description, "class": e.cls, "why": e.why,
            "evaluation": e.evaluation, "data_source_type": e.data_source_type}
