#!/usr/bin/env python3
"""
Capture a live API response into apiOutputSamples/<INTENT>/<slug>.md

Semantic Register V2 — format-agnostic: we store whatever the API returns.
A human must later set status=approved before register-miner-v2.sh.

  python3 scripts/capture_api_output.py \\
    --intent WEATHER_CURRENT \\
    --slug open-meteo-wx \\
    --url 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m' \\
    --description 'Current weather conditions for a location' \\
    --requirement 'Must convey current weather / temperature for the place asked'
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "apiOutputSamples"
UA = "telegraph-capture-api-output/2"


def slugify_intent(name: str) -> str:
    return re.sub(r"[^A-Z0-9_]+", "_", name.strip().upper()).strip("_")


def fetch(url: str, timeout: int = 60) -> tuple[str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            ctype = (r.headers.get("Content-Type") or "").split(";")[0].strip()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"FAIL  HTTP {e.code}: {body[:500]}") from e
    except Exception as e:
        raise SystemExit(f"FAIL  {type(e).__name__}: {e}") from e
    text = raw.decode("utf-8", errors="replace")
    return ctype, text


def pretty_body(text: str) -> tuple[str, str]:
    """Return (fence_lang, formatted_body)."""
    t = text.strip()
    if not t:
        return "text", "(empty body)"
    try:
        obj = json.loads(t)
        return "json", json.dumps(obj, indent=2, ensure_ascii=False)
    except json.JSONDecodeError:
        return "text", t


def write_sample(
    *,
    intent: str,
    slug: str,
    url: str,
    inputs: str,
    description: str,
    requirement: str,
    ctype: str,
    body: str,
    note: str,
) -> Path:
    intent_dir = SAMPLES / slugify_intent(intent)
    intent_dir.mkdir(parents=True, exist_ok=True)
    path = intent_dir / f"{slug}.md"
    fence, formatted = pretty_body(body)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    inputs_block = inputs.strip() or "(none / baked into URL)"
    desc = description.strip() or "(fill: catalog description)"
    req = requirement.strip() or (
        "Must answer what the intent description asks — any format OK "
        "(number, prose, any unit/currency/language)."
    )
    doc = f"""---
intent: {slugify_intent(intent)}
slug: {slug}
status: pending_review
captured_at: {now}
request_url: {url}
content_type: {ctype}
inputs: |
  {inputs_block}
intent_description: |
  {desc}
answer_requirement: |
  {req}
capture_note: |
  {note.strip() or "(none)"}
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```{fence}
{formatted}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
"""
    path.write_text(doc, encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description="Capture API output sample for Semantic V2 register")
    ap.add_argument("--intent", required=True, help="Catalog intent name, e.g. WEATHER_CURRENT")
    ap.add_argument("--slug", required=True, help="Miner / API slug, e.g. open-meteo-wx")
    ap.add_argument("--url", required=True, help="Full request URL with pins filled in")
    ap.add_argument("--inputs", default="", help="Human note of inputs used (lat/lon, ids, …)")
    ap.add_argument("--description", default="", help="Intent catalog description")
    ap.add_argument("--requirement", default="", help="What a correct answer must convey")
    ap.add_argument("--note", default="", help="Optional capture note")
    ap.add_argument("--timeout", type=int, default=60)
    a = ap.parse_args()

    if not re.match(r"^[a-z0-9][a-z0-9_-]*$", a.slug):
        print("FAIL  slug must be lowercase alphanumeric / - _", file=sys.stderr)
        return 1
    if re.search(r"\{\w+\}|%7B\w+%7D", a.url):
        print(f"FAIL  URL has an unfilled {{placeholder}}; fill the real value first: {a.url}", file=sys.stderr)
        return 1

    ctype, body = fetch(a.url, timeout=a.timeout)
    if not body.strip():
        print("FAIL  empty response body", file=sys.stderr)
        return 1

    path = write_sample(
        intent=a.intent,
        slug=a.slug,
        url=a.url,
        inputs=a.inputs,
        description=a.description,
        requirement=a.requirement,
        ctype=ctype,
        body=body,
        note=a.note,
    )
    print(f"WROTE  {path.relative_to(ROOT)}")
    print("status = pending_review")
    print("Next: open the file, verify the answer matches the intent, then:")
    print(
        f"  python3 scripts/set_sample_status.py --file {path.relative_to(ROOT)} "
        f"--status approved --note '…'"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
