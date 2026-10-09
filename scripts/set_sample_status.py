#!/usr/bin/env python3
"""
Set review status on an apiOutputSamples/*.md file.

Manual approve does NOT unlock registerMiner — register_gates_v2 always re-runs
auto_review + LLM. Use this only for bookkeeping / forcing pending_review.

  python3 scripts/set_sample_status.py \\
    --file apiOutputSamples/WEATHER_CURRENT/open-meteo-wx.md \\
    --status approved \\
    --note 'Clear temperature; answers current weather'
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from sample_file import replace_or_add  # noqa: E402

ALLOWED = {"pending_review", "approved", "rejected"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, type=Path)
    ap.add_argument("--status", required=True, choices=sorted(ALLOWED))
    ap.add_argument("--note", default="")
    a = ap.parse_args()

    path = a.file if a.file.is_absolute() else ROOT / a.file
    if not path.is_file():
        print(f"FAIL  missing {path}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print("FAIL  sample file missing YAML front matter", file=sys.stderr)
        return 1

    parts = text.split("---", 2)
    if len(parts) < 3:
        print("FAIL  cannot parse front matter", file=sys.stderr)
        return 1
    fm, body = parts[1], parts[2]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    fm = replace_or_add(fm, "status", a.status)
    fm = replace_or_add(fm, "reviewed_at", now if a.status != "pending_review" else '""')
    fm = replace_or_add(fm, "review_source", "manual")
    fm = replace_or_add(fm, "llm_used", "false")
    fm = replace_or_add(fm, "review_mode", "manual")
    if a.note:
        fm = replace_or_add(fm, "reviewer_note", a.note)

    path.write_text(f"---{fm}---{body}", encoding="utf-8")
    print(f"OK  {path.relative_to(ROOT)} → status={a.status} (review_source=manual)")
    if a.status == "approved":
        print(
            "NOTE  manual approved does NOT unlock gas. "
            "register-miner-v2.sh re-runs auto_review+LLM; rejected/needs_human → no register.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
