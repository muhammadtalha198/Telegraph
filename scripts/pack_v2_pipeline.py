#!/usr/bin/env python3
"""
Pack candidates → Semantic Register V2 (fail-closed, deduped).

Ingest: files/Intent_Coverage_and_Candidates.xlsx
Tracker: PACK_V2_REGISTER_PIPELINE.md + out/pack_v2_queue.jsonl

Phases:
  classify   — dedup vs intentYamls/ (slug, host, publisher); write tracker
  smoke      — live GET smoke on ELIGIBLE keyless rows
  capture    — capture_api_output.py for smoke-pass
  review     — auto_review_samples.py --apply
  yaml       — generate_yamls_from_approved_samples.py
  register   — register_approved_v2_batch.py (pack slugs only)
  run        — smoke → capture → review → yaml (not register)

Usage (from MinerCreator/):
  python3 scripts/pack_v2_pipeline.py classify
  python3 scripts/pack_v2_pipeline.py smoke --limit 20
  python3 scripts/pack_v2_pipeline.py run --limit 5
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
PACK_XLSX = REPO / "files" / "Intent_Coverage_and_Candidates.xlsx"
SCRIPTS = Path(__file__).resolve().parent
OUT = ROOT / "out"
TRACKER = ROOT / "PACK_V2_REGISTER_PIPELINE.md"
QUEUE = OUT / "pack_v2_queue.jsonl"
UA = "telegraph-pack-v2/1"

sys.path.insert(0, str(SCRIPTS))
from v2_intent_folders import CATALOG_TO_CANONICAL, canonical_intent, intent_folder  # noqa: E402

BAD_BODY = [
    r"^\s*<!doctype html",
    r"^\s*<html",
    r"rate.?limit",
    r"too many requests",
    r"\bnot found\b",
    r"access denied",
    r"forbidden",
    r"unauthorized",
    r"invalid api key",
    r"api key.*(required|missing)",
]

# Resolve {placeholders} in Sample URL (golden-test defaults)
URL_DEFAULTS: dict[str, str] = {
    "sym": "BTC",
    "sym_lower": "btc",
    "name": "bitcoin",
    "lat": "52.52",
    "lon": "13.41",
    "lat1": "40.71",
    "lon1": "-74.01",
    "lat2": "34.05",
    "lon2": "-118.24",
    "qe": "EUR",
    "quote": "USD",
    "addr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "token": "USDC",
    "usdc": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "weth": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "base": "ethereum",
    "BASE_URL": "https://api.coingecko.com",
    "cve": "CVE-2021-44228",
    "type": "A",
    "ip": "8.8.8.8",
    "host": "example.com",
    "txid": "f4184fc596403b9d638783cf57adfe4c75c605bfd83c49e259dea15466447c4be",
    "vid": "v1",
    "amount": "1000000",
    "tgt": "en",
    "urle": "https%3A%2F%2Fexample.com",
    "full": "true",
    "cik": "0000320193",
    "cg": "ethereum",
    "src": "ETH",
    "cb": "BTC-USD",
    "kraken": "XBTUSD",
    "pair": "ETHUSD",
    "domain": "google.com",
    "record": "TXT",
    "network": "eth",
    "chain": "ethereum",
    "model": "gpt-3.5-turbo",
}


def norm_publisher(s: str) -> str:
    s = (s or "").lower().strip()
    s = re.sub(r"\s*\([^)]*\)", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


def norm_host(url: str) -> str:
    try:
        u = urlparse(url.strip())
        h = (u.hostname or "").lower()
        if h.startswith("www."):
            h = h[4:]
        return h
    except Exception:
        return ""


def fill_url(template: str, extra: dict[str, str] | None = None) -> str:
    vals = dict(URL_DEFAULTS)
    if extra:
        vals.update(extra)
    s = os.path.expandvars(template)

    def repl(m: re.Match) -> str:
        k = m.group(1)
        return vals.get(k, vals.get(k.lower(), m.group(0)))

    return re.sub(r"\{(\w+)\}", repl, s)


def load_openpyxl():
    try:
        import openpyxl  # type: ignore
    except ImportError:
        raise SystemExit("pip install openpyxl (or use MinerCreator .venv)") from None
    return openpyxl


def load_coverage_descriptions() -> dict[str, str]:
    openpyxl = load_openpyxl()
    wb = openpyxl.load_workbook(PACK_XLSX, read_only=True)
    ws = wb["Coverage (119 intents)"]
    headers = next(ws.iter_rows(min_row=1, max_row=1, values_only=True))
    idx = {h: i for i, h in enumerate(headers)}
    out: dict[str, str] = {}
    for row in ws.iter_rows(min_row=2, values_only=True):
        intent = row[idx["Intent"]]
        if not intent:
            continue
        note = row[idx.get("Status / ceiling note", idx["Intent"])] or ""
        out[str(intent).strip()] = str(note)[:500]
    return out


def parse_yaml_registry() -> tuple[set[str], dict[str, set[str]], dict[str, set[str]], dict[str, set[str]]]:
    """slugs, intent→hosts, intent→publishers, intent→slugs."""
    slugs: set[str] = set()
    hosts: dict[str, set[str]] = defaultdict(set)
    pubs: dict[str, set[str]] = defaultdict(set)
    by_slug_intent: dict[str, str] = {}

    for ypath in (ROOT / "intentYamls").rglob("*.yaml"):
        text = ypath.read_text(encoding="utf-8", errors="replace")
        slug = ypath.stem
        slugs.add(slug)
        m_name = re.search(r"(?m)^name:\s*(.+)$", text)
        m_base = re.search(r"(?m)^base_url:\s*(\S+)", text)
        intents = re.findall(r"(?m)^\s*-\s*([A-Z0-9_]+)\s*$", text)
        # supported_intents block only
        block = re.search(r"supported_intents:\s*\n((?:\s*-\s*[A-Z0-9_]+\s*\n)+)", text)
        if block:
            intents = re.findall(r"-\s*([A-Z0-9_]+)", block.group(1))
        for intent in intents:
            ci = canonical_intent(intent)
            if m_base:
                hosts[ci].add(norm_host(m_base.group(1)))
            if m_name:
                pubs[ci].add(norm_publisher(m_name.group(1).strip().strip('"')))
            pubs[ci].add(norm_publisher(slug.replace("-", " ")))
        by_slug_intent[slug] = canonical_intent(intents[0]) if intents else ""

    return slugs, hosts, pubs, by_slug_intent


def load_candidates() -> list[dict]:
    openpyxl = load_openpyxl()
    wb = openpyxl.load_workbook(PACK_XLSX, read_only=True)
    ws = wb["Candidates"]
    headers = next(ws.iter_rows(min_row=1, max_row=1, values_only=True))
    idx = {h: i for i, h in enumerate(headers)}
    rows = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        intent = row[idx["Intent"]]
        slug = row[idx["Slug"]]
        if not intent or not slug:
            continue
        rows.append(
            {
                "intent_catalog": str(intent).strip(),
                "intent": canonical_intent(str(intent)),
                "slug": str(slug).strip(),
                "publisher": str(row[idx["Source (publisher)"]] or "").strip(),
                "method": (row[idx["Method"]] or "GET").strip().upper(),
                "env": (row[idx["Env var needed"]] or "").strip() if row[idx["Env var needed"]] else "",
                "url_template": str(row[idx["Sample URL"]] or "").strip(),
                "possible_existing": str(row[idx["Possible existing repo slug"]] or "").strip(),
                "note": str(row[idx["Note"]] or "").strip() if "Note" in idx else "",
            }
        )
    return rows


def classify_row(row: dict, reg: tuple) -> str:
    slugs, hosts, pubs, _ = reg
    slug = row["slug"]
    intent = row["intent"]
    if slug in slugs:
        return "ALREADY_REGISTERED"
    poss = [p.strip() for p in re.split(r"[,;]", row.get("possible_existing", "")) if p.strip()]
    if any(p in slugs for p in poss):
        return "ALREADY_REGISTERED"
    if row.get("env") and not os.environ.get(row["env"]):
        return "NEEDS_API_KEY"
    if row["method"] != "GET":
        return "SKIP_POST"
    if not intent_folder(row["intent_catalog"]):
        return "NO_INTENT_FOLDER"
    resolved = fill_url(row["url_template"])
    h = norm_host(resolved)
    pub = norm_publisher(row["publisher"])
    if h and h in hosts.get(intent, set()):
        return "SAME_HOST_AS_REGISTERED"
    if pub and pub in pubs.get(intent, set()):
        return "SAME_PUBLISHER_AS_REGISTERED"
    return "ELIGIBLE"


def run_classify() -> list[dict]:
    reg = parse_yaml_registry()
    desc = load_coverage_descriptions()
    candidates = load_candidates()
    OUT.mkdir(parents=True, exist_ok=True)

    # Reload prior queue state
    prior: dict[str, dict] = {}
    if QUEUE.is_file():
        for line in QUEUE.read_text(encoding="utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                prior[d["slug"]] = d

    rows_out = []
    counts = Counter()
    for c in candidates:
        status = classify_row(c, reg)
        counts[status] += 1
        rec = {
            **c,
            "status": status,
            "folder": intent_folder(c["intent_catalog"]),
            "resolved_url": fill_url(c["url_template"]) if c["url_template"] else "",
            "host": norm_host(fill_url(c["url_template"])) if c["url_template"] else "",
            "description": desc.get(c["intent_catalog"], desc.get(c["intent"], "")),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        old = prior.get(c["slug"])
        if old:
            for k in ("smoke", "capture_path", "register_tx", "register_ok"):
                if k in old:
                    rec[k] = old[k]
            if old.get("status") in ("SMOKE_PASS", "CAPTURED", "APPROVED", "REGISTERED") and status == "ELIGIBLE":
                rec["status"] = old["status"]
        rows_out.append(rec)

    QUEUE.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows_out) + "\n", encoding="utf-8")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    md = [
        "# Pack → Semantic V2 register pipeline",
        "",
        f"Updated: **{now}**",
        f"Source: `{PACK_XLSX.relative_to(REPO)}`",
        f"Queue: `{QUEUE.relative_to(ROOT)}`",
        "",
        "Dedup rules (fail-closed): **slug** already in `intentYamls/` → already registered; "
        "same **host** or **publisher** for that intent → do not register (one source per intent).",
        "",
        "## Summary",
        "",
        "| Status | Count |",
        "|--------|------:|",
    ]
    for k, v in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        md.append(f"| `{k}` | {v} |")
    md += ["", f"**Total candidates:** {len(rows_out)}", ""]

    for section in (
        "ALREADY_REGISTERED",
        "SAME_HOST_AS_REGISTERED",
        "SAME_PUBLISHER_AS_REGISTERED",
        "NEEDS_API_KEY",
        "SKIP_POST",
        "ELIGIBLE",
    ):
        subset = [r for r in rows_out if r["status"] == section]
        if not subset:
            continue
        md += [f"## {section} ({len(subset)})", ""]
        md += ["| Intent | Slug | Publisher | Host |", "|--------|------|-----------|------|"]
        for r in subset[:200]:
            md.append(
                f"| `{r['intent']}` | `{r['slug']}` | {r['publisher'][:40]} | `{r.get('host','')}` |"
            )
        if len(subset) > 200:
            md.append(f"| … | *{len(subset) - 200} more* | | |")
        md.append("")

    md += [
        "## Next commands",
        "",
        "```bash",
        "cd MinerCreator",
        "python3 scripts/pack_v2_pipeline.py smoke          # live GET on ELIGIBLE",
        "python3 scripts/pack_v2_pipeline.py capture        # apiOutputSamples",
        "python3 scripts/auto_review_samples.py --apply --require-llm --all",
        "python3 scripts/generate_yamls_from_approved_samples.py --force",
        "python3 scripts/pack_v2_pipeline.py register  # only auto_review+LLM approved; gates re-check",
        "```",
        "",
    ]
    TRACKER.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"WROTE {TRACKER.relative_to(ROOT)}")
    print(f"WROTE {QUEUE.relative_to(ROOT)}")
    print(dict(counts))
    return rows_out


def load_queue() -> list[dict]:
    if not QUEUE.is_file():
        raise SystemExit("Run classify first")
    return [json.loads(line) for line in QUEUE.read_text(encoding="utf-8").splitlines() if line.strip()]


def save_queue(rows: list[dict]) -> None:
    QUEUE.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")


def smoke_one(url: str, timeout: int = 45) -> tuple[bool, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:120]
    if not body.strip():
        return False, "empty body"
    low = body[:4000].lower()
    for pat in BAD_BODY:
        if re.search(pat, low, re.I):
            return False, f"bad body ({pat[:30]})"
    return True, f"ok {len(body)} bytes"


def phase_smoke(limit: int = 0) -> None:
    rows = load_queue()
    todo = [r for r in rows if r["status"] == "ELIGIBLE"]
    if limit:
        todo = todo[:limit]
    print(f"smoke n={len(todo)}")
    by_slug = {r["slug"]: r for r in rows}
    ok = fail = 0
    for i, r in enumerate(todo, 1):
        url = r.get("resolved_url") or fill_url(r["url_template"])
        good, msg = smoke_one(url)
        rec = by_slug[r["slug"]]
        rec["smoke"] = {"ok": good, "msg": msg, "url": url, "at": datetime.now(timezone.utc).isoformat()}
        rec["status"] = "SMOKE_PASS" if good else "SMOKE_FAIL"
        print(f"[{i}/{len(todo)}] {r['slug']} {'PASS' if good else 'FAIL'} {msg[:60]}")
        ok += good
        fail += not good
        time.sleep(0.35)
    save_queue(rows)
    print(f"smoke done pass={ok} fail={fail}")


def phase_capture(limit: int = 0) -> None:
    rows = load_queue()
    todo = [r for r in rows if r["status"] == "SMOKE_PASS"]
    if limit:
        todo = todo[:limit]
    by_slug = {r["slug"]: r for r in rows}
    for i, r in enumerate(todo, 1):
        url = r.get("resolved_url") or fill_url(r["url_template"])
        intent_fm = r["intent_catalog"]  # capture uses catalog folder name in samples
        desc = r.get("description") or f"Pack candidate {r['publisher']}"
        req = (
            f"Must satisfy catalog intent {r['intent']} via upstream {r['publisher']}"
        )
        cmd = [
            sys.executable,
            str(SCRIPTS / "capture_api_output.py"),
            "--intent",
            r["intent"],
            "--slug",
            r["slug"],
            "--url",
            url,
            "--description",
            desc[:400],
            "--requirement",
            req,
        ]
        print(f"[{i}/{len(todo)}] capture {r['slug']}")
        p = subprocess.run(cmd, cwd=str(ROOT))
        rec = by_slug[r["slug"]]
        sample = ROOT / "apiOutputSamples" / re.sub(r"[^A-Z0-9_]+", "_", r["intent"].upper()).strip("_") / f"{r['slug']}.md"
        if p.returncode == 0 and sample.is_file():
            rec["status"] = "CAPTURED"
            rec["capture_path"] = str(sample.relative_to(ROOT))
        else:
            rec["status"] = "CAPTURE_FAIL"
        save_queue(rows)


def phase_review() -> None:
    """Mandatory LLM auto_review — no --no-llm. Rejected/needs_human stay off the register queue."""
    p = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "auto_review_samples.py"),
            "--apply",
            "--require-llm",
            "--all",
        ],
        cwd=str(ROOT),
    )
    if p.returncode != 0 and not (
        os.environ.get("OMNIROUTE_API_KEY")
        or os.environ.get("OPENAI_API_KEY")
        or os.environ.get("OLLAMA_BASE_URL")
    ):
        raise SystemExit(
            "FAIL  phase_review needs Ollama (OLLAMA_BASE_URL) or OMNIROUTE_API_KEY / OPENAI_API_KEY "
            "(auto_review+LLM is mandatory before register)"
        )
    rows = load_queue()
    for r in rows:
        if r["status"] not in ("CAPTURED", "SMOKE_PASS", "APPROVED"):
            continue
        sample = (
            ROOT
            / "apiOutputSamples"
            / re.sub(r"[^A-Z0-9_]+", "_", r["intent"].upper()).strip("_")
            / f"{r['slug']}.md"
        )
        if not sample.is_file():
            continue
        t = sample.read_text(encoding="utf-8", errors="replace")
        approved = re.search(r"(?m)^status:\s*approved\s*$", t)
        llm = re.search(r"(?m)^llm_used:\s*(true|1|yes)\s*$", t, re.I)
        src = re.search(r"(?m)^review_source:\s*auto_review\s*$", t)
        if approved and llm and src:
            r["status"] = "APPROVED"
        elif approved and not (llm and src):
            r["status"] = "NEEDS_LLM_REVIEW"
        elif re.search(r"(?m)^status:\s*rejected\s*$", t):
            r["status"] = "REJECTED"
        else:
            r["status"] = "NEEDS_HUMAN"
    save_queue(rows)


def phase_yaml() -> None:
    subprocess.run(
        [sys.executable, str(SCRIPTS / "generate_yamls_from_approved_samples.py"), "--force"],
        cwd=str(ROOT),
        check=False,
    )


def phase_register(limit: int = 0) -> None:
    pack_slugs = {r["slug"] for r in load_queue() if r["status"] == "APPROVED"}
    if not pack_slugs:
        print("no APPROVED pack slugs in queue")
        return
    argv = [sys.executable, str(SCRIPTS / "register_approved_v2_batch.py")]
    if limit:
        argv += ["--limit", str(limit)]
    # register script processes all approved; filter via temp env list file
    env = os.environ.copy()
    env["PACK_V2_SLUGS"] = ",".join(sorted(pack_slugs))
    subprocess.run(argv, cwd=str(ROOT), env=env, check=False)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "phase",
        choices=["classify", "smoke", "capture", "review", "yaml", "register", "run"],
    )
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    if not PACK_XLSX.is_file():
        raise SystemExit(f"missing {PACK_XLSX}")

    if a.phase == "classify":
        run_classify()
        return 0
    if a.phase == "smoke":
        phase_smoke(a.limit)
        return 0
    if a.phase == "capture":
        phase_capture(a.limit)
        return 0
    if a.phase == "review":
        phase_review()
        return 0
    if a.phase == "yaml":
        phase_yaml()
        return 0
    if a.phase == "register":
        phase_register(a.limit)
        return 0
    if a.phase == "run":
        run_classify()
        phase_smoke(a.limit)
        phase_capture(a.limit)
        phase_review()
        phase_yaml()
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
