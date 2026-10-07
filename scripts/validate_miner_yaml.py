#!/usr/bin/env python3
"""
Miner YAML gate — parse + shape checks BEFORE host/register.

Catches the Group A failure mode (Usman 2026-09-26): unquoted scalars that
contain `: ` (e.g. `description: Pool key: steth, …`) which the node rejects
as `YAML schema validation failed` even when /truth endpoints PASS.

Stdlib only. Optional PyYAML if a real `yaml.safe_load` is importable.

  python3 scripts/validate_miner_yaml.py path/to/miner.yaml
  python3 scripts/validate_miner_yaml.py intentYamls/crypto-yield/
  python3 scripts/validate_miner_yaml.py --self-test

Exit 0 = all PASS. Exit 1 = any FAIL. Wire this into register-miner.sh /
generate-yaml.sh / local_validate_keepers.py so bad YAML never ships again.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

# Unquoted plain scalar with ": " inside → YAML mapping parse error.
# `https://…` is fine (no space after colon). `Pool key: steth` is not.
_KEY_VALUE = re.compile(r"^(\s*)([^:#\n]+?):\s+(.*?)(\s+#.*)?$")
_FLOW_OR_BLOCK = ("|", ">", "[", "{", "&", "*", "!")
_REQUIRED_TOP = ("version", "kind", "slug", "base_url", "endpoints", "semantics", "on_chain")


def _strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


def scan_unquoted_colon_scalars(text: str, path: str = "") -> list[str]:
    """Return human-readable errors for unquoted `: ` in values (Group A)."""
    errs: list[str] = []
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = _KEY_VALUE.match(line)
        if not m:
            continue
        indent, key, val, _cmt = m.groups()
        val = val.rstrip()
        key_s = key.strip()
        # Flow-map fragment lines: `{type: string, description: "…"}`
        if key_s.startswith(("{", "[", "|", ">")):
            continue
        if not val:
            continue
        # Flow / block collections — not plain scalars (avoids false + on
        # `{type: string, description: "..."}` continuation lines).
        stripped = val.lstrip()
        if not stripped:
            continue
        if stripped[0] in ("'", '"') or stripped.startswith(_FLOW_OR_BLOCK) or stripped[0] in "{[":
            continue
        # Catch colon+space in plain scalar (Group A).
        if ": " in val:
            loc = f"{path}:{i}" if path else f"line {i}"
            errs.append(
                f"{loc}: unquoted value contains ': ' — quote it. "
                f"Got `{key_s}: {val[:60]}` "
                f'(Group A / "YAML schema validation failed")'
            )
    return errs


def try_pyyaml_load(text: str) -> tuple[Any | None, str | None]:
    """Load with PyYAML if a real safe_load exists; else (None, None)."""
    try:
        import yaml  # type: ignore
    except Exception:
        return None, None
    safe = getattr(yaml, "safe_load", None)
    if not callable(safe):
        return None, None
    try:
        return safe(text), None
    except Exception as e:
        return None, f"YAML parse error: {e}"


def check_required_shape(text: str, path: str = "") -> list[str]:
    """Lightweight required-field scan (works without PyYAML)."""
    errs: list[str] = []
    loc = path or "yaml"
    lower = text.lower()
    for key in _REQUIRED_TOP:
        # allow `key:` at line start (with indent ok for nested we only need presence)
        if not re.search(rf"(?m)^\s*{re.escape(key)}\s*:", text):
            errs.append(f"{loc}: missing required top-level key `{key}`")
    if re.search(r"(?m)^\s*kind\s*:\s*", text):
        if not re.search(r"(?m)^\s*kind\s*:\s*miner\s*$", text):
            # kind: "miner" or miner
            km = re.search(r"(?m)^\s*kind\s*:\s*[\"']?(\w+)[\"']?\s*$", text)
            if not km or km.group(1) != "miner":
                errs.append(f"{loc}: kind must be `miner`")
    if "label_field" not in lower and "signal_mapping" in lower:
        errs.append(f"{loc}: semantics.signal_mapping.label_field missing")
    elif "label_field" not in lower:
        errs.append(f"{loc}: semantics.signal_mapping.label_field missing")
    if "supported_intents" not in lower:
        errs.append(f"{loc}: supported_intents missing")
    return errs


def check_doc_fields(doc: dict, path: str = "") -> list[str]:
    """Extra checks when a real YAML parse succeeded."""
    errs: list[str] = []
    loc = path or "yaml"
    if doc.get("kind") != "miner":
        errs.append(f"{loc}: kind must be miner (got {doc.get('kind')!r})")
    slug = doc.get("slug")
    if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug or ""):
        errs.append(f"{loc}: slug must match ^[a-z0-9]+(-[a-z0-9]+)*$ (got {slug!r})")
    sem = doc.get("semantics") or {}
    sm = (sem.get("signal_mapping") or {}) if isinstance(sem, dict) else {}
    if not (isinstance(sm, dict) and sm.get("label_field")):
        errs.append(f"{loc}: semantics.signal_mapping.label_field required")
    intents = sem.get("supported_intents") if isinstance(sem, dict) else None
    if not intents:
        # also accept top-level / endpoint intents
        eps = doc.get("endpoints") or []
        has = False
        if isinstance(eps, list):
            for ep in eps:
                if isinstance(ep, dict) and ep.get("intents"):
                    has = True
                    break
        if not has:
            errs.append(f"{loc}: supported_intents (or endpoint intents) required")
    if not doc.get("endpoints"):
        errs.append(f"{loc}: endpoints required")
    if not doc.get("base_url"):
        errs.append(f"{loc}: base_url required")
    return errs


def validate_text(text: str, path: str = "") -> list[str]:
    errs = scan_unquoted_colon_scalars(text, path)
    # Always run shape scan — catches missing label_field even if parse works.
    errs.extend(check_required_shape(text, path))
    doc, perr = try_pyyaml_load(text)
    if perr:
        errs.append(f"{path or 'yaml'}: {perr}")
    elif isinstance(doc, dict):
        # Prefer structured checks; drop redundant shape dupes by re-running structured only
        # Keep shape errs; add structured
        errs.extend(check_doc_fields(doc, path))
    return errs


def validate_file(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        return [f"{path}: read error: {e}"]
    return validate_text(text, str(path))


def iter_yaml_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(p for p in target.rglob("*.yaml") if p.is_file())


def self_test() -> int:
    bad = 'description: Pool key: steth, reth\n'
    good = 'description: "Pool key: steth, reth"\n'
    be = scan_unquoted_colon_scalars(bad, "bad.yaml")
    ge = scan_unquoted_colon_scalars(good, "good.yaml")
    ok = bool(be) and not ge
    # URL must not false-positive
    url = "documentation: https://docs.lido.fi/integrations/api/\n"
    ue = scan_unquoted_colon_scalars(url, "url.yaml")
    ok = ok and not ue
    print("self-test unquoted colon:", "PASS" if be else "FAIL", be[:1])
    print("self-test quoted:", "PASS" if not ge else "FAIL", ge)
    print("self-test url:", "PASS" if not ue else "FAIL", ue)
    # full miner stub
    stub = """version: "1"
kind: miner
id: 1
slug: yld-test
protocol: generic
name: Test
description: ok
base_url: https://example.com
auth:
  type: none
endpoints:
  - path: /query
    method: GET
    intents: [CRYPTO_YIELD_RATE]
semantics:
  signal_mapping:
    label_field: apy_bps
  supported_intents:
    - CRYPTO_YIELD_RATE
on_chain:
  transform: direct
  min_price_usdc: 0.01
"""
    se = validate_text(stub, "stub.yaml")
    # may still warn if pyyaml missing on shape-only — filter to real fails
    print("self-test stub errs:", se)
    stub_ok = not any("unquoted" in e for e in se) and not any("label_field missing" in e for e in se)
    ok = ok and stub_ok
    print("SELF-TEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate miner YAML before register")
    ap.add_argument("paths", nargs="*", type=Path, help="file(s) or directories")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.paths:
        ap.error("pass YAML path(s) or --self-test")

    n_fail = 0
    n_ok = 0
    for target in args.paths:
        if not target.exists():
            print(f"FAIL  {target}: not found")
            n_fail += 1
            continue
        for f in iter_yaml_files(target):
            errs = validate_file(f)
            # Dedupe while preserving order
            seen: set[str] = set()
            uniq = []
            for e in errs:
                if e not in seen:
                    seen.add(e)
                    uniq.append(e)
            if uniq:
                n_fail += 1
                print(f"FAIL  {f}")
                for e in uniq:
                    print(f"      {e}")
            else:
                n_ok += 1
                print(f"PASS  {f}")
    print(f"\n{n_ok} PASS, {n_fail} FAIL")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
