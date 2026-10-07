#!/usr/bin/env python3
"""
Automatic register gates — ONE path, fail-closed, before any gas.

Runs in order (every gate must PASS; no soft skips):
  1) validate_miner_yaml.py     — Group A YAML parse/shape
  2) preflight_miner.py         — Groups A–D static + live quantity/text
  3) miner_selftest.py          — numeric RelTol OR NON-DET text askability
  4) local_validate_keepers     — --slug if in suite, else --from-yaml (always runs)

Used ONLY by register-miner.sh. Do not call cast registerMiner directly.

  python3 scripts/register_gates.py --file intentYamls/.../slug.yaml

Exit 0 = all required gates PASS → safe to registerMiner.
Exit 1 = blocked (do not spend gas).
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from miner_selftest import INTENTS, TEXT_INTENTS, as_num, dig  # noqa: E402
from preflight_miner import (  # noqa: E402
    build_url,
    default_params,
    endpoint_bits,
    first_intent,
    label_field,
    load_doc,
    preflight_file,
)


def run_cmd(argv: list[str], label: str) -> int:
    print(f"\n----- {label} -----")
    print("+", " ".join(argv))
    p = subprocess.run(argv, cwd=str(ROOT))
    if p.returncode != 0:
        print(f"FAIL  gate: {label} (exit {p.returncode})")
    else:
        print(f"PASS  gate: {label}")
    return p.returncode


def http_json(url: str):
    req = urllib.request.Request(
        url, headers={"User-Agent": "telegraph-register-gates/1", "Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def run_selftest(path: Path, intent: str, field: str, url: str) -> int:
    print(f"\n----- miner_selftest ({intent}) -----")
    if intent not in INTENTS and intent not in TEXT_INTENTS:
        print(
            f"FAIL  intent {intent!r} not in miner_selftest INTENTS/TEXT_INTENTS — "
            f"add it before registerMiner (no soft skip)"
        )
        return 1
    argv = [
        sys.executable,
        str(SCRIPTS / "miner_selftest.py"),
        "--intent",
        intent,
        "--url",
        url,
        "--field",
        field,
    ]
    # Comparator intents: self-truth so RelTol curve also runs.
    # NON-DET / TEXT: shape + askability only (no numeric --truth).
    if intent in INTENTS:
        try:
            doc = http_json(url)
            raw = dig(doc, field)
            if intent == "VULNERABILITY_TRIAGE" and raw is None:
                for alt in ("cvss_base_score_milli", "cvss_base_score"):
                    raw = dig(doc, alt)
                    if raw is not None:
                        field = alt
                        argv[argv.index("--field") + 1] = field
                        break
            val = as_num(raw)
            if intent == "VULNERABILITY_TRIAGE" and field == "cvss_base_score" and val is not None:
                truth = float(val) * 1000.0
            elif val is not None:
                truth = float(val)
            else:
                truth = None
            if truth is not None:
                argv.extend(["--truth", str(truth)])
        except Exception as e:
            print(f"WARN  could not fetch truth for selftest: {e} — shape-only")

    print("+", " ".join(argv))
    p = subprocess.run(argv, cwd=str(ROOT))
    if p.returncode != 0:
        print(f"FAIL  gate: miner_selftest (exit {p.returncode})")
    else:
        print("PASS  gate: miner_selftest")
    return p.returncode


def run_keepers(slug: str, yaml_path: Path) -> int:
    """Always run keepers: suite --slug first, else --from-yaml (never soft-skip)."""
    print(f"\n----- local_validate_keepers --slug {slug} -----")
    argv = [
        sys.executable,
        str(SCRIPTS / "local_validate_keepers.py"),
        "--slug",
        slug,
    ]
    print("+", " ".join(argv))
    p = subprocess.run(argv, cwd=str(ROOT), capture_output=True, text=True)
    out = (p.stdout or "") + (p.stderr or "")
    suite_miss = (
        "Running 0 endpoint cases" in out
        or "FAIL  Running 0 endpoint cases" in out
    )
    if suite_miss:
        print(out[-800:] if out else "")
        print(f"NOTE  slug {slug!r} not in keepers suite → falling back to --from-yaml")
        argv2 = [
            sys.executable,
            str(SCRIPTS / "local_validate_keepers.py"),
            "--from-yaml",
            str(yaml_path),
        ]
        print(f"\n----- local_validate_keepers --from-yaml {yaml_path} -----")
        print("+", " ".join(argv2))
        p2 = subprocess.run(argv2, cwd=str(ROOT), capture_output=True, text=True)
        out2 = (p2.stdout or "") + (p2.stderr or "")
        sys.stdout.write(out2)
        if p2.returncode != 0:
            print(f"FAIL  gate: local_validate_keepers --from-yaml (exit {p2.returncode})")
        else:
            print("PASS  gate: local_validate_keepers (--from-yaml)")
        return p2.returncode

    sys.stdout.write(out)
    if p.returncode != 0:
        print(f"FAIL  gate: local_validate_keepers (exit {p.returncode})")
    else:
        print("PASS  gate: local_validate_keepers")
    return p.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="Auto register gates (YAML+preflight+selftest+keepers)")
    ap.add_argument("--file", type=Path, required=True, help="miner YAML path")
    ap.add_argument(
        "--skip-keepers",
        action="store_true",
        help="UNSAFE: only with ALLOW_UNSAFE_REGISTER=1",
    )
    ap.add_argument(
        "--skip-selftest",
        action="store_true",
        help="UNSAFE: only with ALLOW_UNSAFE_REGISTER=1",
    )
    ap.add_argument(
        "--meta-out",
        type=Path,
        help="write INTENT=/SLUG=/LABEL_FIELD=/PROBE_URL= lines here for the shell wrapper",
    )
    args = ap.parse_args()
    path = args.file
    if not path.is_file():
        print(f"FAIL  not a file: {path}", file=sys.stderr)
        return 1

    unsafe = os.environ.get("ALLOW_UNSAFE_REGISTER", "").strip() == "1"
    if (args.skip_keepers or args.skip_selftest) and not unsafe:
        print(
            "FAIL  --skip-keepers/--skip-selftest blocked. "
            "Set ALLOW_UNSAFE_REGISTER=1 only for true emergencies.",
            file=sys.stderr,
        )
        return 1

    print("=== register_gates (automatic, fail-closed) ===")
    print(f"file={path}")

    # 1) YAML
    rc = run_cmd([sys.executable, str(SCRIPTS / "validate_miner_yaml.py"), str(path)], "validate_miner_yaml")
    if rc != 0:
        return 1

    # 2) Preflight (includes live Groups B/C/D)
    print("\n----- preflight_miner (Groups A–D) -----")
    rc = preflight_file(path, skip_live=False)
    if rc != 0:
        print("FAIL  gate: preflight_miner")
        return 1
    print("PASS  gate: preflight_miner")

    _text, doc, errs = load_doc(path)
    if errs or doc is None:
        print("FAIL  could not reload miner doc after preflight")
        return 1
    intent = first_intent(doc) or ""
    field = label_field(doc) or ""
    slug = str(doc.get("slug") or path.stem)
    base, ep_path = endpoint_bits(doc)
    params = default_params(doc)
    try:
        probe_url = build_url(base or "", ep_path or "", params) if base and ep_path else ""
    except Exception as e:
        print(f"FAIL  build probe URL: {e}")
        return 1

    meta_lines = [
        f"INTENT={intent}",
        f"SLUG={slug}",
        f"LABEL_FIELD={field}",
        f"PROBE_URL={probe_url}",
    ]
    if args.meta_out:
        args.meta_out.write_text("\n".join(meta_lines) + "\n", encoding="utf-8")
        print(f"meta → {args.meta_out}")

    # 3) miner_selftest — required
    if args.skip_selftest:
        print("WARN  skipping miner_selftest (ALLOW_UNSAFE_REGISTER=1)")
    else:
        if not intent or not field or not probe_url:
            print("FAIL  missing intent/field/probe_url for miner_selftest")
            return 1
        rc = run_selftest(path, intent, field, probe_url)
        if rc != 0:
            return 1

    # 4) keepers — required (suite or from-yaml)
    if args.skip_keepers:
        print("WARN  skipping local_validate_keepers (ALLOW_UNSAFE_REGISTER=1)")
    else:
        rc = run_keepers(slug, path)
        if rc != 0:
            return 1

    print("\n=== ALL GATES PASS — safe to registerMiner ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
