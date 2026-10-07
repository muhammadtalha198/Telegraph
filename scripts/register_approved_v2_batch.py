#!/usr/bin/env python3
"""
Register all APPROVED V2 samples that have local YAMLs.

Per miner (fail-closed, no gate bypass):
  1) scripts/upload-host.sh <yaml>
  2) scripts/register-miner-v2.sh --file … --url … --sample …

Usage (from MinerCreator/):
  python3 scripts/register_approved_v2_batch.py
  python3 scripts/register_approved_v2_batch.py --limit 3   # smoke
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from v2_intent_folders import intent_folder  # noqa: E402

PACK_SLUG_FILTER = {s.strip() for s in os.environ.get("PACK_V2_SLUGS", "").split(",") if s.strip()}


def approved_rows():
    rows = []
    for p in sorted((ROOT / "apiOutputSamples").rglob("*.md")):
        if p.name in ("_TEMPLATE.md", "README.md"):
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if not re.search(r"(?m)^status:\s*approved\s*$", t):
            continue
        if os.environ.get("ALLOW_UNSAFE_REGISTER", "").strip() != "1":
            if not re.search(r"(?m)^review_source:\s*auto_review\s*$", t):
                continue
            if not re.search(r"(?m)^llm_used:\s*(true|1|yes)\s*$", t, re.I) and not re.search(
                r"(?m)^review_mode:.*llm", t, re.I
            ):
                continue
        intent_m = re.search(r"(?m)^intent:\s*(\S+)", t)
        slug_m = re.search(r"(?m)^slug:\s*(\S+)", t)
        if not intent_m or not slug_m:
            continue
        intent, slug = intent_m.group(1), slug_m.group(1)
        if PACK_SLUG_FILTER and slug not in PACK_SLUG_FILTER:
            continue
        folder = intent_folder(intent)
        if not folder:
            continue
        y = ROOT / "intentYamls" / folder / f"{slug}.yaml"
        if not y.is_file():
            rows.append({"ok_pre": False, "intent": intent, "slug": slug, "reason": "missing_yaml"})
            continue
        rows.append(
            {
                "ok_pre": True,
                "intent": intent,
                "slug": slug,
                "yaml": y,
                "sample": p,
            }
        )
    return rows


def host_yaml(ypath: Path) -> str:
    p = subprocess.run(
        ["bash", str(ROOT / "scripts" / "upload-host.sh"), str(ypath)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "host failed")[:400])
    m = re.search(r"(?m)^YAML_URL=(.+)$", p.stdout)
    if not m:
        raise RuntimeError(f"no YAML_URL in host output: {p.stdout[:200]}")
    return m.group(1).strip()


def register(ypath: Path, url: str, sample: Path) -> dict:
    p = subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "register-miner-v2.sh"),
            "--file",
            str(ypath),
            "--url",
            url,
            "--sample",
            str(sample),
        ],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    log = (p.stdout or "") + "\n" + (p.stderr or "")
    if p.returncode != 0:
        raise RuntimeError(log[-1500:])
    last = ROOT / "out" / "last-registration-v2.json"
    data = json.loads(last.read_text()) if last.is_file() else {}
    data["log_tail"] = log[-500:]
    return data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--slug", default="")
    a = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_path = OUT / f"V2_REGISTER_BATCH-{stamp}.log"
    report_path = OUT / ("PACK_V2_REGISTER.jsonl" if PACK_SLUG_FILTER else "V2_REGISTER_BATCH.jsonl")
    md_path = OUT / ("PACK_V2_REGISTER.md" if PACK_SLUG_FILTER else "V2_REGISTER_BATCH.md")

    rows = [r for r in approved_rows() if r.get("ok_pre")]
    if a.slug:
        rows = [r for r in rows if r["slug"] == a.slug]
    # Resume: skip slugs already ok in prior jsonl reports
    done = set()
    for prev in {report_path, OUT / "V2_REGISTER_BATCH.jsonl", OUT / "PACK_V2_REGISTER.jsonl"}:
        if not prev.is_file():
            continue
        for line in prev.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("ok") and d.get("slug"):
                done.add(d["slug"])
    if done:
        before = len(rows)
        rows = [r for r in rows if r["slug"] not in done]
        print(f"resume_skip_already_ok={before - len(rows)}")
    if a.limit:
        rows = rows[: a.limit]

    missing = [r for r in approved_rows() if not r.get("ok_pre")]
    lines = [f"=== V2 batch register {datetime.now(timezone.utc).isoformat()} ===", f"to_register={len(rows)} missing_yaml={len(missing)}"]
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if not done:
        report_path.write_text("", encoding="utf-8")
    print("\n".join(lines))

    ok = fail = 0
    results = []
    for i, r in enumerate(rows, 1):
        slug, intent = r["slug"], r["intent"]
        msg = f"[{i}/{len(rows)}] REGISTER {intent}/{slug}"
        print(msg, flush=True)
        with log_path.open("a", encoding="utf-8") as lf:
            lf.write("\n" + msg + "\n")
        try:
            url = host_yaml(r["yaml"])
            print(f"  HOST  {url}", flush=True)
            with log_path.open("a", encoding="utf-8") as lf:
                lf.write(f"HOST {url}\n")
            data = register(r["yaml"], url, r["sample"])
            data.update({"slug": slug, "intent": intent, "ok": True, "yaml_url": url})
            results.append(data)
            ok += 1
            print(f"  PASS  id≈{data.get('new_registration_id')} tx={data.get('tx_hash','')[:18]}…", flush=True)
            with log_path.open("a", encoding="utf-8") as lf:
                lf.write(f"PASS {json.dumps({k: data.get(k) for k in ('new_registration_id','tx_hash','tx_url')})}\n")
        except Exception as e:
            fail += 1
            err = str(e).replace("\n", " ")[:400]
            row = {"slug": slug, "intent": intent, "ok": False, "error": err}
            results.append(row)
            print(f"  FAIL  {err[:160]}", flush=True)
            with log_path.open("a", encoding="utf-8") as lf:
                lf.write(f"FAIL {err}\n")
        with report_path.open("a", encoding="utf-8") as rf:
            rf.write(json.dumps(results[-1], default=str) + "\n")
        time.sleep(int(os.environ.get("REGISTER_BATCH_SLEEP", "4")))

    md = [
        "# V2 register batch",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"ok **{ok}** · fail **{fail}** · attempted **{len(rows)}**",
        "",
        "## Registered",
        "",
    ]
    for r in results:
        if r.get("ok"):
            md.append(
                f"- `{r.get('intent')}/{r.get('slug')}` id≈`{r.get('new_registration_id')}` · "
                f"[tx]({r.get('tx_url','')})"
            )
    md += ["", "## Failed", ""]
    for r in results:
        if not r.get("ok"):
            md.append(f"- `{r.get('intent')}/{r.get('slug')}` — `{r.get('error','')[:180]}`")
    md_path.write_text("\n".join(md) + "\n", encoding="utf-8")
    summary = f"DONE ok={ok} fail={fail}"
    print(summary)
    print(f"WROTE {md_path.relative_to(ROOT)}")
    with log_path.open("a", encoding="utf-8") as lf:
        lf.write(summary + "\n")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
