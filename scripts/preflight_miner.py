#!/usr/bin/env python3
"""
Preflight gate — catch Usman Groups A–D BEFORE registerMiner.

Runs AFTER validate_miner_yaml.py. Stdlib only.

  Group A  YAML already parseable (caller runs validate_miner_yaml first;
           we re-check unquoted `: ` and required shape).
  Group B  Live endpoint must return HTTP 200 JSON (no 404 / DNS / 502).
  Group C  Declared label_field must resolve to a usable live value
           (e.g. vessel SOG present, not "no recent position").
  Group D  label_field must be a NUMBER Usman's toNumber can score —
           not a list / object / advisory id string. Intent field + range
           must match miner_selftest. VULNERABILITY_TRIAGE must go through
           omni-chat /truth/*-cvss with a pinned cve_id.

Usage:
  python3 scripts/preflight_miner.py --file intentYamls/.../slug.yaml
  python3 scripts/preflight_miner.py --file ... --skip-live   # static only
  python3 scripts/preflight_miner.py --regression            # yesterday's fixes

Exit 0 = PASS. Exit 1 = FAIL. Wired into register-miner.sh.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_miner_yaml import validate_file, try_pyyaml_load  # noqa: E402
from miner_selftest import INTENTS, as_num, dig  # noqa: E402

UA = "telegraph-preflight/1"
PROXY_HOST = "omni-chat.13.237.89.59.sslip.io"


def _rx(text: str, pattern: str) -> str | None:
    m = re.search(pattern, text, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def parse_miner_doc(text: str) -> dict[str, Any]:
    """
    Minimal miner-YAML extractor (stdlib). Prefer real PyYAML when available;
    otherwise regex-parse the fields preflight needs.
    """
    doc, _perr = try_pyyaml_load(text)
    if isinstance(doc, dict) and doc.get("base_url") and doc.get("semantics"):
        return doc

    base = _rx(text, r"(?m)^base_url:\s*(\S+)")
    slug = _rx(text, r"(?m)^slug:\s*(\S+)")
    field = _rx(text, r"(?m)^\s*label_field:\s*(\S+)")
    path = _rx(text, r"(?m)^\s*external_path:\s*(\S+)")
    intents: list[str] = []
    # supported_intents: - NAME   or intents: [NAME]
    for m in re.finditer(r"(?m)^\s*-\s*([A-Z][A-Z0-9_]+)\s*$", text):
        intents.append(m.group(1))
    for m in re.finditer(r"intents:\s*\[([^\]]+)\]", text):
        for part in m.group(1).split(","):
            p = part.strip().strip("\"'")
            if p:
                intents.append(p)
    # defaults: `name: {type: string, description: "…", default: "X"}`
    defaults: dict[str, str] = {}
    for m in re.finditer(
        r"([A-Za-z0-9_]+):\s*\{[^}\n]*default:\s*[\"']([^\"']+)[\"'][^}\n]*\}",
        text,
    ):
        defaults[m.group(1)] = m.group(2)

    return {
        "slug": slug,
        "base_url": base,
        "endpoints": [
            {
                "external_path": path or "/query",
                "intents": intents[:1] or None,
            }
        ],
        "input_schema": {
            "properties": {k: {"default": v} for k, v in defaults.items()},
        },
        "semantics": {
            "signal_mapping": {"label_field": field.strip("\"'") if field else None},
            "supported_intents": intents or None,
        },
    }

# Intent → accepted label_field names (first is canonical in miner_selftest).
FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "VULNERABILITY_TRIAGE": ("cvss_base_score_milli", "cvss_base_score"),
    "CRYPTO_YIELD_RATE": ("apy_bps",),
    "EVENT_OUTCOME_RESOLUTION": ("resolved_yes",),
    "VESSEL_TELEMETRY_VERIFY": ("sog_milliknots",),
    "LANGUAGE_TRANSLATION": ("translated_text",),
    "TEXT_SUMMARIZATION": ("summary_text",),
    "CHATBOT_CONVERSATION": ("reply_text",),
    "TEXT_TO_SPEECH": ("audio_b64",),
}

# NON-DETERMINISTIC / adapter intents: label is text (LLM-judge), not toNumber.
TEXT_INTENTS = frozenset({
    "LANGUAGE_TRANSLATION",
    "TEXT_SUMMARIZATION",
    "CHATBOT_CONVERSATION",
    "TEXT_TO_SPEECH",
    "CODE_REVIEW",
    "LLM_OUTPUT_EVALUATION",
})

# VULN must not hit public APIs direct (Group D second problem).
VULN_DIRECT_HOSTS = (
    "api.github.com",
    "services.nvd.nist.gov",
    "api.osv.dev",
    "cve.circl.lu",
    "cveawg.mitre.org",
)
VULN_OK_PATHS = (
    "/truth/nvd-cvss",
    "/truth/circl-cvss",
    "/truth/osv-cvss",
    "/truth/ghsa-cvss",
    "/truth/redhat-cvss",
    "/truth/cveorg-cvss",
)

# Slugs fixed 2026-09-28 — regression must stay green.
# NON-DET campaign 2026-09-29 appended (adapter text askability).
REGRESSION_SLUGS = (
    "yld-lido",
    "yld-defillama",
    "yld-rocketpool",
    "yld-frax",
    "yld-stader",
    "yld-aave",
    "yld-compound",
    "event-kalshi-result",
    "ves-digitraffic",
    "vuln-circl-browse",
    "vuln-circl-last",
    "vuln-ghsa-npm",
    "vuln-ghsa-pip",
    "vuln-ghsa-severity",
    "vuln-nvd",
    "vuln-nvd-keyword",
    "vuln-osv-id",
    "vuln-osv-log4j",
    # NON-DET
    "tr-mymemory",
    "tr-google",
    "tr-hf-opus",
    "tr-pollinations",
    "sum-hf-bart",
    "sum-hf-pegasus",
    "sum-hf-distilbart",
    "sum-pollinations",
    "chat-pollinations",
    "chat-aihorde",
    "chat-nova",
    "tts-google",
    "tts-espeak",
)


def fail(msg: str) -> None:
    print(f"FAIL  {msg}")


def ok(msg: str) -> None:
    print(f"PASS  {msg}")


def load_doc(path: Path) -> tuple[str, dict[str, Any] | None, list[str]]:
    text = path.read_text(encoding="utf-8")
    errs = validate_file(path)
    try:
        doc = parse_miner_doc(text)
    except Exception as e:
        errs.append(f"parse_miner_doc: {e}")
        return text, None, errs
    if not doc.get("base_url") or not label_field(doc):
        errs.append("could not extract base_url / label_field from YAML")
        return text, None, errs
    return text, doc, errs


def first_intent(doc: dict) -> str | None:
    sem = doc.get("semantics") or {}
    intents = sem.get("supported_intents") if isinstance(sem, dict) else None
    if isinstance(intents, list):
        for i in intents:
            s = str(i)
            if s.isupper() and "_" in s:
                return s
            if s.isupper() and s not in ("*",):
                return s
    for ep in doc.get("endpoints") or []:
        if isinstance(ep, dict) and ep.get("intents"):
            for i in ep["intents"]:
                s = str(i)
                if s != "*" and s.isupper():
                    return s
    return None


def label_field(doc: dict) -> str | None:
    sem = doc.get("semantics") or {}
    sm = sem.get("signal_mapping") if isinstance(sem, dict) else None
    if isinstance(sm, dict) and sm.get("label_field") is not None:
        return str(sm["label_field"])
    return None


def default_params(doc: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    schema = doc.get("input_schema") or {}
    props = schema.get("properties") if isinstance(schema, dict) else None
    if isinstance(props, dict):
        for k, v in props.items():
            if isinstance(v, dict) and "default" in v and v["default"] is not None:
                out[str(k)] = str(v["default"])
    return out


def endpoint_bits(doc: dict) -> tuple[str | None, str | None]:
    """Return (base_url, external_path) from first endpoint."""
    base = doc.get("base_url")
    if not isinstance(base, str):
        return None, None
    eps = doc.get("endpoints") or []
    if not eps or not isinstance(eps[0], dict):
        return base.rstrip("/"), None
    ep = eps[0]
    path = ep.get("external_path") or ep.get("path") or ""
    return base.rstrip("/"), str(path)


def build_url(base: str, path: str, params: dict[str, str]) -> str:
    # Substitute {name} path params from defaults.
    def repl(m: re.Match[str]) -> str:
        key = m.group(1)
        if key not in params:
            raise KeyError(f"path param {{{key}}} missing default in input_schema")
        return urllib.parse.quote(params[key], safe="")

    filled = re.sub(r"\{([A-Za-z0-9_]+)\}", repl, path)
    # Remaining params as query (skip those already used in path).
    used = set(re.findall(r"\{([A-Za-z0-9_]+)\}", path))
    q = {k: v for k, v in params.items() if k not in used}
    url = base + (filled if filled.startswith("/") else "/" + filled)
    if q:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(q)
    return url


def http_json(url: str, timeout: int = 90) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def static_intent_rules(doc: dict, intent: str, field: str) -> list[str]:
    """Group D (+ related) static rules — no network."""
    errs: list[str] = []
    base, path = endpoint_bits(doc)
    base = base or ""
    path = path or ""
    aliases = FIELD_ALIASES.get(intent)
    if aliases and field not in aliases:
        # Also allow exact selftest canonical when listed in INTENTS
        canon = INTENTS.get(intent, (None,))[0]
        if field != canon:
            errs.append(
                f"Group D / WRONG_QUANTITY: label_field={field!r} not in "
                f"accepted {aliases} for {intent}"
            )

    if intent == "VULNERABILITY_TRIAGE":
        host = urllib.parse.urlparse(base).hostname or ""
        if any(h in host for h in VULN_DIRECT_HOSTS) or any(
            h in base for h in VULN_DIRECT_HOSTS
        ):
            errs.append(
                f"Group D: base_url hits upstream {host or base!r} directly — "
                f"must use omni-chat proxy /truth/*-cvss"
            )
        if PROXY_HOST not in base and "omni-chat" not in base:
            errs.append(
                f"Group D: base_url must be omni-chat proxy (got {base!r})"
            )
        path_ok = any(path == p or path.startswith(p) for p in VULN_OK_PATHS)
        if not path_ok:
            errs.append(
                f"Group D: external_path must be one of {VULN_OK_PATHS} (got {path!r})"
            )
        params = default_params(doc)
        if "cve_id" not in params:
            errs.append("Group D: input_schema must default-pin cve_id (shared question)")
        if field in ("0", "id", "vulnerabilities"):
            errs.append(
                f"Group D: label_field={field!r} is list/id — need cvss_base_score"
            )

    if intent == "CRYPTO_YIELD_RATE" and field != "apy_bps":
        errs.append(f"CRYPTO_YIELD_RATE label_field must be apy_bps (got {field!r})")

    if intent == "EVENT_OUTCOME_RESOLUTION" and field != "resolved_yes":
        errs.append(
            f"EVENT_OUTCOME_RESOLUTION label_field must be resolved_yes (got {field!r})"
        )

    if intent == "VESSEL_TELEMETRY_VERIFY" and field != "sog_milliknots":
        errs.append(
            f"VESSEL_TELEMETRY_VERIFY label_field must be sog_milliknots (got {field!r})"
        )

    return errs


def live_probe(doc: dict, intent: str, field: str) -> list[str]:
    """Group B/C/D live: askable + numeric (or non-empty text for adapter intents)."""
    errs: list[str] = []
    base, path = endpoint_bits(doc)
    if not base or not path:
        return ["missing base_url or external_path"]
    params = default_params(doc)
    try:
        url = build_url(base, path, params)
    except KeyError as e:
        return [f"NOT_ASKABLE: {e}"]

    print(f"  probe {url}")
    try:
        doc_json = http_json(url)
    except urllib.error.HTTPError as e:
        return [f"Group B NOT_ASKABLE: HTTP {e.code} for {url}"]
    except Exception as e:
        return [f"Group B NOT_ASKABLE: {type(e).__name__}: {e}"]

    if isinstance(doc_json, dict) and doc_json.get("error"):
        return [f"Group C/B NOT_ASKABLE: upstream error {doc_json.get('error')!r}"]

    raw = dig(doc_json, field)
    if raw is None:
        keys = list(doc_json)[:12] if isinstance(doc_json, dict) else type(doc_json).__name__
        return [
            f"Group D WRONG_QUANTITY: field {field!r} absent. Top-level: {keys}"
        ]

    # Adapter / NON-DET: string answer is the scored artifact (LLM-judge).
    if intent in TEXT_INTENTS:
        if isinstance(raw, (dict, list)):
            return [
                f"WRONG_QUANTITY: {field!r} is {type(raw).__name__} — need plain translated/generated text"
            ]
        s = str(raw).strip()
        if len(s) < 1:
            return [f"NOT_ASKABLE: {field!r} empty: {raw!r}"]
        print(f"  value {field}={s[:120]!r}")
        return errs

    # Explicit non-numeric shapes Usman listed (comparator / toNumber path)
    if isinstance(raw, (dict, list)):
        return [
            f"Group D WRONG_QUANTITY: field {field!r} is {type(raw).__name__} — "
            f"toNumber rejects maps/lists"
        ]
    if isinstance(raw, str) and as_num(raw) is None:
        return [
            f"Group D WRONG_QUANTITY: field {field!r}={raw!r} is not a number "
            f"(OSV id-string class failure)"
        ]

    val = as_num(raw)
    if val is None:
        return [f"Group D WRONG_QUANTITY: field {field!r} not numeric: {raw!r}"]

    # Range / selftest row when known
    if intent in INTENTS:
        _f, _note, tol, lo, hi = INTENTS[intent]
        check_val = val
        if intent == "VULNERABILITY_TRIAGE" and field == "cvss_base_score":
            if not (0 <= float(val) <= 10.0):
                return [
                    f"WRONG_QUANTITY: cvss_base_score {val} outside 0–10 "
                    f"(intent scores CVSS base)"
                ]
            check_val = float(val) * 1000.0
        if not (lo <= abs(check_val) <= hi):
            if not (tol <= 0 and val in (0, 0.0, 1, 1.0)):
                errs.append(
                    f"WRONG_QUANTITY: {val} outside plausible range "
                    f"[{lo:g},{hi:g}] for {intent} (scale/field mismatch?)"
                )

    print(f"  value {field}={val}")
    return errs


def preflight_file(path: Path, skip_live: bool = False) -> int:
    print(f"=== preflight {path} ===")
    _text, doc, yaml_errs = load_doc(path)
    if yaml_errs:
        for e in yaml_errs:
            fail(f"Group A YAML: {e}")
        return 1
    ok("YAML gate (Group A)")

    assert doc is not None
    intent = first_intent(doc)
    field = label_field(doc)
    if not intent:
        fail("no supported_intents / endpoint intents")
        return 1
    if not field:
        fail("semantics.signal_mapping.label_field missing")
        return 1
    print(f"  intent={intent}  label_field={field}")

    static_errs = static_intent_rules(doc, intent, field)
    if static_errs:
        for e in static_errs:
            fail(e)
        return 1
    ok("static intent rules (Group D shape)")

    if skip_live:
        ok("live probe skipped (--skip-live)")
        return 0

    live_errs = live_probe(doc, intent, field)
    if live_errs:
        for e in live_errs:
            fail(e)
        return 1
    ok("live askable + numeric quantity (Groups B/C/D)")
    print(f"PASS  {path.name} ready to register")
    return 0


def find_slug_yaml(slug: str) -> Path | None:
    matches = sorted((ROOT / "intentYamls").rglob(f"{slug}.yaml"))
    return matches[0] if matches else None


def regression() -> int:
    print("=== regression: 2026-09-28 Groups A–D fixes ===\n")
    n_fail = 0
    for slug in REGRESSION_SLUGS:
        p = find_slug_yaml(slug)
        if not p:
            fail(f"regression: missing YAML for {slug}")
            n_fail += 1
            continue
        rc = preflight_file(p, skip_live=False)
        if rc != 0:
            n_fail += 1
        print()
    print(f"REGRESSION {len(REGRESSION_SLUGS) - n_fail}/{len(REGRESSION_SLUGS)} PASS")
    return 1 if n_fail else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Preflight miner YAML + live quantity gate")
    ap.add_argument("--file", type=Path, help="miner YAML to check")
    ap.add_argument("--skip-live", action="store_true", help="static rules only")
    ap.add_argument(
        "--regression",
        action="store_true",
        help="re-check all 2026-09-28 fixed slugs (Groups A–D)",
    )
    args = ap.parse_args()
    if args.regression:
        return regression()
    if not args.file:
        ap.error("pass --file YAML or --regression")
    if not args.file.is_file():
        fail(f"not a file: {args.file}")
        return 1
    return preflight_file(args.file, skip_live=args.skip_live)


if __name__ == "__main__":
    sys.exit(main())
