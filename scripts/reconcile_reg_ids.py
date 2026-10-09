#!/usr/bin/env python3
"""
Recover the TRUE registration ID for every tx we logged, and check it on the live node.

Background: register scripts recorded minerCount() instead of the receipt event, so
43 IDs in out/*.jsonl are each claimed by two different txs (found 2026-10-07).
This re-reads every receipt and is read-only (no gas, no writes on-chain).

  python3 scripts/reconcile_reg_ids.py            # needs cast + RPC_URL/DIAMOND in .env
  python3 scripts/reconcile_reg_ids.py --no-node  # skip devnode probe

Writes out/RECONCILED_REG_IDS.json and out/RECONCILED_REG_IDS.md
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from reg_id_from_receipt import extract  # noqa: E402

NODE = os.environ.get("NODE_URL", "https://devnode.telegraphprotocol.com").rstrip("/")


def load_env() -> None:
    p = ROOT / ".env"
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def logged_rows() -> list[dict]:
    seen: dict[str, dict] = {}
    files = sorted(glob.glob(str(ROOT / "out" / "*.jsonl")) + glob.glob(str(ROOT / "out" / "*register*.json"))
                   + [str(ROOT / "out" / n) for n in ("last-registration.json", "last-registration-v2.json")])
    for f in files:
        try:
            txt = Path(f).read_text()
        except OSError:
            continue
        try:
            o = json.loads(txt)
            objs = o if isinstance(o, list) else [o]
        except Exception:
            objs = []
            for l in txt.splitlines():
                try:
                    objs.append(json.loads(l))
                except Exception:
                    pass
        for o in objs:
            if isinstance(o, dict) and o.get("tx_hash") and o.get("new_registration_id"):
                seen.setdefault(o["tx_hash"], {**o, "_log": Path(f).name})
    return list(seen.values())


def receipt(tx: str) -> dict:
    out = subprocess.run(["cast", "receipt", tx, "--json", "--rpc-url", os.environ["RPC_URL"]],
                         capture_output=True, text=True, timeout=60)
    if out.returncode:
        raise RuntimeError(out.stderr.strip()[:200])
    return json.loads(out.stdout)


def node_miner(rid: int) -> dict:
    try:
        with urllib.request.urlopen(f"{NODE}/api/miners/{rid}", timeout=20) as r:
            return (json.load(r) or {}).get("miner") or {}
    except Exception as e:
        return {"_error": str(e)[:120]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-node", action="store_true")
    a = ap.parse_args()
    load_env()
    for k in ("RPC_URL", "DIAMOND"):
        if not os.environ.get(k):
            sys.exit(f"{k} missing (.env)")
    rows = logged_rows()
    print(f"{len(rows)} logged txs")
    res = []
    for r in rows:
        slug = Path(r.get("yaml_file", "")).stem or r.get("slug", "?")
        mode = r.get("mode") or "register"
        item = {"slug": slug, "tx": r["tx_hash"], "logged_id": r["new_registration_id"],
                "yaml_url": r.get("yaml_url"), "log": r["_log"]}
        try:
            item["true_id"] = extract(receipt(r["tx_hash"]), os.environ["DIAMOND"], mode)
        except Exception as e:
            item["true_id"], item["error"] = None, str(e)
        if item["true_id"] and not a.no_node:
            m = node_miner(item["true_id"])
            item["node_status"] = m.get("activation_status") or m.get("_error")
            item["node_yaml_url"] = m.get("yaml_url")
            item["node_rejection"] = m.get("rejection_reason")
            item["yaml_url_matches"] = m.get("yaml_url") == r.get("yaml_url")
            time.sleep(0.15)
        item["id_was_wrong"] = item["true_id"] is not None and item["true_id"] != item["logged_id"]
        res.append(item)
        flag = "WRONG-ID" if item["id_was_wrong"] else "ok"
        print(f"  {flag:8} {slug:32} logged={item['logged_id']} true={item['true_id']} node={item.get('node_status')}")
    (ROOT / "out" / "RECONCILED_REG_IDS.json").write_text(json.dumps(res, indent=2) + "\n")
    wrong = [x for x in res if x["id_was_wrong"]]
    notlive = [x for x in res if x.get("node_status") not in (None, "active")]
    md = ["# Reconciled registration IDs", "",
          f"Logged txs: **{len(res)}** · wrong logged ID: **{len(wrong)}** · not active on node: **{len(notlive)}** · "
          f"receipt errors: **{sum(1 for x in res if x.get('error'))}**", "",
          "| Slug | Logged ID | True ID | Node status | YAML URL matches | Note |", "|---|---:|---:|---|---|---|"]
    for x in sorted(res, key=lambda x: (x["true_id"] or 0)):
        md.append(f"| `{x['slug']}` | {x['logged_id']} | {x['true_id']} | {x.get('node_status','')} | "
                  f"{x.get('yaml_url_matches','')} | {x.get('error') or x.get('node_rejection') or ''} |")
    (ROOT / "out" / "RECONCILED_REG_IDS.md").write_text("\n".join(md) + "\n")
    print(f"\nwrong IDs: {len(wrong)} · not active: {len(notlive)} -> out/RECONCILED_REG_IDS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
