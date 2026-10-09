#!/usr/bin/env python3
"""Refresh tests/fixtures/live/*.json: call every source of every spec test once, live,
and save the (trimmed) response + fetch time. tests/test_real_specs.py replays them
offline, so a spec path that stops matching the real API shape fails a test.

  .venv/bin/python tests/record_live.py            # all intents
  .venv/bin/python tests/record_live.py FX_NOW
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from minercheck.fetch import Fetcher  # noqa: E402
from minercheck.geocode import open_meteo_geocoder  # noqa: E402
from minercheck.normalize import normalize  # noqa: E402
from minercheck.spec import Registry  # noqa: E402
from minercheck.errors import ExtractError  # noqa: E402
from minercheck.verify import build_request  # noqa: E402

OUT = ROOT / "tests" / "fixtures" / "live"
KEEP = {"usd", "eur", "pkr", "jpy"}


def trim_json(obj):
    """Big dicts (rate tables) keep only the currencies the tests use; long lists keep 2 items."""
    if isinstance(obj, dict):
        # a big dict whose keys are all short codes is a rate/price table -> keep only tested currencies;
        # a big dict with descriptive keys (a quote object) is kept as-is so its fields survive
        if len(obj) > 40 and all(len(str(k)) <= 5 for k in obj):
            obj = {k: v for k, v in obj.items() if k.lower() in KEEP}
        return {k: trim_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        # keep first and last so both .0 and .-1 (latest timeseries point) survive trimming
        keep = obj if len(obj) <= 3 else [obj[0], obj[-1]]
        return [trim_json(x) for x in keep]
    return obj


def scrub(text: str) -> str:
    """Never commit the recording machine's IP / location (Cloudflare trace, time.now client_ip)."""
    text = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "203.0.113.1", text)          # TEST-NET-3
    text = re.sub(r"(?m)^(loc|colo)=\w+", lambda m: f"{m.group(1)}=XX", text)
    return re.sub(r'"client_ip":\s*"[^"]*"', '"client_ip": "203.0.113.1"', text)


def trim(body: str, ctype: str) -> str:
    t = scrub(body.strip())
    if t[:1] in "{[":
        try:
            return json.dumps(trim_json(json.loads(t)), ensure_ascii=False)
        except ValueError:
            return t
    if "<item>" in t:  # floatrates: keep the items tests ask for
        head = t.split("<item>", 1)[0]
        items = [m for m in re.findall(r"<item>.*?</item>", t, re.S)
                 if re.search(r"<targetCurrency>(EUR|PKR|JPY)</targetCurrency>", m)]
        return head + "\n".join(items) + "\n</channel>"
    m = re.search(r'<span class="ccOutputRslt">.*?</span>\s*</span>|<span class="ccOutputRslt">.*?</span>', t, re.S)
    if m:  # x-rates: keep just the result span inside a minimal page
        return f"<!DOCTYPE html><html><body><div>{m.group(0)}</div></body></html>"
    return t[:20000]


def main() -> int:
    reg = Registry()
    fetcher = Fetcher()
    geocoder = open_meteo_geocoder(fetcher)
    only = {a.upper() for a in sys.argv[1:]}
    OUT.mkdir(parents=True, exist_ok=True)
    for name, spec in sorted(reg.specs.items()):
        if only and name not in only:
            continue
        rows = []
        for t in spec.tests:
            norm = normalize(spec, t["inputs"], reg.shared, geocoder)
            for src in spec.sources:
                if not src.enabled:
                    continue                         # disabled (wrong-kind) miners are gated by slug, not recorded
                if any(str(norm.values.get(k)) != v for k, v in src.when.items()):
                    continue                         # source does not apply to this question
                try:
                    req = build_request(src, norm.vars)
                except ExtractError as e:
                    print(f"{name}/{t['id']}/{src.id}: SKIP ({e})")
                    continue
                res = fetcher.fetch(req)
                body = res.body.decode("utf-8", "replace")
                rows.append({"test": t["id"], "source": src.id, "url": req.url, "status": res.status,
                             "http_status": res.http_status, "error": res.error,
                             "headers": {k: v for k, v in res.headers.items() if k in ("content-type", "date")},
                             "body": trim(body, res.headers.get("content-type", "")),
                             "fetched_at": res.fetched_at.isoformat()})
                print(f"{name}/{t['id']}/{src.id}: {res.status} {res.http_status} {len(body)}B")
        (OUT / f"{name}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
