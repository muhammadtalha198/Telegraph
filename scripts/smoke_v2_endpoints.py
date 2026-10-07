#!/usr/bin/env python3
"""Smoke-test V2 endpoint candidates: HTTP status + short body sniff."""
from __future__ import annotations
import json, sys, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "telegraph-v2-endpoint-smoke/1"
path = ROOT / "additions" / "v2_endpoints_research.json"
items = json.loads(path.read_text())
# optional: only one intent
intent = sys.argv[1].upper() if len(sys.argv) > 1 else ""

ok = fail = skip = 0
for it in items:
    if intent and it["intent"] != intent:
        continue
    if it.get("needs_fill") or "FILL_" in it["url"]:
        print(f"SKIP  {it['slug']}  needs real hash/key fill")
        skip += 1
        continue
    url = it["url"]
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,*/*"})
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read(800)
            code = r.status
        text = body.decode("utf-8", "replace").lower()
        bad = any(x in text for x in ("<!doctype html", "<html", "rate limit", "too many requests", "access denied"))
        if code == 200 and body and not bad and body.strip() not in (b"{}", b"[]", b"null"):
            print(f"OK    {it['slug']:32} HTTP {code}  {len(body)}+ bytes")
            ok += 1
            it["smoke"] = "ok"
        else:
            print(f"FAIL  {it['slug']:32} HTTP {code}  sniff={text[:80]!r}")
            fail += 1
            it["smoke"] = "fail"
    except Exception as e:
        print(f"FAIL  {it['slug']:32} {type(e).__name__}: {e}")
        fail += 1
        it["smoke"] = f"fail:{type(e).__name__}"

path.write_text(json.dumps(items, indent=2) + "\n")
print(f"\nsummary  ok={ok} fail={fail} skip={skip}  (smoke field written back to JSON)")
