#!/usr/bin/env python3
"""
Extract the registration ID from a `cast send --json` receipt (stdin).

Why: register scripts used to read `minerCount()` AFTER the tx. That returns the
wrong ID whenever the RPC is a block behind or anyone else registers in the same
window — PACK_V2_REGISTER.jsonl has 25 IDs recorded twice for different slugs.
The receipt's own event log is the only authoritative source.

  cast send ... --json | python3 scripts/reg_id_from_receipt.py --diamond 0x... --mode register
  -> prints the ID; exit 1 if tx reverted or the event is missing (fail closed).

Topics (keccak256 of the signatures in Telegraph/contracts/evm/facets/MinerRegistryFacet.sol):
"""
from __future__ import annotations

import argparse
import json
import sys

# MinerRegistered(uint256 indexed registrationId, address indexed miner, string, bytes32, address, uint256, string[])
TOPIC_REGISTERED = "0x7305b0d0f2fed40b03fb6b42dfaa5d50920aa0312578b5ed482f1072942823a4"
# MinerUpdated(uint256 indexed oldRegistrationId, uint256 indexed newRegistrationId, address indexed miner)
TOPIC_UPDATED = "0x730a714c2daeaccdb38464c13f0fc5dcdf8240b5c8c3e9b61d502407b61613e0"


def extract(receipt: dict, diamond: str, mode: str) -> int:
    status = str(receipt.get("status", "")).lower()
    if status not in ("0x1", "1", "true"):
        raise ValueError(f"tx not successful (status={status!r}) — registration did NOT happen")
    want = TOPIC_UPDATED if mode == "update" else TOPIC_REGISTERED
    idx = 2 if mode == "update" else 1  # update: topics[2] = newRegistrationId
    hits = []
    for log in receipt.get("logs") or []:
        if str(log.get("address", "")).lower() != diamond.lower():
            continue
        topics = [str(t).lower() for t in log.get("topics") or []]
        if topics and topics[0] == want and len(topics) > idx:
            hits.append(int(topics[idx], 16))
    if len(hits) != 1:
        raise ValueError(f"expected exactly one {mode} event from {diamond}, found {len(hits)}")
    return hits[0]


def _self_test() -> int:
    d = "0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8"
    other = "0x" + "11" * 20
    def lg(addr, *topics):
        return {"address": addr, "topics": list(topics), "data": "0x"}
    pad = lambda n: "0x" + format(n, "064x")
    ok_reg = {"status": "0x1", "logs": [
        lg(other, TOPIC_REGISTERED, pad(9999)),            # foreign contract, ignored
        lg(d, "0x" + "ab" * 32, pad(1)),                    # IntentRegistered etc., ignored
        lg(d, TOPIC_REGISTERED, pad(4564), pad(0xBEEF))]}
    ok_upd = {"status": "0x1", "logs": [lg(d, TOPIC_UPDATED, pad(4383), pad(4701), pad(0xBEEF))]}
    reverted = {"status": "0x0", "logs": []}
    no_event = {"status": "0x1", "logs": [lg(d, "0x" + "ab" * 32)]}
    checks = []
    checks.append(extract(ok_reg, d, "register") == 4564)
    checks.append(extract(ok_upd, d, "update") == 4701)
    for bad in (reverted, no_event):
        try:
            extract(bad, d, "register"); checks.append(False)
        except ValueError:
            checks.append(True)
    print("SELF-TEST", "PASS" if all(checks) else f"FAIL {checks}")
    return 0 if all(checks) else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--diamond")
    ap.add_argument("--mode", choices=("register", "update"), default="register")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return _self_test()
    if not a.diamond:
        ap.error("--diamond required")
    try:
        print(extract(json.load(sys.stdin), a.diamond, a.mode))
        return 0
    except Exception as e:  # fail closed
        print(f"reg_id_from_receipt: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
