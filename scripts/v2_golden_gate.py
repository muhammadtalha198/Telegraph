#!/usr/bin/env python3
"""
Optional golden-test gate for Semantic V2 (fail-closed when a suite exists).

Looks for candidate definitions in:
  - TeleGraph/files/candidates/*.json
  - MinerCreator/candidates/*.json

If the slug is present: run the same hard + check kinds as files/run_golden_tests.py
(for the candidate's first / listed tests). FAIL → do not register.

If no suite for this slug: SKIP (not a pass claim) — auto_review+LLM remains mandatory.

  python3 scripts/v2_golden_gate.py --sample apiOutputSamples/CRYPTO_PRICE/cp-binance.md
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import statistics
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
UA = "telegraph-v2-golden-gate/1"
BAD = [
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
    r"service unavailable",
]


def fill(s, vals):
    if isinstance(s, str):
        s = os.path.expandvars(s)
        return re.sub(r"\{(\w+)\}", lambda m: str(vals.get(m.group(1), m.group(0))), s)
    if isinstance(s, dict):
        return {k: fill(v, vals) for k, v in s.items()}
    if isinstance(s, list):
        return [fill(v, vals) for v in s]
    return s


def jpath(obj, path):
    cur = obj
    for part in path.split("."):
        try:
            cur = cur[int(part)] if isinstance(cur, list) else cur[part]
        except (KeyError, IndexError, ValueError, TypeError):
            return None
    return cur


def to_num(v):
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.strip()
        if re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", s):
            s = s.replace(",", "")
        m = re.search(r"-?\d+(?:\.\d+)?(?:[eE]-?\d+)?", s)
        return float(m.group(0)) if m else None
    return None


def call(c, vals, timeout=30):
    url = fill(c["url"], vals)
    hdrs = {"User-Agent": UA, "Accept": "*/*"}
    hdrs.update(fill(c.get("headers", {}), vals))
    data = None
    if c.get("body") is not None:
        data = json.dumps(fill(c["body"], vals)).encode()
        hdrs.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=data, headers=hdrs, method=c.get("method", "GET"))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace"), url
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), url
    except Exception as e:
        return None, str(e), url


def hard_fail(status, body, allow_html):
    if status != 200:
        return f"http {status}"
    t = body.strip()
    if not t or t in ("{}", "[]", "null"):
        return "empty body"
    if not allow_html:
        head = t[:500].lower()
        for pat in BAD:
            if re.search(pat, head, re.M):
                return f"error-like body ({pat})"
    try:
        o = json.loads(t)
        if isinstance(o, dict) and o.get("error") and len(o) <= 3:
            return "JSON error object"
    except Exception:
        pass
    return None


def extract(c, vals, body):
    ex = c.get("extract")
    if not ex:
        return None
    ex = fill(ex, vals)
    try:
        if ex.startswith("re:"):
            m = re.search(ex[3:], body, re.S)
            n = to_num(m.group(1)) if m else None
        elif ex.startswith("diff:"):
            a, b = ex[5:].split("|")
            o = json.loads(body)
            na, nb = to_num(jpath(o, a)), to_num(jpath(o, b))
            n = None if na is None or nb is None else na - nb
        elif ex.startswith("hex:"):
            v = jpath(json.loads(body), ex[4:])
            n = float(int(v, 16)) if isinstance(v, str) else None
        else:
            n = to_num(jpath(json.loads(body), ex))
    except Exception:
        return None
    return None if n is None else n * float(c.get("scale", 1))


def load_blocks() -> list[dict]:
    dirs = [
        REPO / "miner_pack" / "candidates",
        REPO / "files" / "candidates",
        ROOT / "candidates",
    ]
    blocks = []
    seen = set()
    for d in dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.json")):
            key = f.resolve()
            if key in seen:
                continue
            seen.add(key)
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    data = [data]
                blocks.extend(data)
            except Exception as e:
                print(f"WARN  bad candidates file {f}: {e}", file=sys.stderr)
    return blocks


def find_candidate(slug: str) -> tuple[dict, dict] | None:
    """Return (block, candidate) or None."""
    for b in load_blocks():
        for c in b.get("candidates") or []:
            if c.get("slug") == slug:
                return b, c
    return None


def parse_sample_meta(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    fm = text.split("---", 2)[1]
    out = {}
    for line in fm.splitlines():
        if ":" in line and re.match(r"^[a-z_]+:", line):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"')
    return out


def run_golden_for_slug(slug: str) -> tuple[str, str]:
    """
    Returns (status, message) where status is PASS | FAIL | SKIP.
    """
    found = find_candidate(slug)
    if not found:
        return "SKIP", "no golden suite for slug (candidates/*.json missing or slug absent)"
    block, cand = found
    if cand.get("needs_key") and not os.environ.get(cand["needs_key"]):
        return "FAIL", f"golden suite needs env {cand['needs_key']} unset"
    tests = {t["id"]: t for t in block.get("tests") or []}
    tids = cand.get("tests") or list(tests)
    if not tids:
        return "SKIP", "candidate has no tests listed"
    raw = {}
    for tid in tids:
        t = tests[tid]
        vals = dict(t.get("inputs") or {})
        vals.update({k + "_lower": str(v).lower() for k, v in vals.items()})
        vals.setdefault("today", datetime.date.today().isoformat())
        vals.setdefault(
            "tomorrow",
            (datetime.date.today() + datetime.timedelta(days=1)).isoformat(),
        )
        st, body, url = call(cand, vals)
        raw[tid] = dict(
            status=st,
            body=body,
            url=url,
            vals=vals,
            hard=hard_fail(st, body, cand.get("allow_html", False)),
            num=extract(cand, vals, body),
        )
        time.sleep(0.3)
    med = {}
    for tid, t in tests.items():
        chk = t.get("check") or {}
        if chk.get("kind") == "consensus":
            nums = [raw[x]["num"] for x in tids if x in raw and raw[x]["num"] is not None and not raw[x]["hard"]]
            # consensus needs peers — load all candidates for this test if possible
            peer_nums = []
            for c2 in block.get("candidates") or []:
                if c2.get("needs_key") and not os.environ.get(c2["needs_key"]):
                    continue
                st, body, _ = call(c2, dict(t.get("inputs") or {}))
                if hard_fail(st, body, c2.get("allow_html", False)):
                    continue
                n = extract(c2, dict(t.get("inputs") or {}), body)
                if n is not None:
                    peer_nums.append(n)
                time.sleep(0.2)
            med[tid] = statistics.median(peer_nums) if len(peer_nums) >= 3 else None

    why = []
    for tid in tids:
        r = raw[tid]
        chk = (cand.get("checks") or {}).get(tid, tests[tid]["check"])
        k = chk["kind"]
        reason = r["hard"]
        low = r["body"].lower()
        if not reason:
            if k == "golden_number":
                n = r["num"]
                if n is None:
                    reason = "could not extract number"
                elif abs(n - chk["value"]) > abs(chk["value"]) * chk.get("tol", 0.02):
                    reason = f"{n} != golden {chk['value']}"
            elif k == "consensus":
                n, m = r["num"], med.get(tid)
                if n is None:
                    reason = "could not extract number"
                elif m is None:
                    reason = "no consensus (<3 numeric answers)"
                elif m and abs(n - m) / abs(m) > chk.get("tol", 0.03):
                    reason = f"{n} vs median {m}"
            elif k == "contains_all":
                miss = [fill(v, r["vals"]) for v in chk["values"] if fill(v, r["vals"]).lower() not in low]
                if miss:
                    reason = f"missing {miss}"
            elif k == "contains_any":
                if not any(fill(v, r["vals"]).lower() in low for v in chk["values"]):
                    reason = f"none of {chk['values']}"
            elif k == "json_has":
                try:
                    o = json.loads(r["body"])
                    miss = [p for p in chk["paths"] if jpath(o, fill(p, r["vals"])) in (None, "", [], {})]
                    if miss:
                        reason = f"missing paths {miss}"
                except Exception:
                    reason = "not JSON"
            elif k == "nonempty":
                reason = None
        if reason:
            why.append(f"{tid}: {reason}")
    if why:
        return "FAIL", "; ".join(why)[:300]
    return "PASS", f"passed {len(tids)} golden test(s)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=Path, required=True)
    ap.add_argument("--slug", default="")
    a = ap.parse_args()
    path = a.sample if a.sample.is_absolute() else ROOT / a.sample
    meta = parse_sample_meta(path) if path.is_file() else {}
    slug = a.slug or meta.get("slug") or path.stem
    status, msg = run_golden_for_slug(slug)
    print(f"golden_gate  {status}  slug={slug}  {msg}")
    if status == "FAIL":
        return 1
    return 0  # PASS or SKIP


if __name__ == "__main__":
    raise SystemExit(main())
