"""Intent Catalog (xlsx) -> machine-readable index, verification tiers, and spec audit.

The catalog is the authority for what a correct answer means. Every intent spec binds to a
catalog row (`catalog.intent`), copies its Description verbatim, and accounts for every
clause of that Description in `catalog.facets`. `audit()` checks all of that.

Tiers come from intents/_catalog_policy.yaml (derived from Class, Scoring path, Verifiable):
  required      a deterministic answer exists: a spec is REQUIRED, the gate fails closed without one
  judgment      no deterministic truth (catalog class/path says so): LLM judge only, SKIP is allowed
  unverifiable  catalog marks Verifiable = No: BLOCKED with the catalog's own reason
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .errors import SpecError
from .spec import DEFAULT_DIR, ROOT, IntentSpec, Registry

XLSX = ROOT / "Intent Catalog v2 25-Sept (1).xlsx"
INDEX = DEFAULT_DIR / "_catalog.json"
POLICY = DEFAULT_DIR / "_catalog_policy.yaml"
BUILD_SHEET = ROOT / "INTENT_BUILD_SHEET-2026-09-23.md"

COLUMNS = {  # xlsx header -> index field
    "Priority Score": "priority", "Category": "category", "Intent": "intent", "Class": "cls", "Why": "why",
    "Needs dataset?": "needs_dataset", "Needs adapter?": "needs_adapter", "Scoring path": "scoring_path",
    "Description": "description", "Data Source Type": "data_source_type", "Primary Aggregator / Hubs": "hubs",
    "How to Scale to 10+ Miners Instantly": "scale_note", "Target Latency": "target_latency",
    "Miners Integrated": "miners_integrated", "Ranking Supported": "ranking_supported",
    "Evaluation Mechanism": "evaluation", "Status": "status", "Verification Complexity": "verification_complexity",
    "Verifiable": "verifiable", "Verifiability Reason": "verifiability_reason",
}


@dataclass
class CatalogEntry:
    intent: str
    section: str = ""
    priority: Any = None
    category: str = ""
    cls: str = ""
    why: str = ""
    needs_dataset: str = ""
    needs_adapter: str = ""
    scoring_path: str = ""
    description: str = ""
    data_source_type: str = ""
    hubs: str = ""
    scale_note: str = ""
    target_latency: str = ""
    miners_integrated: Any = None
    ranking_supported: Any = None
    evaluation: str = ""
    status: str = ""
    verification_complexity: str = ""
    verifiable: str = ""
    verifiability_reason: str = ""
    build_sheet_description: str = ""
    tier: str = ""
    tier_reason: str = ""


def _clean(v: Any) -> Any:
    if isinstance(v, str):
        return re.sub(r"\s+", " ", v).strip()
    return v


def parse_xlsx(path: Path = XLSX) -> dict[str, CatalogEntry]:
    import openpyxl  # in the venv (also used for ACTIVE_MINERS.xlsx)
    if not path.is_file():
        raise SpecError(f"catalog workbook not found: {path}")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb["Intent Catalog"] if "Intent Catalog" in wb.sheetnames else wb.worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    hdr = [str(h).strip() if h else "" for h in rows[0]]
    missing = [h for h in COLUMNS if h not in hdr]
    if missing:
        raise SpecError(f"{path.name}: catalog columns missing: {missing}")
    out: dict[str, CatalogEntry] = {}
    section = ""
    for r in rows[1:]:
        d = dict(zip(hdr, r))
        if not d.get("Intent"):
            section = _clean(r[0]) or section          # "Mandatory Intents", "Existing Intents", ...
            continue
        e = CatalogEntry(intent=_clean(d["Intent"]), section=section or "")
        for h, f in COLUMNS.items():
            if f != "intent":
                v = _clean(d.get(h))
                setattr(e, f, "" if v is None else v)
        if e.intent in out:
            raise SpecError(f"{path.name}: duplicate catalog intent {e.intent}")
        out[e.intent] = e
    return out


def build_sheet_descriptions(path: Path = BUILD_SHEET) -> dict[str, str]:
    """`**Description (what the miner must answer):**` blocks per intent, for cross-checking."""
    if not path.is_file():
        return {}
    out = {}
    for sec in re.split(r"\n### ", path.read_text(encoding="utf-8")):
        m = re.match(r"(?:<span[^>]*>)?`([A-Z0-9_]+)`", sec)
        d = re.search(r"\*\*Description \(what the miner must answer\):\*\*\s*\n\s*\n> (.+)", sec)
        if m and d:
            out[m.group(1)] = _clean(d.group(1))
    return out


def load_policy(path: Path = POLICY) -> dict:
    try:
        p = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as e:
        raise SpecError(f"{path}: {e}") from None
    for k in ("tiers", "aliases"):
        if k not in p:
            raise SpecError(f"{path}: missing {k!r}")
    return p


def tier_of(e: CatalogEntry, policy: dict) -> tuple[str, str]:
    ov = (policy.get("overrides") or {}).get(e.intent)
    if ov:
        return ov["tier"], f"policy override: {ov['reason']}"
    for name, rule in policy["tiers"].items():
        conds = []
        if "verifiable" in rule:
            conds.append(str(e.verifiable).strip().lower() == str(rule["verifiable"]).lower())
        if "class" in rule:
            conds.append(e.cls in rule["class"])
        if conds and all(conds):
            reason = (f"Verifiable={e.verifiable}: {e.verifiability_reason}" if name == "unverifiable"
                      else f"Class={e.cls}, Scoring path={e.scoring_path}")
            return name, reason
    return policy.get("default_tier", "required"), f"Class={e.cls}, Scoring path={e.scoring_path}"


def build_index(xlsx: Path = XLSX, policy_path: Path = POLICY) -> dict[str, CatalogEntry]:
    entries = parse_xlsx(xlsx)
    policy = load_policy(policy_path)
    sheet = build_sheet_descriptions()
    for e in entries.values():
        e.build_sheet_description = sheet.get(e.intent, "")
        e.tier, e.tier_reason = tier_of(e, policy)
    return entries


def write_index(entries: dict[str, CatalogEntry], path: Path = INDEX) -> None:
    payload = {"_doc": f"Generated from {XLSX.name} by `python -m minercheck catalog build`. Do not edit by hand.",
               "intents": {k: asdict(v) for k, v in sorted(entries.items())}}
    path.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def load_index(path: Path = INDEX) -> dict[str, CatalogEntry]:
    if not path.is_file():
        raise SpecError(f"{path} missing: run `python -m minercheck catalog build`")
    data = json.loads(path.read_text(encoding="utf-8"))["intents"]
    return {k: CatalogEntry(**v) for k, v in data.items()}


class Catalog:
    """Index + policy + name aliasing (on-chain/canonical names <-> catalog names)."""

    def __init__(self, directory: Path = DEFAULT_DIR) -> None:
        self.entries = load_index(directory / "_catalog.json")
        self.policy = load_policy(directory / "_catalog_policy.yaml")
        self.to_catalog = {k.upper(): v for k, v in (self.policy.get("aliases") or {}).items()}

    def entry(self, intent: str) -> CatalogEntry | None:
        name = (intent or "").strip().upper()
        return self.entries.get(self.to_catalog.get(name, name))

    def canonical_names(self, catalog_intent: str) -> list[str]:
        return [catalog_intent] + [k for k, v in self.to_catalog.items() if v == catalog_intent]


# ------------------------------------------------------------------ audit
def description_clauses(text: str) -> list[str]:
    """'Provides real-time ambient temperature, humidity, precipitation rate, and wind vectors by
    coordinates.' -> ['provides real-time ambient temperature', 'humidity', 'precipitation rate',
    'wind vectors by coordinates']. Parentheticals and one-word verb fragments are dropped."""
    t = re.sub(r"\([^)]*\)", "", text).strip().rstrip(".").lower()
    parts = re.split(r",\s*(?:and\s+)?|\s+and\s+", t)
    return [p.strip() for p in parts if len(p.strip().split()) > 1]


def audit_spec(spec: IntentSpec, cat: Catalog) -> list[str]:
    """Problems that make a spec NOT aligned with the catalog (empty list = aligned)."""
    c = spec.catalog or {}
    if not c:
        return ["spec has no catalog: block (must bind to a catalog intent, or set catalog: {local_only: true})"]
    if c.get("local_only"):
        return []
    e = cat.entry(c.get("intent", ""))
    if e is None:
        return [f"catalog.intent {c.get('intent')!r} is not in the Intent Catalog"]
    errs = []
    if c.get("description") != e.description:
        errs.append(f"catalog.description differs from the catalog row (copy it verbatim):\n      catalog: {e.description}\n      spec:    {c.get('description')}")
    if e.tier != "required":
        errs.append(f"catalog tier is {e.tier} ({e.tier_reason}); a deterministic spec contradicts the catalog")
    facets = c.get("facets") or []
    texts = [str(f.get("text", "")).lower() for f in facets]
    for f in facets:
        if str(f.get("text", "")).lower() not in e.description.lower():
            errs.append(f"facet {f.get('text')!r} is not a phrase of the catalog Description")
    for clause in description_clauses(e.description):
        if not any(t and t in clause for t in texts):
            errs.append(f"Description clause {clause!r} has no facet (say how it is covered, or covered_by: none + note)")
    primary = [f for f in facets if f.get("covered_by") == "value"]
    if len(primary) != 1:
        errs.append(f"exactly one facet must be covered_by: value (the verified answer); found {len(primary)}")
    names = {f"{p}" for p in spec.inputs}
    for f in facets:
        cov = str(f.get("covered_by", ""))
        if cov.startswith("extra:") and cov[6:] not in spec.extras:
            errs.append(f"facet {f.get('text')!r}: extra {cov[6:]!r} is not declared")
        if cov.startswith("input:") and cov[6:] not in names:
            errs.append(f"facet {f.get('text')!r}: input {cov[6:]!r} is not declared")
    kinds = set(c.get("allowed_kinds") or [])
    for s in spec.sources:
        if not s.kind:
            errs.append(f"source {s.id}: kind missing (needed to check the catalog's Data Source Type)")
        elif kinds and s.kind not in kinds and not s.miner_slug:
            errs.append(f"source {s.id}: kind {s.kind!r} is not allowed by the catalog for this intent; "
                        f"only miners should be listed with a disallowed kind (so they fail with the reason)")
    return errs


def coverage(spec: IntentSpec) -> list[dict]:
    return list((spec.catalog or {}).get("facets") or [])


def table(cat: Catalog, reg: Registry, wave2: dict[str, list[str]]) -> list[dict]:
    rows = []
    for name, e in sorted(cat.entries.items(), key=lambda kv: (kv[1].tier != "required", kv[0])):
        spec = next((s for s in reg.specs.values() if (s.catalog or {}).get("intent") == name), None)
        slugs = sorted({s for alias in cat.canonical_names(name) for s in wave2.get(alias, [])})
        rows.append({"intent": name, "tier": e.tier, "class": e.cls, "description": e.description,
                     "spec": spec.intent if spec else "", "aligned": (not audit_spec(spec, cat)) if spec else None,
                     "wave2": slugs})
    return rows
