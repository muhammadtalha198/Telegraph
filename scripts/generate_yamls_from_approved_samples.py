#!/usr/bin/env python3
"""
Generate intentYamls/*.yaml from APPROVED apiOutputSamples (Semantic Register V2).

Creation pipeline (baked in — do not skip):
  1) sample status must be approved by auto_review+LLM (review_source=auto_review, llm_used=true)
  2) parse request_url → base_url + external_path + pins (defaults from capture)
  3) write YAML under intentYamls/<folder>/<slug>.yaml
  4) validate_miner_yaml.py (Group A colon/quote + shape)

Does NOT register or host. Next:
  host YAML → ./scripts/register-miner-v2.sh --file … --url … --sample …

Usage (from MinerCreator/):
  python3 scripts/generate_yamls_from_approved_samples.py
  python3 scripts/generate_yamls_from_approved_samples.py --intent ONCHAIN_METRIC_VERIFY
  python3 scripts/generate_yamls_from_approved_samples.py --force   # overwrite existing
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "apiOutputSamples"
OUT_YAMLS = ROOT / "intentYamls"
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from sample_file import parse_sample as _parse_sample_file  # noqa: E402
from v2_intent_folders import canonical_intent, intent_folder  # noqa: E402


def intent_dir(intent: str) -> str | None:
    return intent_folder(intent) or intent_folder(canonical_intent(intent))

# V2: format-agnostic — label_field is a soft hint; Usman LLM normalizes.
LABEL = {
    "LIQUIDITY_DEPTH_VERIFY": "data",
    "ONCHAIN_METRIC_VERIFY": "coin_balance",
    "EVENT_OUTCOME_RESOLUTION": "events",
    "SECURITY_REVIEW": "vulnerabilities",
    "VULNERABILITY_TRIAGE": "cvss",
    "CODE_PATCH_VERIFY": "conclusion",
    "OPTIMAL_EXECUTION_ROUTE": "estimate",
    "CROSS_CHAIN_STATE_VERIFY": "status",
}

ADDR_RE = re.compile(r"0x[a-fA-F0-9]{40}")
CVE_RE = re.compile(r"CVE-\d{4}-\d+", re.I)
GHSA_RE = re.compile(r"GHSA-[a-z0-9-]+", re.I)
BTC_RE = re.compile(r"\b(bc1[a-zA-HJ-NP-Z0-9]{25,90}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})\b")


def parse_sample(path: Path) -> dict:
    return _parse_sample_file(path)["meta"]


def q(s: str) -> str:
    """YAML double-quote escape."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def title_from_slug(slug: str) -> str:
    return " ".join(w.upper() if w in ("btc", "eth", "usd", "usdc", "nft", "ci", "f1", "nba", "nfl", "mlb", "nhl") else w.capitalize()
                    for w in slug.replace("_", "-").split("-"))


def split_url(url: str) -> tuple[str, str, list[tuple[str, str]], dict[str, str]]:
    """
    Return (base_url, external_path_template, query_params[(name,default)], path_params{name:default}).
    """
    u = urlparse(url.strip())
    base = f"{u.scheme}://{u.netloc}"
    path = unquote(u.path or "/")
    path_params: dict[str, str] = {}

    def sub(pat: re.Pattern, name: str, s: str) -> str:
        m = pat.search(s)
        if not m:
            return s
        path_params[name] = m.group(0)
        return s[: m.start()] + "{" + name + "}" + s[m.end() :]

    # Order matters — more specific first
    path = sub(GHSA_RE, "ghsa_id", path)
    path = sub(CVE_RE, "cve_id", path)
    path = sub(ADDR_RE, "address", path)
    path = sub(BTC_RE, "btc_address", path)

    # GeckoTerminal /networks/{network}/…
    m = re.search(r"/networks/([a-z0-9-]+)(/|$)", path)
    if m:
        path_params["network"] = m.group(1)
        path = path[: m.start()] + f"/networks/{{network}}{m.group(2)}" + path[m.end() :]

    # deps.dev /systems/{system}/packages/{pkg}/versions/{ver}
    m = re.search(r"/systems/([^/]+)/packages/([^/]+)/versions/([^/]+)/?$", path)
    if m:
        path_params["system"] = unquote(m.group(1))
        path_params["pkg"] = unquote(m.group(2))
        path_params["ver"] = unquote(m.group(3))
        path = re.sub(
            r"/systems/[^/]+/packages/[^/]+/versions/[^/]+/?$",
            "/systems/{system}/packages/{pkg}/versions/{ver}",
            path,
        )

    # pypi /pypi/{pkg}/{ver}/json
    m = re.search(r"/pypi/([^/]+)/([^/]+)/json$", path)
    if m:
        path_params["pkg"] = m.group(1)
        path_params["ver"] = m.group(2)
        path = re.sub(r"/pypi/[^/]+/[^/]+/json$", "/pypi/{pkg}/{ver}/json", path)

    # npm registry /{pkg}/{ver}
    m = re.search(r"^/([^/]+)/(\d+\.\d+\.\d+[^/]*)$", path)
    if m and "registry.npmjs" in u.netloc:
        path_params["pkg"] = m.group(1)
        path_params["ver"] = m.group(2)
        path = "/{pkg}/{ver}"

    # sportsdb eventslast.php?id= — query handled below; lookupevent similarly
    # GitHub repos/{owner}/{repo}/…
    m = re.search(r"/repos/([^/]+)/([^/]+)/(.*)$", path)
    if m and "api.github.com" in u.netloc:
        path_params["owner"] = m.group(1)
        path_params["repo"] = m.group(2)
        rest = m.group(3)
        # workflow file in path
        wm = re.search(r"workflows/([^/]+)/runs", rest)
        if wm:
            path_params["workflow"] = wm.group(1)
            rest = rest.replace(wm.group(1), "{workflow}", 1)
        path = f"/repos/{{owner}}/{{repo}}/{rest}"

    query = [(k, v) for k, v in parse_qsl(u.query, keep_blank_values=True)]
    return base, path, query, path_params


def render_yaml(
    *,
    miner_id: int,
    slug: str,
    intent: str,
    name: str,
    description: str,
    base_url: str,
    external_path: str,
    query: list[tuple[str, str]],
    path_params: dict[str, str],
    docs_url: str,
) -> str:
    label = LABEL.get(intent, "answer")
    # params block
    param_blocks = []
    if path_params:
        lines = ["      path:", "        required:"]
        for n, default in path_params.items():
            lines += [
                f"          - name: {n}",
                "            type: string",
                '            intents: ["*"]',
                f"            description: {n.replace('_', ' ')}",
            ]
        param_blocks.append("\n".join(lines))
    if query:
        lines = ["      query:", "        required:"]
        for n, _v in query:
            lines += [
                f"          - name: {n}",
                "            type: string",
                '            intents: ["*"]',
                f"            description: {n}",
            ]
        param_blocks.append("\n".join(lines))
    if not param_blocks:
        # no pins — still askable as fixed URL (static feed)
        param_blocks.append(
            "      query:\n"
            "        optional:\n"
            "          - name: _\n"
            "            type: string\n"
            '            intents: ["*"]\n'
            "            description: unused placeholder"
        )

    req_names = list(path_params.keys()) + [k for k, _ in query]
    if not req_names:
        input_schema = (
            "input_schema:\n"
            "  type: object\n"
            "  required: []\n"
            "  properties: {}\n"
        )
    else:
        props = []
        for n, default in list(path_params.items()) + query:
            props.append(
                f"    {json.dumps(n)}: {{type: string, description: {q(n)}, default: {q(default)}}}"
            )
        input_schema = (
            "input_schema:\n"
            "  type: object\n"
            f"  required: [{', '.join(json.dumps(n) for n in req_names)}]\n"
            "  properties:\n"
            + "\n".join(props)
            + "\n"
        )

    # Quote description if it might contain ": "
    desc = description.strip().replace("\n", " ")
    if ": " in desc or desc.startswith((">", "|")):
        desc_block = f"description: {q(desc)}"
    else:
        desc_block = f"description: >\n  {desc}"

    params_yaml = "\n".join(param_blocks)
    return f"""version: "1"
kind: miner
id: {miner_id}
slug: {slug}
protocol: generic
name: {q(name)}
{desc_block}

base_url: {base_url}

auth:
  type: none

rate_limit_per_sec: 1
cache_ttl_sec: 60
circuit_threshold: 5
circuit_cooldown_seconds: 30

docs:
  documentation: {docs_url}
  website: {base_url}

endpoints:
  - path: /query
    external_path: {external_path}
    method: GET
    description: Query for intent {intent} via {name}.
    intents: [{intent}]
    params:
{params_yaml}

{input_schema}
semantics:
  signal_mapping:
    label_field: {label}
  supported_intents:
    - {intent}

on_chain:
  description: Stores signal for {intent} (Semantic V2 format-agnostic).
  transform: direct
  min_price_usdc: 0.01
  fields:
    strings:
      - index: 0
        name: result
        description: Primary result
        source_path: result
      - index: 1
        name: intent
        description: Intent name
        source_path: intent
    integers:
      - index: 0
        name: ok
        description: Success flag
        source_path: ok
"""


def next_id_start() -> int:
    ids = []
    for p in OUT_YAMLS.rglob("*.yaml"):
        m = re.search(r"(?m)^id:\s*(\d+)", p.read_text(encoding="utf-8", errors="replace"))
        if m:
            ids.append(int(m.group(1)))
    return max(ids + [190000]) + 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--intent", default="", help="only one intent")
    ap.add_argument("--slug", default="", help="only one slug")
    ap.add_argument("--force", action="store_true", help="overwrite existing YAML")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    files = sorted(
        p
        for p in SAMPLES.rglob("*.md")
        if p.name not in ("_TEMPLATE.md", "README.md")
        and (not a.intent or a.intent.upper() in p.parent.name.upper())
        and (not a.slug or p.stem == a.slug)
    )

    mid = next_id_start()
    wrote = skipped = failed = 0
    report_lines = ["# YAML generation from approved samples", ""]

    for path in files:
        try:
            meta = parse_sample(path)
        except Exception as e:
            print(f"SKIP  {path}: {e}")
            skipped += 1
            continue
        if (meta.get("status") or "").strip() != "approved":
            skipped += 1
            continue
        intent = canonical_intent((meta.get("intent") or path.parent.name).strip().upper())
        slug = (meta.get("slug") or path.stem).strip()
        # Fail-closed: do not build YAML from manual-only approve
        src = (meta.get("review_source") or "").strip()
        llm = (meta.get("llm_used") or "").strip().lower()
        mode = (meta.get("review_mode") or "").strip()
        if os.environ.get("ALLOW_UNSAFE_REGISTER", "").strip() != "1":
            if src == "manual" or (llm not in ("true", "1", "yes") and "llm" not in mode):
                print(f"SKIP  {slug}: approved without auto_review+LLM (run auto_review --apply --require-llm)")
                skipped += 1
                continue
        url = (meta.get("request_url") or "").strip()
        if not url:
            print(f"FAIL  {slug}: no request_url")
            failed += 1
            continue
        if re.search(r"\{\w+\}|%7B\w+%7D", url):
            # cp-kraken shipped `pair: "{kraken_pair}"` this way: a template, not a question
            print(f"FAIL  {slug}: request_url still has an unfilled {{placeholder}}: {url}")
            failed += 1
            continue
        folder = intent_dir(intent)
        if not folder:
            print(f"FAIL  {slug}: no folder mapping for {intent}")
            failed += 1
            continue
        out_dir = OUT_YAMLS / folder
        out_path = out_dir / f"{slug}.yaml"
        if out_path.is_file() and not a.force:
            print(f"KEEP  {out_path.relative_to(ROOT)} (exists)")
            skipped += 1
            continue

        base, ext_path, query, path_params = split_url(url)
        desc = (meta.get("intent_description") or intent).strip().split("\n")[0][:200]
        req = (meta.get("answer_requirement") or "").strip().split("\n")[0][:160]
        full_desc = f"Semantic V2 miner for {intent}. {desc} Capture pin answers: {req}".strip()
        name = title_from_slug(slug)
        docs = base + "/"

        yml = render_yaml(
            miner_id=mid,
            slug=slug,
            intent=intent,
            name=name,
            description=full_desc,
            base_url=base,
            external_path=ext_path,
            query=query,
            path_params=path_params,
            docs_url=docs,
        )
        mid += 1

        if a.dry_run:
            print(f"DRY   {out_path.relative_to(ROOT)}")
            wrote += 1
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        out_path.write_text(yml, encoding="utf-8")

        # Gate: validate_miner_yaml (creation must not ship Group A breaks)
        p = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_miner_yaml.py"), str(out_path)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        if p.returncode != 0:
            print(f"FAIL  validate {out_path.relative_to(ROOT)}")
            print(p.stdout or p.stderr)
            out_path.unlink(missing_ok=True)
            failed += 1
            report_lines.append(f"- FAIL `{slug}` validate")
            continue

        print(f"WROTE {out_path.relative_to(ROOT)}")
        wrote += 1
        report_lines.append(
            f"- OK `{intent}/{slug}` → `{out_path.relative_to(ROOT)}` "
            f"(sample approved ✓ · validate ✓)"
        )

    report_lines += [
        "",
        f"summary wrote={wrote} skipped={skipped} failed={failed}",
        "",
        "## Next",
        "1. Host each YAML at `https://omni-chat…/miner-yamls/<slug>.yaml`",
        "2. Register:",
        "```bash",
        "./scripts/register-miner-v2.sh \\",
        "  --file intentYamls/<folder>/<slug>.yaml \\",
        "  --url https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml \\",
        "  --sample apiOutputSamples/<INTENT>/<slug>.md",
        "```",
        "",
    ]
    out_report = ROOT / "out" / "YAML_FROM_APPROVED.md"
    out_report.parent.mkdir(exist_ok=True)
    out_report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"\nsummary wrote={wrote} skipped={skipped} failed={failed}")
    print(f"WROTE  {out_report.relative_to(ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
