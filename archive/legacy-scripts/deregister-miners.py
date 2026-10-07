#!/usr/bin/env python3
"""Deregister miners by registration id (batches)."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
LOG = OUT / "deregister.jsonl"
IDS_FILE = OUT / "deregister-active-ids.json"


def load_env() -> dict[str, str]:
    env = dict(os.environ)
    for line in (ROOT / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env.setdefault(k.strip(), v.strip())
    return env


def cast_out(cmd: list[str]) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "")[-800:])
    return (p.stdout or "").strip()


def done_ids() -> set[int]:
    done = set()
    if LOG.exists():
        for line in LOG.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if r.get("status") == "deregistered":
                done.add(int(r["registration_id"]))
    return done


def append(row: dict) -> None:
    with LOG.open("a") as f:
        f.write(json.dumps(row) + "\n")


def deregister_one(env: dict, reg_id: int) -> tuple[str, str]:
    diamond = env.get("DIAMOND", "0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8")
    rpc = env.get("RPC_URL", "https://sepolia.base.org")
    pk = env["MINER_PRIVATE_KEY"]
    addr = cast_out(["cast", "wallet", "address", "--private-key", pk])

    last = ""
    for attempt in range(1, 6):
        nonce = cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
        cmd = [
            "cast", "send", diamond, "deregisterMiner(uint256)", str(reg_id),
            "--rpc-url", rpc, "--private-key", pk, "--nonce", nonce, "--json",
        ]
        p = subprocess.run(cmd, capture_output=True, text=True)
        raw = ((p.stdout or "") + "\n" + (p.stderr or "")).strip()
        if p.returncode != 0:
            last = raw[-800:]
            low = last.lower()
            if "already deregistered" in low or "not found" in low:
                return "", "already_gone"
            if any(x in low for x in ("nonce too low", "already known", "underpriced", "nonce too high")):
                time.sleep(2 * attempt)
                continue
            raise RuntimeError(last)
        start = raw.find("{")
        payload = json.loads(raw[start: raw.rfind("}") + 1])
        tx = payload.get("transactionHash") or ""
        status = str(payload.get("status", ""))
        for _ in range(40):
            cur = cast_out(["cast", "nonce", addr, "--rpc-url", rpc]).split()[0]
            if int(cur) > int(nonce):
                break
            time.sleep(0.4)
        return tx, status
    raise RuntimeError(last)


def main() -> int:
    env = load_env()
    ids = json.loads(IDS_FILE.read_text())
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    done = done_ids()
    pending = [i for i in ids if i not in done]
    if limit is not None:
        pending = pending[:limit]
    print(f"Deregistering {len(pending)} (skipping {len(done)} done / total {len(ids)})")
    for n, rid in enumerate(pending, 1):
        try:
            tx, status = deregister_one(env, rid)
            if status == "already_gone":
                append({"registration_id": rid, "status": "deregistered", "note": "already_gone"})
                print(f"[{n}/{len(pending)}] GONE {rid}")
            else:
                ok = status in ("0x1", "1", "0x01")
                append({
                    "registration_id": rid,
                    "tx_hash": tx,
                    "tx_status": status,
                    "status": "deregistered" if ok else "tx_failed",
                    "tx_url": f"https://sepolia.basescan.org/tx/{tx}",
                })
                print(f"[{n}/{len(pending)}] {'OK' if ok else 'FAIL'} {rid} tx={tx[:12]}…")
        except Exception as e:
            append({"registration_id": rid, "status": "failed", "error": str(e)[:500]})
            print(f"[{n}/{len(pending)}] FAIL {rid}: {e}")
            time.sleep(2)
            continue
        time.sleep(0.6)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
