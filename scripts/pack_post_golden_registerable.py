#!/usr/bin/env python3
"""
After miner_pack/run_golden_tests.py:
  - load results/approved.json
  - drop already-registered / same-host / same-publisher
  - require sample status approved via auto_review+LLM
  - write out/PACK_REGISTERABLE.md
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
PACK = REPO / "miner_pack"
APPROVED = PACK / "results" / "approved.json"
SUMMARY = PACK / "results" / "summary.md"
YAMLS = ROOT / "intentYamls"
OUT = ROOT / "out" / "PACK_REGISTERABLE.md"
SAMPLES = ROOT / "apiOutputSamples"

CAT = {
    "CRYPTO_PRICE_LOOKUP": "CRYPTO_PRICE",
    "GAS_PRICE_ESTIMATION": "GAS_PRICE",
    "SSL_CERTIFICATE_VERIFY": "SSL_VERIFICATION",
    "URL_CONTENT_EXTRACTION": "CONTENT_EXTRACTION",
    "WEB_SEARCH_QUERY": "WEB_SEARCH",
    "WEATHER_CURRENT": "WEATHER_CHECK",
    "STOCK_PRICE_QUOTE": "STOCK_PRICE",
}


def canon(i: str) -> str:
    u = (i or "").strip().upper()
    return CAT.get(u, u)


def host(url: str) -> str:
    try:
        u = re.sub(r"\{[^}]+\}", "x", (url or "").replace("${BASE_URL}", "https://x.invalid"))
        h = (urlparse(u).hostname or "").lower()
        return h[4:] if h.startswith("www.") else h
    except Exception:
        return ""


def pub(s: str) -> str:
    s = re.sub(r"\s*\([^)]*\)", "", (s or "").lower())
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def load_registry():
    slugs = set()
    hosts = defaultdict(set)
    pubs = defaultdict(set)
    for y in YAMLS.rglob("*.yaml"):
        t = y.read_text(encoding="utf-8", errors="replace")
        slug = y.stem
        slugs.add(slug)
        mb = re.search(r"(?m)^base_url:\s*(\S+)", t)
        mn = re.search(r"(?m)^name:\s*(.+)$", t)
        block = re.search(r"supported_intents:\s*\n((?:\s*-\s*[A-Z0-9_]+\s*\n)+)", t)
        intents = re.findall(r"-\s*([A-Z0-9_]+)", block.group(1)) if block else []
        for intent in intents:
            ci = canon(intent)
            if mb:
                hosts[ci].add(host(mb.group(1)))
            if mn:
                pubs[ci].add(pub(mn.group(1).strip().strip('"')))
            pubs[ci].add(pub(slug.replace("-", " ")))
    return slugs, hosts, pubs


def sample_path(intent: str, slug: str) -> Path:
    # capture may use catalog or canonical folder names
    for name in {intent, canon(intent)}:
        d = SAMPLES / re.sub(r"[^A-Z0-9_]+", "_", name.upper()).strip("_")
        p = d / f"{slug}.md"
        if p.is_file():
            return p
    return SAMPLES / re.sub(r"[^A-Z0-9_]+", "_", canon(intent).upper()).strip("_") / f"{slug}.md"


def sample_llm_approved(path: Path) -> tuple[bool, str]:
    if not path.is_file():
        return False, "no_sample"
    t = path.read_text(encoding="utf-8", errors="replace")
    st = re.search(r"(?m)^status:\s*(\S+)", t)
    status = st.group(1) if st else ""
    if status != "approved":
        return False, status or "missing_status"
    src = re.search(r"(?m)^review_source:\s*(\S+)", t)
    llm = re.search(r"(?m)^llm_used:\s*(\S+)", t)
    mode = re.search(r"(?m)^review_mode:\s*(.+)$", t)
    if (src and src.group(1) == "auto_review") and (
        (llm and llm.group(1).lower() in ("true", "1", "yes"))
        or (mode and "llm" in mode.group(1).lower())
    ):
        return True, "approved_llm"
    return False, f"approved_but_not_llm (src={src.group(1) if src else ''} llm={llm.group(1) if llm else ''})"


def main() -> int:
    if not APPROVED.is_file():
        print(f"FAIL  missing {APPROVED} — run golden tests first", file=sys.stderr)
        return 1
    approved = json.loads(APPROVED.read_text(encoding="utf-8"))
    reg_slugs, hosts, pubs = load_registry()

    rows = []
    for intent, cands in approved.items():
        for c in cands:
            slug = c["slug"]
            url = c.get("url") or ""
            source = c.get("source") or ""
            h = host(url)
            ci = canon(intent)
            if slug in reg_slugs:
                bucket = "DUP_SAME_SLUG"
            elif h and h in hosts.get(ci, set()):
                bucket = "DUP_SAME_HOST"
            elif pub(source) and pub(source) in pubs.get(ci, set()):
                bucket = "DUP_SAME_PUBLISHER"
            else:
                bucket = "NEW"
            sp = sample_path(intent, slug)
            ok_llm, why = sample_llm_approved(sp)
            rows.append(
                {
                    "intent": intent,
                    "canon": ci,
                    "slug": slug,
                    "source": source,
                    "url": url,
                    "host": h,
                    "bucket": bucket,
                    "sample": str(sp.relative_to(ROOT)) if sp.is_file() else "",
                    "llm_ok": ok_llm,
                    "llm_why": why,
                }
            )

    # auto-review only NEW with samples
    to_review = [r for r in rows if r["bucket"] == "NEW" and r["sample"] and not r["llm_ok"]]
    print(f"golden_approved_rows={len(rows)} new={sum(1 for r in rows if r['bucket']=='NEW')} to_auto_review={len(to_review)}")

    # Review each NEW sample with gate-style LLM (apply)
    for i, r in enumerate(to_review, 1):
        print(f"[{i}/{len(to_review)}] auto_review --gate {r['slug']}", flush=True)
        p = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "auto_review_samples.py"),
                "--gate",
                "--file",
                str(ROOT / r["sample"]),
            ],
            cwd=str(ROOT),
        )
        # refresh
        ok_llm, why = sample_llm_approved(ROOT / r["sample"])
        r["llm_ok"] = ok_llm
        r["llm_why"] = why if p.returncode == 0 or ok_llm else f"gate_exit={p.returncode};{why}"

    # refresh all NEW after reviews
    for r in rows:
        if r["sample"]:
            ok_llm, why = sample_llm_approved(ROOT / r["sample"])
            r["llm_ok"] = ok_llm
            r["llm_why"] = why

    registerable = [r for r in rows if r["bucket"] == "NEW" and r["llm_ok"]]
    blocked = [r for r in rows if r["bucket"] == "NEW" and not r["llm_ok"]]

    lines = [
        "# Pack registerable after golden + auto_review+LLM",
        "",
        f"Golden approved intents: **{len(approved)}** · golden-pass rows: **{len(rows)}**",
        f"Already registered / same source: **{sum(1 for r in rows if r['bucket'].startswith('DUP'))}**",
        f"New sources golden-pass: **{sum(1 for r in rows if r['bucket']=='NEW')}**",
        f"**Registerable (NEW + auto_review LLM approved): {len(registerable)}**",
        f"Blocked (NEW but LLM not approved / no sample): **{len(blocked)}**",
        "",
        "## Registerable now",
        "",
        "| Intent | Slug | Source | Sample |",
        "|--------|------|--------|--------|",
    ]
    for r in sorted(registerable, key=lambda x: (x["intent"], x["slug"])):
        lines.append(f"| `{r['intent']}` | `{r['slug']}` | {r['source'][:40]} | `{r['sample']}` |")

    lines += ["", "## Golden-pass but NOT registerable yet", ""]
    lines += ["| Intent | Slug | Why |", "|--------|------|-----|"]
    for r in sorted(blocked, key=lambda x: (x["intent"], x["slug"])):
        lines.append(f"| `{r['intent']}` | `{r['slug']}` | {r['llm_why']} |")

    lines += ["", "## Golden-pass but already registered / same source", ""]
    lines += ["| Intent | Slug | Bucket |", "|--------|------|--------|"]
    for r in sorted([x for x in rows if x["bucket"].startswith("DUP")], key=lambda x: (x["intent"], x["slug"])):
        lines.append(f"| `{r['intent']}` | `{r['slug']}` | `{r['bucket']}` |")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {OUT.relative_to(ROOT)}")
    print(f"REGISTERABLE={len(registerable)} BLOCKED_NEW={len(blocked)}")
    for r in registerable:
        print(f"  OK  {r['intent']}/{r['slug']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
