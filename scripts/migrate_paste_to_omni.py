#!/usr/bin/env python3
"""
Move paste.rs-hosted miners to our Omni nginx host.

WHY: paste.rs accepts unauthenticated `DELETE https://paste.rs/<id>`, and every yaml_url is
public on-chain — anyone can take our miners down. 164 registrations were hosted there.

Stages (each one safe to re-run):
  backup   no gas  download every paste.rs YAML, verify sha256 == on-chain yaml_hash,
                   save to out/paste_backup/<slug>-<id>.yaml   <- RUN THIS FIRST, TODAY
  rehost   no gas  scp those exact bytes to omni (same hash), verify public byte-match
  repoint  GAS     updateMiner(id, omni_url, same hash, same fee/price/intents); dry-run
                   unless --execute. New ID read from the receipt (reg_id_from_receipt).

Source of truth for IDs: out/RECONCILED_REG_IDS.json (run reconcile_reg_ids.py first),
then on-chain getMiner(id) for hash/fee/price/intents/active (node /api/miners is often 403).

  python3 scripts/migrate_paste_to_omni.py backup
  python3 scripts/migrate_paste_to_omni.py rehost
  python3 scripts/migrate_paste_to_omni.py repoint             # dry-run: prints the txs
  python3 scripts/migrate_paste_to_omni.py repoint --execute --limit 5
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from reconcile_reg_ids import load_env, logged_rows  # noqa: E402
from reg_id_from_receipt import extract  # noqa: E402

BACKUP = ROOT / "out" / "paste_backup"
LOG = ROOT / "out" / "PASTE_MIGRATION.jsonl"
UA = {"User-Agent": "Go-http-client/1.1"}
GET_MINER = "getMiner(uint256)(address,string,bytes32,bool,bytes32,address,uint256,string[])"


def chain_miner(rid: int) -> dict:
    """On-chain miner record — preferred over node HTTP (devnode often 403)."""
    out = subprocess.run(
        ["cast", "call", os.environ["DIAMOND"], GET_MINER, str(rid),
         "--rpc-url", os.environ["RPC_URL"], "--json"],
        capture_output=True, text=True, timeout=60,
    )
    if out.returncode:
        return {"_error": (out.stderr or out.stdout)[:200]}
    try:
        miner, yaml_url, yaml_hash, active, _intent, fee, price, intents = json.loads(out.stdout)
    except Exception as e:
        return {"_error": f"parse: {e}: {out.stdout[:120]}"}
    return {
        "yaml_url": yaml_url,
        "yaml_hash": str(yaml_hash).lower().removeprefix("0x"),
        "active": bool(active),
        "fee_address": fee,
        "min_price_usdc": int(price),
        "supported_intents": list(intents),
    }


def targets() -> list[dict]:
    p = ROOT / "out" / "RECONCILED_REG_IDS.json"
    if not p.exists():
        sys.exit("run scripts/reconcile_reg_ids.py first (true IDs needed)")
    rows = [r for r in json.loads(p.read_text()) if r.get("true_id")]
    out = []
    for r in rows:
        m = chain_miner(int(r["true_id"]))
        if m.get("_error"):
            print(f"  SKIP {r['slug']}: getMiner {m['_error']}")
            continue
        url = m.get("yaml_url") or ""
        if "paste.rs" not in url:
            continue
        if not m.get("active"):
            print(f"  SKIP {r['slug']}: on-chain inactive (id={r['true_id']})")
            continue
        out.append({
            **r,
            "yaml_url": url,
            "yaml_hash": m["yaml_hash"],
            "fee_address": m["fee_address"],
            "min_price_usdc": m["min_price_usdc"],
            "supported_intents": m["supported_intents"],
        })
        time.sleep(0.05)
    return out


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read()


def _h(r: dict) -> str:
    return str(r.get("yaml_hash") or "").lower().removeprefix("0x")


def backup_path(r: dict) -> Path:
    # content-addressed: never collides with legacy omni <slug>.yaml files
    return BACKUP / f"{r['slug']}-{_h(r)[:8]}.yaml"


def logged_paste_rows() -> list[dict]:
    """Backup needs no RPC: every paste.rs URL + its registered hash straight from out/*.jsonl."""
    out, seen = [], set()
    for o in logged_rows():
        u = o.get("yaml_url") or ""
        if "paste.rs" in u and u not in seen:
            seen.add(u)
            out.append({"slug": Path(o.get("yaml_file", "")).stem or o.get("slug", "x"),
                        "yaml_url": u, "yaml_hash": _h(o)})
    return out


def log(ev: dict) -> None:
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps({**ev, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}) + "\n")


def do_backup(rows: list[dict]) -> int:
    BACKUP.mkdir(parents=True, exist_ok=True)
    bad = unverified = 0
    for r in rows:
        want = _h(r)
        if want and backup_path(r).exists():
            continue
        try:
            body = fetch(r["yaml_url"])
        except Exception as e:
            print(f"  UNREACHABLE {r['slug']:27} {e}")
            bad += 1
            continue
        got = hashlib.sha256(body).hexdigest()
        if want and got != want:
            print(f"  HASH!  {r['slug']:32} paste bytes != registered hash (tampered or replaced?)")
            bad += 1
            continue
        if not want:  # log row had no hash: keep the bytes, verify against the node later (rehost does)
            r["yaml_hash"] = got
            unverified += 1
        backup_path(r).write_bytes(body)
        print(f"  saved  {r['slug']:32} {r['yaml_url']}{'  (hash not in log — unverified)' if not want else ''}")
        time.sleep(0.2)
    print(f"\nbackup: {len(rows) - bad}/{len(rows)} saved to {BACKUP} ({unverified} unverified)")
    return 1 if bad else 0


def ssh(*args: str) -> None:
    key = os.environ.get("OMNI_SSH_KEY") or sys.exit("OMNI_SSH_KEY not set")
    opt = ["-i", key, "-o", "StrictHostKeyChecking=accept-new", "-o", "ConnectTimeout=15"]
    subprocess.run(args[0:1] + tuple(opt) + args[1:], check=True)


def omni_url(r: dict) -> str:
    prefix = os.environ.get("HOST_PREFIX_CHAT", "").rstrip("/") or sys.exit("HOST_PREFIX_CHAT not set")
    return f"{prefix}/{backup_path(r).name}"


def do_rehost(rows: list[dict]) -> int:
    target = os.environ.get("OMNI_SSH_TARGET", "ubuntu@13.237.89.59")
    d = os.environ.get("OMNI_YAML_DIR", "/var/www/miner-yamls")
    files = [backup_path(r) for r in rows if backup_path(r).exists()]
    if not files:
        sys.exit("nothing backed up yet — run `backup` first")
    ssh("ssh", target, "mkdir -p /tmp/paste_mig")
    ssh("scp", "-q", *map(str, files), f"{target}:/tmp/paste_mig/")
    ssh("ssh", target, f"sudo install -m 0644 /tmp/paste_mig/*.yaml {d}/ && rm -rf /tmp/paste_mig")
    bad = 0
    for r in rows:
        if not backup_path(r).exists():
            continue
        ok = fetch(omni_url(r)) == backup_path(r).read_bytes()
        bad += not ok
        print(f"  {'ok  ' if ok else 'MISMATCH'} {omni_url(r)}")
    print(f"\nrehost: {len(files) - bad}/{len(files)} byte-identical on omni")
    return 1 if bad else 0


def do_repoint(rows: list[dict], execute: bool, limit: int) -> int:
    done = {json.loads(l)["old_id"] for l in LOG.read_text().splitlines() if '"repointed"' in l} if LOG.exists() else set()
    todo = [r for r in rows if r["true_id"] not in done and backup_path(r).exists()][: limit or None]
    for r in todo:
        url = omni_url(r)
        body = backup_path(r).read_bytes()
        try:
            remote = fetch(url)
        except Exception as e:
            print(f"  SKIP {r['slug']}: omni fetch failed ({e}) — run rehost")
            continue
        if remote != body:
            print(f"  SKIP {r['slug']}: omni copy missing/mismatched — run rehost")
            continue
        got = hashlib.sha256(body).hexdigest()
        want = _h(r)
        if want and got != want:
            print(f"  SKIP {r['slug']}: backup hash != on-chain yaml_hash")
            continue
        h = "0x" + got
        args = [str(r["true_id"]), url, h, r["fee_address"], str(r["min_price_usdc"]),
                json.dumps(r["supported_intents"])]
        print(f"  updateMiner({', '.join(args)})")
        if not execute:
            continue
        out = subprocess.run(["cast", "send", os.environ["DIAMOND"],
                              "updateMiner(uint256,string,bytes32,address,uint256,string[])", *args,
                              "--rpc-url", os.environ["RPC_URL"], "--private-key", os.environ["MINER_PRIVATE_KEY"],
                              "--json"], capture_output=True, text=True)
        if out.returncode:
            print(f"    FAIL {out.stderr.strip()[:200]}")
            log({"event": "failed", "slug": r["slug"], "old_id": r["true_id"], "err": out.stderr[:300]})
            return 1
        rec = json.loads(out.stdout)
        new_id = extract(rec, os.environ["DIAMOND"], "update")
        log({"event": "repointed", "slug": r["slug"], "old_id": r["true_id"], "new_id": new_id,
             "yaml_url": url, "tx": rec.get("transactionHash")})
        print(f"    OK new id {new_id}")
        time.sleep(1.5)
    if not execute:
        print(f"\nDRY RUN — {len(todo)} updateMiner txs listed. Re-run with --execute to send.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=("backup", "rehost", "repoint"))
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    load_env()
    if a.stage == "backup":
        rows = logged_paste_rows()
        print(f"{len(rows)} paste.rs YAMLs in register logs")
        return do_backup(rows)
    rows = targets()
    print(f"{len(rows)} active miners hosted on paste.rs")
    if a.stage == "rehost":
        return do_rehost(rows)
    return do_repoint(rows, a.execute, a.limit)


if __name__ == "__main__":
    sys.exit(main())
