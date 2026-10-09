"""Intent spec loader. intents/<INTENT>.yaml is the single source of truth for
how an intent is asked, fetched, extracted, checked and rendered.

Validation happens at load time and is strict: unknown keys, missing mandatory
fields, unknown {placeholders}, unreachable min_sources... all raise SpecError
with every problem listed. A bad spec never reaches a network call.
"""
from __future__ import annotations

import difflib
import re
from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml

from .answers import ANSWER_TYPES
from .errors import SpecError
from .reader import LOCATORS

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "intents"

INPUT_KINDS = ("location", "asset", "currency", "timezone", "enum", "text", "table")
EXTRA_QUANTITIES = ("temperature", "speed", "percent", "number", "money", "text", "datetime", "direction",
                    "precipitation", "boolean")
META_VARS = {"value", "agreeing_count", "answered_count", "queried_count", "agreeing_sources",
             "confidence", "as_of", "primary_source", "reason", "unit_label", "verified_by"}
# Variables each input kind exports to URL/rule/template placeholders.
KIND_VARS = {
    "location": {"lat", "lon", "place", "country", "timezone", "bbox"},
    "timezone": {"timezone", "tz_label"},
    "asset": {"symbol", "symbol_lower", "asset_name"},
}
TYPE_VARS = {"fx_rate": {"converted"}, "date": {"iso_date", "weekday"},
             "datetime_tz": {"time", "date", "weekday", "tz_abbr", "utc_offset", "iso"}}
RULE_MODS = {"unit", "scale", "tz", "epoch", "format", "invert", "date_order", "time_of_day",
             "attr", "index", "group", "flags", "where", "row", "regex",
             "each", "exists", "aggregate", "price", "size", "flat", "map", "hex"}

# ---------------------------------------------------------------- schema
# key -> (type(s), required). Nested dict schemas are validated recursively.
_RULE = "rule"
SCHEMA: dict[str, Any] = {
    "intent": (str, True),
    "aliases": (list, False),
    "description": (str, True),
    "answer_type": (str, True),
    "scope": (str, False),
    "inputs": (dict, True),
    "normalize": (dict, False),
    "units": ({"canonical": (str, False), "render_input": (str, False), "render": (dict, False)}, False),
    "validation": ({
        "sanity": ({"min": ((int, float, str), False), "max": ((int, float, str), False),
                    "max_days_from_today": (int, False)}, False),
        "freshness": ({"max_age_s": (int, False), "max_future_s": (int, False),
                       "require_timestamp": (bool, False)}, False),
        "entity": ({"max_km": ((int, float), False)}, False),
        "cross_check": ({"tolerance": ({"abs": ((int, float, str), False), "rel": ((int, float, str), False)}, True),
                         "min_sources": (int, True), "target_sources": (int, False)}, True),
    }, True),
    "extras": (dict, False),
    "sources": (list, True),
    "template": ({"answer": (str, True), "extras": (list, False), "footer": (str, False),
                  "unverified": (str, True), "yes": (str, False), "no": (str, False)}, True),
    "tests": (list, False),
    "catalog": ({"intent": (str, False), "description": (str, False), "local_only": (bool, False),
                 "facets": (list, False), "allowed_kinds": (list, False), "notes": (str, False)}, True),
}
FACET_SCHEMA = {"text": (str, True), "covered_by": (str, True), "required": (bool, False), "note": (str, False)}
INPUT_SCHEMA = {"kind": (str, True), "required": (bool, False), "default": ((str, int, float), False),
                "description": (str, False), "values": (list, False), "aliases": (dict, False),
                "table": (str, False)}
SOURCE_SCHEMA = {
    "id": (str, True), "name": (str, True), "publisher": (str, True), "enabled": (bool, False),
    "kind": (str, True), "authority": (bool, False), "when": (dict, False),
    "miner": ({"slug": (str, True), "question": (dict, True)}, False),
    "request": ({"url": (str, True), "method": (str, False), "headers": (dict, False), "body": (str, False),
                 "timeout_s": ((int, float), False)}, True),
    "cache_ttl_s": (int, False), "rate_limit_per_min": (int, False),
    "free_tier": ({"requests_per_day": (int, False), "requests_per_month": (int, False)}, False),
    "freshness_max_age_s": (int, False),
    "value": (list, True), "timestamp": (list, False), "entity": (dict, False), "extras": (dict, False),
    "notes": (str, False),
}
EXTRA_SCHEMA = {"quantity": (str, True), "unit": (str, False), "signed": (bool, False),
                "sanity": ({"min": ((int, float), False), "max": ((int, float), False)}, False)}
ENTITY_KEYS = {"lat", "lon", "symbol", "base", "quote", "timezone", "country", "place", "name"}
TEST_SCHEMA = {"id": (str, True), "inputs": (dict, True)}


def _check(obj: Any, schema: dict, where: str, errs: list[str]) -> None:
    if not isinstance(obj, dict):
        errs.append(f"{where}: must be a mapping, got {type(obj).__name__}")
        return
    for k in obj:
        if k not in schema:
            hint = difflib.get_close_matches(str(k), list(schema), n=1)
            errs.append(f"{where}: unknown key {k!r}" + (f" (did you mean {hint[0]!r}?)" if hint else ""))
    for k, (typ, req) in schema.items():
        if k not in obj or obj[k] is None:
            if req:
                errs.append(f"{where}: missing required key {k!r}")
            continue
        v = obj[k]
        if isinstance(typ, dict):
            _check(v, typ, f"{where}.{k}", errs)
            continue
        types = typ if isinstance(typ, tuple) else (typ,)
        # bool is an int subclass: `min: true` must not pass as a number
        if not isinstance(v, types) or (isinstance(v, bool) and bool not in types):
            errs.append(f"{where}.{k}: must be {'/'.join(t.__name__ for t in types)}, got {type(v).__name__}")


def _check_rules(rules: Any, where: str, errs: list[str], *, allow_empty: bool = False) -> None:
    if not isinstance(rules, list) or (not rules and not allow_empty):
        errs.append(f"{where}: must be a non-empty list of extraction rules")
        return
    for i, r in enumerate(rules):
        w = f"{where}[{i}]"
        if not isinstance(r, dict):
            errs.append(f"{w}: rule must be a mapping like {{json: a.b}}")
            continue
        locs = [k for k in LOCATORS if k in r]
        primary = [k for k in locs if k != "regex"]
        if len(primary) > 1 or not locs:
            errs.append(f"{w}: needs exactly one of {', '.join(LOCATORS)} (regex may also post-filter)")
        for k in r:
            if k not in LOCATORS and k not in RULE_MODS:
                hint = difflib.get_close_matches(k, list(LOCATORS) + sorted(RULE_MODS), n=1)
                errs.append(f"{w}: unknown key {k!r}" + (f" (did you mean {hint[0]!r}?)" if hint else ""))
        if "epoch" in r and r["epoch"] not in ("s", "ms"):
            errs.append(f"{w}.epoch: must be s or ms")
        if "date_order" in r and str(r["date_order"]).upper() not in ("MDY", "DMY"):
            errs.append(f"{w}.date_order: must be MDY or DMY")


# ---------------------------------------------------------------- model
@dataclass
class InputSpec:
    name: str
    kind: str
    required: bool = False
    default: Any = None
    description: str = ""
    values: list[str] = field(default_factory=list)
    aliases: dict[str, str] = field(default_factory=dict)
    table: str = ""                  # kind=table: normalize.<table> rows keyed by id


@dataclass
class SourceSpec:
    id: str
    name: str
    publisher: str
    priority: int
    url: str
    method: str = "GET"
    headers: dict[str, str] = field(default_factory=dict)
    body: str | None = None
    timeout_s: float = 15.0
    cache_ttl_s: int = 60
    rate_limit_per_min: int | None = None
    requests_per_day: int | None = None
    freshness_max_age_s: int | None = None
    value: list[dict] = field(default_factory=list)
    timestamp: list[dict] = field(default_factory=list)
    entity: dict[str, list[dict]] = field(default_factory=dict)
    extras: dict[str, list[dict]] = field(default_factory=dict)
    miner_slug: str | None = None
    miner_question: dict[str, Any] = field(default_factory=dict)
    enabled: bool = True
    kind: str = ""
    authority: bool = False          # official record holder: a valid answer is verified on its own
    when: dict[str, str] = field(default_factory=dict)   # only query this source when inputs match


@dataclass
class Validation:
    sanity_min: Decimal | None
    sanity_max: Decimal | None
    max_days_from_today: int | None
    max_age_s: int | None
    max_future_s: int
    require_timestamp: bool
    max_km: float | None
    tol_abs: Decimal | None
    tol_rel: Decimal | None
    min_sources: int
    target_sources: int

    def tolerance(self, ref: Decimal) -> Decimal:
        """Allowed |deviation| around ref: the larger of abs and rel*|ref|."""
        parts = [t for t in (self.tol_abs, (self.tol_rel * abs(ref)) if self.tol_rel is not None else None) if t is not None]
        return max(parts) if parts else Decimal(0)


@dataclass
class IntentSpec:
    intent: str
    aliases: list[str]
    description: str
    answer_type: str
    scope: str
    inputs: dict[str, InputSpec]
    normalize: dict[str, Any]
    canonical_unit: str
    render_input: str | None
    render_units: dict[str, dict[str, str]]
    validation: Validation
    extras: dict[str, dict]
    template: dict[str, Any]
    sources: list[SourceSpec]
    tests: list[dict]
    path: Path | None = None
    catalog: dict[str, Any] = field(default_factory=dict)

    def source(self, source_id: str) -> SourceSpec:
        for s in self.sources:
            if s.id == source_id:
                return s
        raise KeyError(source_id)

    def by_miner(self, slug: str) -> SourceSpec | None:
        return next((s for s in self.sources if s.miner_slug == slug), None)

    def variables(self) -> set[str]:
        out = set(META_VARS) | TYPE_VARS.get(self.answer_type, set())
        for name, inp in self.inputs.items():
            out |= KIND_VARS.get(inp.kind, set())
            if inp.kind in ("currency", "enum", "text", "table"):
                out |= {name, f"{name}_lower"}
            if inp.kind == "table":
                for row in ((self.normalize or {}).get(inp.table) or {}).values():
                    if isinstance(row, dict):
                        out |= {k for k in row if k != "aliases"}
        assets = (self.normalize or {}).get("assets") or {}
        for row in assets.values():
            if isinstance(row, dict):
                out |= {k for k in row if k not in ("aliases",)}
        return out


_PH = re.compile(r"\{(\w+)(?:[:!][^}]*)?\}")


def _placeholders(s: Any) -> set[str]:
    return set(_PH.findall(s)) if isinstance(s, str) else set()


def _dec(v: Any) -> Decimal | None:
    return None if v is None else Decimal(str(v))


def build(doc: dict, path: Path | None = None) -> IntentSpec:
    where = str(path.name if path else "<spec>")
    errs: list[str] = []
    _check(doc, SCHEMA, where, errs)
    if errs:
        raise SpecError("invalid intent spec:\n  " + "\n  ".join(errs))

    at = doc["answer_type"]
    if at not in ANSWER_TYPES:
        errs.append(f"{where}.answer_type: {at!r} is not one of {', '.join(ANSWER_TYPES)}")
    if path and path.stem != doc["intent"]:
        errs.append(f"{where}: file name must be {doc['intent']}.yaml")

    inputs: dict[str, InputSpec] = {}
    for name, raw in (doc.get("inputs") or {}).items():
        _check(raw, INPUT_SCHEMA, f"{where}.inputs.{name}", errs)
        if not isinstance(raw, dict):
            continue
        if raw.get("kind") not in INPUT_KINDS:
            errs.append(f"{where}.inputs.{name}.kind: {raw.get('kind')!r} is not one of {', '.join(INPUT_KINDS)}")
        if raw.get("kind") == "enum" and not raw.get("values"):
            errs.append(f"{where}.inputs.{name}: enum needs values")
        if raw.get("kind") == "table" and not (doc.get("normalize") or {}).get(raw.get("table", "")):
            errs.append(f"{where}.inputs.{name}: kind table needs table: <name of a normalize.<table> mapping>")
        inputs[name] = InputSpec(name, raw.get("kind", ""), bool(raw.get("required", False)), raw.get("default"),
                                 raw.get("description", ""), [str(v) for v in raw.get("values") or []],
                                 {str(k).lower(): str(v) for k, v in (raw.get("aliases") or {}).items()},
                                 str(raw.get("table", "")))
    kinds = [i.kind for i in inputs.values()]
    for k in ("location", "asset", "timezone"):
        if kinds.count(k) > 1:
            errs.append(f"{where}.inputs: at most one input of kind {k}")

    v = doc["validation"]
    cc = v["cross_check"]
    tol = cc.get("tolerance") or {}
    if "abs" not in tol and "rel" not in tol:
        errs.append(f"{where}.validation.cross_check.tolerance: give abs and/or rel")
    val = Validation(
        sanity_min=_dec((v.get("sanity") or {}).get("min")), sanity_max=_dec((v.get("sanity") or {}).get("max")),
        max_days_from_today=(v.get("sanity") or {}).get("max_days_from_today"),
        max_age_s=(v.get("freshness") or {}).get("max_age_s"),
        max_future_s=int((v.get("freshness") or {}).get("max_future_s", 600)),
        require_timestamp=bool((v.get("freshness") or {}).get("require_timestamp", False)),
        max_km=(v.get("entity") or {}).get("max_km"),
        tol_abs=_dec(tol.get("abs")), tol_rel=_dec(tol.get("rel")),
        min_sources=int(cc["min_sources"]), target_sources=int(cc.get("target_sources", cc["min_sources"] + 1)),
    )
    extras = {}
    for name, raw in (doc.get("extras") or {}).items():
        _check(raw, EXTRA_SCHEMA, f"{where}.extras.{name}", errs)
        if isinstance(raw, dict) and raw.get("quantity") not in EXTRA_QUANTITIES:
            errs.append(f"{where}.extras.{name}.quantity: must be one of {', '.join(EXTRA_QUANTITIES)}")
        extras[name] = raw if isinstance(raw, dict) else {}

    sources: list[SourceSpec] = []
    seen_ids: set[str] = set()
    for i, raw in enumerate(doc.get("sources") or []):
        w = f"{where}.sources[{i}]"
        _check(raw, SOURCE_SCHEMA, w, errs)
        if not isinstance(raw, dict) or "id" not in raw:
            continue
        if raw["id"] in seen_ids:
            errs.append(f"{w}: duplicate source id {raw['id']!r}")
        seen_ids.add(raw["id"])
        _check_rules(raw.get("value"), f"{w}.value", errs)
        if "timestamp" in raw:
            _check_rules(raw["timestamp"], f"{w}.timestamp", errs)
        for ek, er in (raw.get("entity") or {}).items():
            if ek not in ENTITY_KEYS:
                errs.append(f"{w}.entity: unknown key {ek!r} (allowed: {', '.join(sorted(ENTITY_KEYS))})")
            _check_rules(er, f"{w}.entity.{ek}", errs)
        for xk, xr in (raw.get("extras") or {}).items():
            if xk not in extras:
                errs.append(f"{w}.extras.{xk}: not declared in top-level extras")
            _check_rules(xr, f"{w}.extras.{xk}", errs)
        for wk in (raw.get("when") or {}):
            if wk not in inputs:
                errs.append(f"{w}.when: {wk!r} is not a declared input")
        miner = raw.get("miner") or {}
        for qk in (miner.get("question") or {}):
            if qk not in inputs:
                errs.append(f"{w}.miner.question: {qk!r} is not a declared input")
        req = raw.get("request") or {}
        method = str(req.get("method", "GET")).upper()
        if method not in ("GET", "POST", "HEAD"):
            errs.append(f"{w}.request.method: {method} not supported (GET/POST/HEAD)")
        sources.append(SourceSpec(
            id=raw["id"], name=raw.get("name", raw["id"]), publisher=raw.get("publisher", ""), priority=i,
            url=req.get("url", ""), method=method, headers={str(k): str(x) for k, x in (req.get("headers") or {}).items()},
            body=req.get("body"), timeout_s=float(req.get("timeout_s", 15)), cache_ttl_s=int(raw.get("cache_ttl_s", 60)),
            rate_limit_per_min=raw.get("rate_limit_per_min"),
            requests_per_day=(raw.get("free_tier") or {}).get("requests_per_day"),
            freshness_max_age_s=raw.get("freshness_max_age_s"),
            value=raw.get("value") or [], timestamp=raw.get("timestamp") or [], entity=raw.get("entity") or {},
            extras=raw.get("extras") or {}, miner_slug=miner.get("slug"), miner_question=miner.get("question") or {},
            enabled=bool(raw.get("enabled", True)), kind=str(raw.get("kind", "")), authority=bool(raw.get("authority", False)),
            when={str(k): str(v) for k, v in (raw.get("when") or {}).items()},
        ))

    units = doc.get("units") or {}
    spec = IntentSpec(
        intent=doc["intent"], aliases=[str(a) for a in doc.get("aliases") or []], description=doc["description"],
        answer_type=at, scope=doc.get("scope", "current"), inputs=inputs, normalize=doc.get("normalize") or {},
        canonical_unit=units.get("canonical", ""), render_input=units.get("render_input"),
        render_units=units.get("render") or {}, validation=val, extras=extras, template=doc["template"],
        sources=sources, tests=doc.get("tests") or [], path=path, catalog=doc.get("catalog") or {},
    )
    spec_vars = spec.variables()
    for i, f in enumerate(spec.catalog.get("facets") or []):
        _check(f, FACET_SCHEMA, f"{where}.catalog.facets[{i}]", errs)
        cov = str((f or {}).get("covered_by", "")) if isinstance(f, dict) else ""
        if cov and not (cov in ("value", "none") or cov.split(":", 1)[0] in ("extra", "entity", "input")):
            errs.append(f"{where}.catalog.facets[{i}].covered_by: use value | extra:<name> | entity:<key> | input:<name> | none")
        if isinstance(f, dict) and f.get("required") and cov.startswith("extra:") and cov[6:] not in extras:
            errs.append(f"{where}.catalog.facets[{i}]: required extra {cov[6:]!r} is not declared")

    # placeholders must resolve
    for s in sources:
        w = f"{where}.sources[{s.id}]"
        used = _placeholders(s.url) | _placeholders(s.body) | set().union(*[_placeholders(x) for x in s.headers.values()] or [set()])
        for rules in [s.value, s.timestamp, *s.entity.values(), *s.extras.values()]:
            for r in rules:
                for k in ("json", "xpath", "css", "csv", "header", "regex", "unit", "tz"):
                    used |= _placeholders(r.get(k))
        bad = sorted(used - spec_vars)
        if bad:
            errs.append(f"{w}: unknown placeholder(s) {', '.join('{'+b+'}' for b in bad)}")
        if s.miner_slug:
            missing = [n for n, inp in inputs.items() if inp.required and n not in s.miner_question]
            if missing:
                errs.append(f"{w}.miner.question: missing required input(s) {missing}")
    tvars = spec_vars | set(extras)
    for key in ("answer", "footer", "unverified"):
        bad = sorted(_placeholders(spec.template.get(key)) - tvars)
        if bad:
            errs.append(f"{where}.template.{key}: unknown placeholder(s) {bad}")
    for i, sentence in enumerate(spec.template.get("extras") or []):
        bad = sorted(_placeholders(sentence) - tvars)
        if bad:
            errs.append(f"{where}.template.extras[{i}]: unknown placeholder(s) {bad}")

    pubs = {s.publisher for s in sources if s.enabled}
    has_authority = any(s.authority and s.enabled for s in sources)
    if val.min_sources < 2 and not has_authority:
        errs.append(f"{where}.validation.cross_check.min_sources: must be >= 2 unless a source has authority: true "
                    "(one non-authoritative source cannot verify itself)")
    if len(pubs) < val.min_sources:
        errs.append(f"{where}: only {len(pubs)} enabled publisher(s) but min_sources={val.min_sources}; it can never verify")
    for i, t in enumerate(spec.tests):
        _check(t, TEST_SCHEMA, f"{where}.tests[{i}]", errs)
        for k in (t.get("inputs") or {}) if isinstance(t, dict) else {}:
            if k not in inputs:
                errs.append(f"{where}.tests[{i}].inputs: {k!r} is not a declared input")
    if errs:
        raise SpecError("invalid intent spec:\n  " + "\n  ".join(errs))
    return spec


def load_file(path: Path) -> IntentSpec:
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        raise SpecError(f"{path}: YAML does not parse: {e}") from None
    if not isinstance(doc, dict):
        raise SpecError(f"{path}: top level must be a mapping")
    return build(doc, path)


def load_shared(directory: Path = DEFAULT_DIR) -> dict:
    p = directory / "_shared.yaml"
    if not p.is_file():
        return {}
    try:
        d = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        raise SpecError(f"{p}: YAML does not parse: {e}") from None
    if not isinstance(d, dict):
        raise SpecError(f"{p}: top level must be a mapping")
    return d


class Registry:
    """All specs in a directory, addressable by intent name or alias."""

    def __init__(self, directory: Path = DEFAULT_DIR) -> None:
        self.directory = directory
        self.specs: dict[str, IntentSpec] = {}
        self.alias: dict[str, str] = {}
        problems = []
        for p in sorted(directory.glob("*.yaml")):
            if p.name.startswith("_"):
                continue
            try:
                s = load_file(p)
            except SpecError as e:
                problems.append(str(e))
                continue
            self.specs[s.intent] = s
            for a in [s.intent, *s.aliases]:
                if a.upper() in self.alias and self.alias[a.upper()] != s.intent:
                    problems.append(f"{p.name}: alias {a} already used by {self.alias[a.upper()]}")
                self.alias[a.upper()] = s.intent
        if problems:
            raise SpecError("\n".join(problems))
        self.shared = load_shared(directory)

    def get(self, intent: str) -> IntentSpec | None:
        name = self.alias.get((intent or "").strip().upper())
        return self.specs.get(name) if name else None
