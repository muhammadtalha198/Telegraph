#!/usr/bin/env python3
"""
Shared-pin check (Usman 2026-10-06): miners ranked against each other for one intent
must answer ONE question. LLM-normalize fixes output shape, not different questions.

For every intent, compares each miner's default ask (input_schema defaults minus the
venue/routing param). Different defaults = `diff-question` = not rankable.

  python3 scripts/pin_consistency_check.py                  # report, all intents
  python3 scripts/pin_consistency_check.py --intent AIR_QUALITY_INDEX
  python3 scripts/pin_consistency_check.py --file new.yaml  # gate: exit 1 if new miner's
                                                            # pin differs from its intent's
                                                            # locked pin (shared_pins.json)
Locked pins live in shared_pins.json (intent -> {param: value}).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PINS = ROOT / "shared_pins.json"
ROUTING = {"venue", "provider", "source", "network", "model", "engine"}  # which-miner params, not the question


def ask_of(doc: dict) -> dict:
    props = ((doc.get("input_schema") or {}).get("properties")) or {}
    return {k: v.get("default") for k, v in props.items()
            if isinstance(v, dict) and k not in ROUTING and "default" in v}


def intents_of(doc: dict) -> list[str]:
    return list(((doc.get("semantics") or {}).get("supported_intents")) or [])


def scan() -> dict[str, list[tuple[str, dict]]]:
    by = defaultdict(list)
    for f in sorted((ROOT / "intentYamls").rglob("*.yaml")):
        try:
            doc = yaml.safe_load(f.read_text())
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        for it in intents_of(doc):
            by[it].append((doc.get("slug") or f.stem, ask_of(doc)))
            PUB[(it, doc.get("slug") or f.stem)] = publisher_of(doc)
    return by


PUB: dict[tuple[str, str], str] = {}


_PROXY_HOSTS = ("omni-chat.13.237.89.59.sslip.io",)
_SLD = {"co", "com", "gov", "org", "net", "ac", "edu"}


def publisher_of(doc: dict) -> str:
    """Upstream publisher identity. Proxy miners: route + venue. Direct: registrable domain."""
    from urllib.parse import urlparse
    host = (urlparse(str(doc.get("base_url") or "")).hostname or "").lower()
    if host in _PROXY_HOSTS:
        ep = (doc.get("endpoints") or [{}])[0] or {}
        props = ((doc.get("input_schema") or {}).get("properties")) or {}
        venue = (props.get("venue") or {}).get("default") if isinstance(props.get("venue"), dict) else None
        return f"proxy:{ep.get('external_path', '')}:{venue or '?'}"
    parts = host.split(".")
    n = 3 if len(parts) >= 3 and parts[-2] in _SLD and len(parts[-1]) == 2 else 2
    return ".".join(parts[-n:])


def load_pins() -> dict:
    d = json.loads(PINS.read_text()) if PINS.exists() else {}
    return {k: v for k, v in d.items() if not k.startswith("_")}


def verdict(rows: list[tuple[str, dict]], locked: dict | None) -> tuple[str, list[str]]:
    if len(rows) < 2:
        return "single", []
    if locked:
        off = [s for s, a in rows if any(str(a.get(k)) != str(v) for k, v in locked.items())]
        return ("pinned" if not off else "off-pin"), off
    asks = {json.dumps(a, sort_keys=True) for _, a in rows}
    return ("same-question" if len(asks) == 1 else "diff-question"), []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--intent")
    ap.add_argument("--file", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--same-source", action="store_true", help="list intents with >1 miner from one publisher")
    ap.add_argument("--fixed", action="store_true",
                    help="list miners with NO question params (question hard-coded in path) in multi-miner intents")
    a = ap.parse_args()
    pins = load_pins()

    if a.file:  # register gate
        doc = yaml.safe_load(a.file.read_text())
        bad = []
        for it in intents_of(doc):
            lock = pins.get(it)
            if not lock:
                continue
            ask = ask_of(doc)
            diff = {k: (ask.get(k), v) for k, v in lock.items() if str(ask.get(k)) != str(v)}
            if diff:
                bad.append(f"{it}: default ask {diff} != locked shared pin (shared_pins.json)")
        by = scan()
        me, pub = doc.get("slug"), publisher_of(doc)
        same_slug = []
        for p in (ROOT / "intentYamls").rglob("*.yaml"):
            if p.resolve() == a.file.resolve():
                continue
            try:
                other = yaml.safe_load(p.read_text()) or {}
            except yaml.YAMLError:
                # One broken file elsewhere must not crash this gate with a traceback.
                print(f"WARN  {p} does not parse; skipped in the duplicate-slug scan")
                continue
            if isinstance(other, dict) and other.get("slug") == me:
                same_slug.append(str(p))
        if same_slug:
            bad.append(f"slug `{me}` already used by {', '.join(same_slug)} — node rejects duplicate slugs")
        for it in intents_of(doc):
            twins = [s for s, _ in by.get(it, []) if s != me and PUB.get((it, s)) == pub]
            if twins:
                bad.append(f"{it}: same publisher `{pub}` as {', '.join(twins)} — one miner per source (Usman)")
        for b in bad:
            print("FAIL", b)
        if not bad:
            print("PASS shared pin + distinct publisher")
        return 1 if bad else 0

    by = scan()
    if a.same_source:
        n = 0
        for it in sorted(by):
            groups = defaultdict(list)
            for slug, _ in by[it]:
                groups[PUB[(it, slug)]].append(slug)
            for pub, slugs in sorted(groups.items()):
                if len(slugs) > 1:
                    n += len(slugs) - 1
                    print(f"{it:30} {pub:42} {len(slugs)}x  {', '.join(slugs)}")
        print(f"\n{n} extra miners share a publisher with another miner on the same intent")
        return 0
    if a.fixed:
        n = 0
        for it in sorted(by):
            fixed = [s for s, ask in by[it] if not ask]
            if len(by[it]) > 1 and fixed:
                n += len(fixed)
                print(f"{it:34} {len(fixed)}/{len(by[it])} fixed-question: {', '.join(fixed)}")
        print(f"\n{n} miners cannot take the scorer's question (path-baked); they only answer when the generated question happens to match")
        return 0
    out = {}
    for it in sorted(by):
        if a.intent and it != a.intent:
            continue
        v, off = verdict(by[it], pins.get(it))
        out[it] = {"verdict": v, "miners": len(by[it]), "off_pin": off,
                   "asks": {s: ask for s, ask in by[it]}}
    if a.json:
        print(json.dumps(out, indent=2))
        return 0
    order = {"diff-question": 0, "off-pin": 1, "pinned": 2, "same-question": 3, "single": 4}
    for it, r in sorted(out.items(), key=lambda kv: (order[kv[1]["verdict"]], kv[0])):
        print(f"{r['verdict']:14} {it:34} {r['miners']:>3} miners")
        if r["verdict"] in ("diff-question", "off-pin") or a.intent:
            for s, ask in r["asks"].items():
                mark = "  x" if s in r["off_pin"] else "   "
                print(f"   {mark} {s:30} {ask}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
