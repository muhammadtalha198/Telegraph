#!/usr/bin/env python3
"""
Semantic Register V2 gates — fail-closed before gas.

Order (mandatory — no bypass without ALLOW_UNSAFE_REGISTER=1):
  1) Sample file exists
  2) auto_review_samples.py --gate --file SAMPLE  (hard checks + heuristics + LLM required)
     → must write status=approved; needs_human / rejected = FAIL (no register)
  3) v2_golden_gate.py --sample SAMPLE
     → if candidates/*.json defines this slug, must PASS; else SKIP (still OK)
  4) validate_miner_yaml.py
  5) Live probe of sample request_url — non-empty body
  6) Hosted YAML byte-match is done in register-miner-v2.sh

Manual set_sample_status.py approved alone does NOT unlock gas — step 2 re-runs LLM review.

Does NOT enforce RelTol label_field / milli scale (LLM normalize on Usman side).

  python3 scripts/register_gates_v2.py \\
    --file intentYamls/.../slug.yaml \\
    --sample apiOutputSamples/WEATHER_CURRENT/slug.md
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
UA = "telegraph-register-gates-v2/1"


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = parts[1]
    out: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for line in fm.splitlines():
        if re.match(r"^[a-z_]+:", line) and not line.startswith(" "):
            if key is not None:
                out[key] = "\n".join(buf).strip().strip('"')
            key, _, rest = line.partition(":")
            key = key.strip()
            rest = rest.strip()
            if rest == "|":
                buf = []
            else:
                buf = [rest]
                out[key] = rest.strip('"')
                key = None
                buf = []
        elif key is not None:
            buf.append(line)
    if key is not None:
        out[key] = "\n".join(buf).strip().strip('"')
    return out


def run_cmd(argv: list[str], label: str) -> int:
    print(f"\n----- {label} -----")
    print("+", " ".join(argv))
    p = subprocess.run(argv, cwd=str(ROOT))
    print("PASS" if p.returncode == 0 else "FAIL", label)
    return p.returncode


def live_probe(url: str, timeout: int = 60, *, sample_raw: str = "") -> None:
    print(f"\n----- live probe -----")
    print("+ GET", url[:120] + ("…" if len(url) > 120 else ""))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
    except urllib.error.HTTPError as e:
        # Many public Ethereum JSON-RPC endpoints reject GET (400/405); probe with eth_blockNumber.
        looks_rpc = (
            "/rpc" in url.lower()
            or url.rstrip("/").endswith(".io")
            or '"jsonrpc"' in (sample_raw or "")[:200].lower()
            or "jsonrpc" in (sample_raw or "")[:200].lower()
        )
        if e.code in (400, 405, 415, 422) and looks_rpc:
            print(f"GET → HTTP {e.code}; retrying JSON-RPC POST eth_blockNumber")
            payload = b'{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
            preq = urllib.request.Request(
                url,
                data=payload,
                method="POST",
                headers={
                    "User-Agent": UA,
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
            )
            with urllib.request.urlopen(preq, timeout=timeout) as r:
                body = r.read()
        else:
            raise
    if not body.strip():
        raise RuntimeError("empty response body")
    print(f"PASS  live probe ({len(body)} bytes)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, type=Path, help="miner YAML")
    ap.add_argument("--sample", required=True, type=Path, help="apiOutputSamples/…/*.md")
    ap.add_argument("--skip-live", action="store_true")
    ap.add_argument(
        "--skip-auto-review",
        action="store_true",
        help="UNSAFE — only with ALLOW_UNSAFE_REGISTER=1",
    )
    ap.add_argument(
        "--skip-golden",
        action="store_true",
        help="skip golden suite check (still runs auto_review)",
    )
    a = ap.parse_args()

    ypath = a.file if a.file.is_absolute() else ROOT / a.file
    spath = a.sample if a.sample.is_absolute() else ROOT / a.sample

    print("=== register_gates_v2 (semantic / format-agnostic) ===")

    if not ypath.is_file():
        print(f"FAIL  yaml missing: {ypath}")
        return 1
    if not spath.is_file():
        print(f"FAIL  sample missing: {spath}")
        print("      Capture first: python3 scripts/capture_api_output.py …")
        return 1

    unsafe = os.environ.get("ALLOW_UNSAFE_REGISTER", "").strip() == "1"

    # --- Gate A: auto_review + LLM (mandatory) ---
    if a.skip_auto_review:
        if not unsafe:
            print("FAIL  --skip-auto-review requires ALLOW_UNSAFE_REGISTER=1")
            return 1
        print("WARN  skipping auto_review (ALLOW_UNSAFE_REGISTER=1)")
    else:
        rc = run_cmd(
            [
                sys.executable,
                str(SCRIPTS / "auto_review_samples.py"),
                "--gate",
                "--file",
                str(spath),
                "--min-confidence",
                os.environ.get("AUTO_REVIEW_MIN_CONF", "0.75"),
            ],
            "auto_review+LLM (required)",
        )
        if rc:
            print(
                "FAIL  sample did not get auto_review status=approved "
                "(hard reject / heuristic reject / LLM no|partial / needs_human). "
                "Fix capture or drop — do not register."
            )
            return 1

    meta = parse_front_matter(spath.read_text(encoding="utf-8"))
    status = (meta.get("status") or "").strip()
    print(f"sample  {spath.relative_to(ROOT)}")
    print(f"status  {status!r}  review_source={meta.get('review_source', '')!r}  "
          f"llm_used={meta.get('llm_used', '')!r}  mode={meta.get('review_mode', '')!r}")
    print(f"intent  {meta.get('intent', '')!r}  slug={meta.get('slug', '')!r}")

    if status != "approved":
        print("FAIL  sample status is not approved after auto_review gate")
        return 1

    # Refuse pure-manual approvals unless unsafe (gate should have overwritten, but belt+suspenders)
    src = (meta.get("review_source") or "").strip()
    llm_used = (meta.get("llm_used") or "").strip().lower()
    mode = (meta.get("review_mode") or "").strip()
    if not unsafe:
        if src == "manual":
            print("FAIL  review_source=manual — gas requires auto_review+LLM (re-run will overwrite)")
            return 1
        if llm_used not in ("true", "1", "yes") and "llm" not in mode:
            # Heuristic-only approve is not enough for register
            print(
                "FAIL  sample approved without LLM (llm_used!=true). "
                "Start Ollama or set OMNIROUTE_API_KEY / OPENAI_API_KEY and re-run gates."
            )
            return 1

    # --- Gate B: golden suite when present ---
    if not a.skip_golden:
        rc = run_cmd(
            [sys.executable, str(SCRIPTS / "v2_golden_gate.py"), "--sample", str(spath)],
            "golden suite (PASS required if suite exists; SKIP ok)",
        )
        if rc:
            print("FAIL  golden suite failed for this slug — do not register")
            return 1
    elif not unsafe:
        print("FAIL  --skip-golden requires ALLOW_UNSAFE_REGISTER=1")
        return 1

    if run_cmd(
        [sys.executable, str(SCRIPTS / "validate_miner_yaml.py"), str(ypath)],
        "validate_miner_yaml",
    ):
        return 1

    if not a.skip_live:
        url = (meta.get("request_url") or "").strip()
        if not url.startswith("http"):
            print("FAIL  sample front matter missing request_url")
            return 1
        try:
            sample_text = spath.read_text(encoding="utf-8", errors="replace")
            mraw = re.search(r"```(?:json|text)?\n(.*?)```", sample_text, re.S)
            live_probe(url, sample_raw=(mraw.group(1) if mraw else "")[:500])
        except Exception as e:
            print(f"FAIL  live probe: {e}")
            return 1

    print("\nPASS  all V2 gates (auto_review+LLM + golden-if-any + yaml + live) — safe to registerMiner")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
