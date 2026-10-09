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
  5) pin_consistency_check.py --file (shared pin, distinct publisher, unique slug)
  6) Sample asks the SAME question as the YAML (sample request_url == the node's request)
  7) minercheck gate: the miner's live answer, called as the node calls it, passes
     E1/E5/E2/E4 and agrees with independent sources (intents/<INTENT>.yaml);
     SKIP if the intent has no spec yet
  8) Live probe of the YAML request — content family matches the sample
  9) Hosted YAML byte-match is done in register-miner-v2.sh

Manual set_sample_status.py approved alone does NOT unlock gas — step 2 re-runs LLM review.

Does NOT enforce RelTol label_field / milli scale (LLM normalize on Usman side).

  python3 scripts/register_gates_v2.py \\
    --file intentYamls/.../slug.yaml \\
    --sample apiOutputSamples/WEATHER_CURRENT/slug.md
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
UA = "telegraph-register-gates-v2/1"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(ROOT))
from sample_file import parse_front_matter, raw_body  # noqa: E402


def run_cmd(argv: list[str], label: str) -> int:
    print(f"\n----- {label} -----")
    print("+", " ".join(argv))
    p = subprocess.run(argv, cwd=str(ROOT))
    print("PASS" if p.returncode == 0 else "FAIL", label)
    return p.returncode


class _NoCrossHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow same-host redirects only. A cross-host 302 (e.g. an RPC host bouncing a GET
    to its marketing site) is NOT the API answering — it used to pass as 'non-empty body'."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        from urllib.parse import urlparse
        if urlparse(newurl).hostname != urlparse(req.full_url).hostname:
            raise urllib.error.HTTPError(req.full_url, code,
                                         f"cross-host redirect to {newurl}", headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_NoCrossHostRedirect)


def yaml_request(ypath: Path) -> tuple[str, str]:
    """(method, url) exactly as the node will call it: {placeholder} path params are filled
    from the defaults and dropped from the query (Telegraph generic.go); the rest become
    query params. Before 2026-10-08 this left '{address}' literally in the path."""
    import yaml  # validate_miner_yaml already requires PyYAML
    from minercheck.gate import node_request
    try:
        return node_request(yaml.safe_load(ypath.read_text(encoding="utf-8")) or {})
    except Exception as e:  # MinerCheckError / YAML error -> gate failure with the reason
        raise RuntimeError(str(e)) from e


def same_question(sample_url: str, node_url: str) -> bool:
    """Same host, path (trailing '/' ignored) and non-blank query parameters (any order)."""
    from urllib.parse import parse_qsl, unquote, urlparse
    a, b = urlparse(sample_url.strip()), urlparse(node_url.strip())
    path = lambda u: unquote(u.path).rstrip("/") or "/"  # noqa: E731
    query = lambda u: sorted(parse_qsl(u.query))  # blank values dropped, as the node drops empty defaults  # noqa: E731
    return (a.scheme, a.hostname, path(a), query(a)) == (b.scheme, b.hostname, path(b), query(b))


def _family(ctype: str, body: bytes) -> str:
    """Body decides (headers lie); binary media types are trusted."""
    from minercheck.reader import detect_format
    c = (ctype or "").lower()
    if c.startswith(("audio/", "image/", "application/octet")):
        return "binary"
    fmt = detect_format(body.decode("utf-8", "replace") if body else "", c)
    return fmt if fmt in ("json", "html", "binary") else "text"


def live_probe(ypath: Path, *, sample_ctype: str = "", sample_raw: str = "", timeout: int = 60) -> None:
    """Call the miner exactly as its YAML declares (no POST rescue, no cross-host redirects)
    and require the same content family as the approved sample."""
    print("\n----- live probe (as the node will call it) -----")
    method, url = yaml_request(ypath)
    print(f"+ {method}", url[:160] + ("…" if len(url) > 160 else ""))
    if method != "GET":
        # YAML POST bodies are built per-request by the node from on_chain.request fields;
        # we cannot reproduce that faithfully here, so do not pretend to.
        raise RuntimeError(f"YAML declares {method}; live probe only verifies GET miners — needs manual review")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with _OPENER.open(req, timeout=timeout) as r:  # HTTPError (incl. 4xx/5xx/cross-host) -> FAIL
        body, ctype = r.read(), r.headers.get("Content-Type", "")
    if not body.strip():
        raise RuntimeError("empty response body")
    got = _family(ctype, body)
    want = _family(sample_ctype, (sample_raw or "").encode())
    if got == "html" and want != "html":
        raise RuntimeError("YAML request returned an HTML page, not the API answer the sample shows")
    if want in ("json", "html") and got != want:
        raise RuntimeError(f"YAML request returned {got}, but the approved sample is {want} — "
                           "sample was not captured the way the node calls this miner")
    print(f"PASS  live probe ({len(body)} bytes, {got})")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, type=Path, help="miner YAML")
    ap.add_argument("--sample", required=True, type=Path, help="apiOutputSamples/…/*.md")
    ap.add_argument("--skip-live", action="store_true", help="UNSAFE — only with ALLOW_UNSAFE_REGISTER=1")
    ap.add_argument("--skip-verify", action="store_true",
                    help="skip minercheck answer verification — only with ALLOW_UNSAFE_REGISTER=1")
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
    for flag, on in (("--skip-live", a.skip_live), ("--skip-verify", a.skip_verify)):
        if on and not unsafe:
            print(f"FAIL  {flag} requires ALLOW_UNSAFE_REGISTER=1")
            return 1

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

    if run_cmd(
        [sys.executable, str(SCRIPTS / "pin_consistency_check.py"), "--file", str(ypath)],
        "shared pin (shared_pins.json — same question as the intent's rank set)",
    ):
        return 1

    # --- Gate C: the approved sample must be THIS miner's question ---
    print("\n----- sample question == YAML question -----")
    try:
        _m, node_url = yaml_request(ypath)
    except RuntimeError as e:
        print(f"FAIL  cannot build the node request from the YAML: {e}")
        return 1
    sample_url = str(meta.get("request_url") or "")
    if not same_question(sample_url, node_url):
        print(f"FAIL  approved sample asked a different question than the YAML will:\n"
              f"      sample: {sample_url}\n      yaml:   {node_url}\n"
              "      Re-capture the sample with the YAML's request, or fix the YAML defaults.")
        return 1
    print("PASS  sample request == node request")

    # --- Gate D: deterministic answer verification (intents/<INTENT>.yaml) ---
    if a.skip_verify:
        print("WARN  skipping minercheck verify (ALLOW_UNSAFE_REGISTER=1)")
    else:
        from v2_intent_folders import canonical_intent
        intent = canonical_intent(meta.get("intent") or spath.parent.name)
        if run_cmd([sys.executable, "-m", "minercheck", "gate", "--file", str(ypath), "--intent", intent],
                   "minercheck: miner answer verified against independent sources (SKIP if no spec)"):
            print("FAIL  miner answer is not verified — do not register")
            return 1

    if not a.skip_live:
        try:
            sample_text = spath.read_text(encoding="utf-8", errors="replace")
            live_probe(ypath, sample_ctype=str(meta.get("content_type") or ""),
                       sample_raw=raw_body(sample_text)[:500])
        except Exception as e:
            print(f"FAIL  live probe: {e}")
            return 1

    print("\nPASS  all V2 gates (auto_review+LLM + golden-if-any + yaml + pin + question + verify + live)"
          " — safe to registerMiner")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)  # keep our lines in order with the gate subprocesses' output
    raise SystemExit(main())
