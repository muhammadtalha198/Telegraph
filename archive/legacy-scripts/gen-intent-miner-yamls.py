#!/usr/bin/env python3
"""Generate one Telegraph miner YAML per (intent, API provider) pair.

Reads MinerCreator/apiRegistry/*.json (see apiRegistry/SCHEMA.md) and writes
MinerCreator/intentYamls/<intent-slug>/<miner-slug>.yaml

Each provider's `inputs[]` drives two things:
  * the endpoint `params` block (what the dispatcher forwards upstream), and
  * the top-level `input_schema` (what Alexandria's Direct Request panel renders
    as input fields).

Run: ./.venv-xlsx/bin/python scripts/gen-intent-miner-yamls.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

MC = Path(__file__).resolve().parents[1]
REGISTRY = MC / "apiRegistry"
OUT = MC / "intentYamls"
OUT_JSON = MC / "out"
ID_START = 30001

# Catalog intents that are not in the on-chain canonical registry. The node's
# validate endpoint rejects non-canonical intents outright, so where a
# defensible canonical equivalent exists we register under that and keep the
# catalog name in the description. Intents with no honest equivalent stay as-is
# and are reported as blocked until governance calls addIntent().
CANONICAL_ALIAS = {
    "WEATHER_CURRENT": "WEATHER_CHECK",
    "CRYPTO_PRICE_LOOKUP": "CRYPTO_PRICE",
    "CRYPTO_TRANSFER_VERIFY": "ONCHAIN_TX_LOOKUP",
    "GAS_PRICE_ESTIMATION": "GAS_PRICE",
    "TOKEN_TOTAL_SUPPLY_VERIFY": "ONCHAIN_METRIC_VERIFY",
    "SMART_CONTRACT_AUDIT": "SECURITY_REVIEW",
    "CRYPTO_YIELD_RATE": "FINANCIAL_DATA",
    "STOCK_PRICE_QUOTE": "STOCK_PRICE",
    "LOAN_INTEREST_RATE_QUOTE": "FINANCIAL_DATA",
    "THREAT_IP_REPUTATION": "THREAT_INTELLIGENCE",
    "SSL_CERTIFICATE_VERIFY": "SSL_VERIFICATION",
    "FACT_CHECKING": "FACT_CHECK",
    "PLAGIARISM_DETECTION": "TEXT_AUTHENTICITY_CHECK",
    "TOXICITY_MODERATION": "CONTENT_MODERATION",
    "WEB_SEARCH_QUERY": "WEB_SEARCH",
    "URL_CONTENT_EXTRACTION": "CONTENT_EXTRACTION",
    "TEXT_SUMMARIZATION": "TEXT_GENERATION",
    "QUESTION_ANSWERING": "RESEARCH_QUERY",
    "CHATBOT_CONVERSATION": "CHAT_COMPLETION",
    "SERVER_UPTIME_MONITOR": "SLA_COMPLIANCE",
    "API_HEALTH_CHECK": "SLA_COMPLIANCE",
    "CLOUD_RESOURCE_USAGE": "DATACENTER_TELEMETRY_VERIFY",
    "MEDIA_FORENSIC_VERIFY": "MEDIA_AUTHENTICITY_CHECK",
}

AUTH_TYPE = {
    "none": "none",
    "self_host": "none",
    "free_key": "bearer",
    "oauth": "bearer",
    "paid": "bearer",
}


def slugify(value: str, limit: int = 60) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (value or "").lower())
    return re.sub(r"-{2,}", "-", s).strip("-")[:limit]


def one_line(value: str, limit: int = 220) -> str:
    s = re.sub(r"\s+", " ", str(value or "")).strip()
    return s[:limit]


def param_entry(inp: dict) -> OrderedDict:
    """One entry in an endpoint params group."""
    e = OrderedDict()
    e["name"] = inp.get("upstream") or inp["name"]
    e["type"] = "string" if inp.get("type") in (None, "number", "integer", "boolean") else inp["type"]
    e["intents"] = ["*"]
    e["description"] = one_line(inp.get("description") or inp["name"], 160)
    return e


def build_params(inputs: list[dict]) -> tuple[OrderedDict, OrderedDict]:
    """Return (params block, param_map) for the endpoint."""
    groups: dict[str, dict[str, list]] = {}
    param_map = OrderedDict()
    for inp in inputs:
        where = inp.get("in") or "query"
        if where not in ("query", "path", "body", "header", "multipart"):
            where = "query"
        bucket = "required" if inp.get("required") else "optional"
        groups.setdefault(where, {}).setdefault(bucket, []).append(param_entry(inp))
        upstream = inp.get("upstream")
        if where == "query" and upstream and upstream != inp["name"]:
            param_map[inp["name"]] = upstream

    params = OrderedDict()
    for where in ("path", "query", "body", "header", "multipart"):
        if where not in groups:
            continue
        section = OrderedDict()
        for bucket in ("required", "optional"):
            if groups[where].get(bucket):
                section[bucket] = groups[where][bucket]
        params[where] = section
    return params, param_map


def build_input_schema(inputs: list[dict]) -> OrderedDict | None:
    """JSON Schema that Alexandria renders as Direct Request input fields."""
    if not inputs:
        return None
    props = OrderedDict()
    required = []
    for inp in inputs:
        name = inp["name"]
        prop = OrderedDict()
        prop["type"] = inp.get("type") or "string"
        prop["description"] = one_line(inp.get("description") or name, 160)
        if inp.get("enum"):
            prop["enum"] = inp["enum"]
        if inp.get("default") is not None:
            prop["default"] = inp["default"]
        props[name] = prop
        if inp.get("required"):
            required.append(name)
    schema = OrderedDict()
    schema["type"] = "object"
    if required:
        schema["required"] = required
    schema["properties"] = props
    return schema


def build_on_chain(intent: str, signal: dict) -> OrderedDict:
    fields = OrderedDict()
    strings = []
    for i, f in enumerate((signal.get("strings") or [])[:2]):
        e = OrderedDict()
        e["index"] = i
        e["name"] = slugify(f.get("name") or f"s{i}", 30).replace("-", "_") or f"s{i}"
        e["description"] = one_line(f.get("description") or e["name"], 120)
        e["source_path"] = f.get("source_path") or "result"
        strings.append(e)
    if not strings:
        strings = [
            OrderedDict(
                [("index", 0), ("name", "result"), ("description", "Primary result field"), ("source_path", "result")]
            )
        ]
    fields["strings"] = strings

    integers = []
    for i, f in enumerate((signal.get("integers") or [])[:2]):
        e = OrderedDict()
        e["index"] = i
        e["name"] = slugify(f.get("name") or f"i{i}", 30).replace("-", "_") or f"i{i}"
        e["description"] = one_line(f.get("description") or e["name"], 120)
        e["source_path"] = f.get("source_path") or "ok"
        if f.get("multiplier"):
            e["multiplier"] = f["multiplier"]
        integers.append(e)
    if integers:
        fields["integers"] = integers

    oc = OrderedDict()
    oc["description"] = f"Stores the primary signal for {intent}."
    oc["transform"] = "direct"
    oc["min_price_usdc"] = 0.01
    oc["fields"] = fields
    return oc


def apply_fixed_query(provider: dict, inputs: list[dict]) -> tuple[str, list[dict]]:
    """Fold provider constants into the request.

    The deployed dispatcher builds upstream URLs by appending `?<params>`, so an
    external_path that already carries a query string only survives when the
    miner sends no query params of its own. When it does, the constants are
    emitted as prefilled optional inputs instead so the URL stays valid.
    """
    fixed = provider.get("fixed_query") or {}
    path = provider["external_path"]
    if not fixed:
        return path, inputs

    has_query_input = any((i.get("in") or "query") == "query" for i in inputs)
    if not has_query_input:
        joiner = "&" if "?" in path else "?"
        return path + joiner + "&".join(f"{k}={v}" for k, v in fixed.items()), inputs

    extra = [
        {
            "name": k,
            "in": "query",
            "type": "string",
            "required": False,
            "description": f"Upstream constant for {provider['provider']}",
            "default": v,
        }
        for k, v in fixed.items()
        if k not in {i["name"] for i in inputs}
    ]
    return path, inputs + extra


def build_miner(yaml_id, miner_slug, catalog_intent, reg_intent, category, provider) -> OrderedDict:
    external_path, inputs = apply_fixed_query(provider, provider.get("inputs") or [])
    params, param_map = build_params(inputs)
    signal = provider.get("signal") or {}

    note_bits = [f"{catalog_intent} via {provider['provider']}."]
    if catalog_intent != reg_intent:
        note_bits.append(f"Catalog intent {catalog_intent} is not canonical on-chain; registered as {reg_intent}.")
    note_bits.append(f"Category: {category}. Auth: {provider.get('auth', 'none')}.")
    if provider.get("notes"):
        note_bits.append(one_line(provider["notes"], 200))

    m = OrderedDict()
    m["version"] = "1"
    m["kind"] = "miner"
    m["id"] = yaml_id
    m["slug"] = miner_slug
    m["protocol"] = "generic"
    m["name"] = one_line(f"{provider['provider']} {catalog_intent.replace('_', ' ').title()}", 60)
    m["description"] = " ".join(note_bits)
    m["base_url"] = provider["base_url"].rstrip("/")
    m["auth"] = OrderedDict([("type", AUTH_TYPE.get(provider.get("auth", "none"), "none"))])
    m["rate_limit_per_sec"] = 2
    m["cache_ttl_sec"] = 30
    m["circuit_threshold"] = 5
    m["circuit_cooldown_seconds"] = 30

    docs = OrderedDict()
    if provider.get("docs"):
        docs["documentation"] = provider["docs"]
    if provider.get("website"):
        docs["website"] = provider["website"]
    if docs:
        m["docs"] = docs

    ep = OrderedDict()
    ep["path"] = "/query"
    ep["external_path"] = external_path
    ep["method"] = provider.get("method", "GET").upper()
    ep["description"] = one_line(
        f"{catalog_intent} lookup through {provider['provider']}.", 200
    )
    ep["intents"] = [reg_intent]
    if param_map:
        ep["param_map"] = param_map
    if params:
        ep["params"] = params
    if ep["method"] == "POST":
        ep["content_type"] = provider.get("content_type", "application/json")
    m["endpoints"] = [ep]

    schema = build_input_schema(inputs)
    if schema:
        m["input_schema"] = schema

    sem = OrderedDict()
    label = (signal.get("label_field") or (signal.get("strings") or [{}])[0].get("source_path") or "result")
    sem["signal_mapping"] = OrderedDict([("label_field", label)])
    sem["supported_intents"] = [reg_intent]
    m["semantics"] = sem

    m["on_chain"] = build_on_chain(reg_intent, signal)
    return m


class Dumper(yaml.SafeDumper):
    pass


Dumper.add_representer(
    OrderedDict, lambda d, data: d.represent_mapping("tag:yaml.org,2002:map", data.items())
)


def main() -> int:
    files = sorted(p for p in REGISTRY.glob("*.json") if not p.name.startswith("_"))
    if not files:
        print(f"no registry files in {REGISTRY}", file=sys.stderr)
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.rglob("*.yaml"):
        old.unlink()

    manifest = []
    used_slugs: set[str] = set()
    next_id = ID_START
    problems = []

    for path in files:
        try:
            entries = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            problems.append(f"{path.name}: invalid JSON ({exc})")
            continue

        for entry in entries:
            catalog_intent = entry["intent"]
            category = entry.get("category", "")
            reg_intent = CANONICAL_ALIAS.get(catalog_intent, catalog_intent)
            intent_dir = OUT / slugify(catalog_intent)
            intent_dir.mkdir(parents=True, exist_ok=True)

            providers = entry.get("providers") or []
            if len(providers) < 10:
                problems.append(
                    f"{path.name}: {catalog_intent} has only {len(providers)} providers (need 10)"
                )

            for provider in providers:
                base = f"{slugify(catalog_intent, 28)}-{slugify(provider['slug'], 28)}"
                miner_slug = base
                n = 2
                while miner_slug in used_slugs:
                    miner_slug = f"{base[:56]}-{n}"
                    n += 1
                used_slugs.add(miner_slug)

                try:
                    doc = build_miner(
                        next_id, miner_slug, catalog_intent, reg_intent, category, provider
                    )
                except (KeyError, TypeError) as exc:
                    problems.append(f"{path.name}: {catalog_intent}/{provider.get('slug')}: {exc}")
                    continue

                text = yaml.dump(
                    doc, Dumper=Dumper, sort_keys=False, default_flow_style=False, width=100, allow_unicode=True
                )
                dest = intent_dir / f"{miner_slug}.yaml"
                dest.write_text(text)
                try:
                    rel = str(dest.relative_to(MC))
                except ValueError:
                    rel = str(dest)

                manifest.append(
                    {
                        "catalog_intent": catalog_intent,
                        "registered_intent": reg_intent,
                        "canonical_alias_applied": catalog_intent != reg_intent,
                        "category": category,
                        "provider": provider["provider"],
                        "auth": provider.get("auth", "none"),
                        "live_verified": bool((provider.get("verify") or {}).get("checked")),
                        "base_url": provider["base_url"],
                        "external_path": provider["external_path"],
                        "method": provider.get("method", "GET"),
                        "input_fields": [i["name"] for i in (provider.get("inputs") or [])],
                        "yaml_id": next_id,
                        "slug": miner_slug,
                        "file": rel,
                        "docs": provider.get("docs", ""),
                        "group": path.stem,
                    }
                )
                next_id += 1

    OUT_JSON.mkdir(parents=True, exist_ok=True)
    (OUT_JSON / "intent-yaml-manifest.json").write_text(json.dumps(manifest, indent=2))

    intents = {m["catalog_intent"] for m in manifest}
    print(f"groups        : {len(files)}")
    print(f"intents       : {len(intents)}")
    print(f"yamls written : {len(manifest)}  -> {OUT}")
    print(f"auth=none     : {sum(1 for m in manifest if m['auth'] == 'none')}")
    print(f"live verified : {sum(1 for m in manifest if m['live_verified'])}")
    print(f"aliased intent: {len({m['catalog_intent'] for m in manifest if m['canonical_alias_applied']})}")
    print(f"with UI fields: {sum(1 for m in manifest if m['input_fields'])}")
    if problems:
        print(f"\nPROBLEMS ({len(problems)}):")
        for p in problems[:40]:
            print("  -", p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
