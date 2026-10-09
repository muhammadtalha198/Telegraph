---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-linea-root
status: pending_review
captured_at: 2026-10-05T09:28:52Z
request_url: https://rpc.linea.build
content_type: application/json
inputs: |
  {}
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must return verifiable state roots / cross-chain message status between networks.
capture_note: |
  golden-test PASS: Linea
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "baseFeePerGas": "0x7",
    "blobGasUsed": "0x0",
    "difficulty": "0x0",
    "excessBlobGas": "0x0",
    "extraData": "0x0100007530000f42400000a3b000000000000000000000000000000000000000",
    "gasLimit": "0x77359400",
    "gasUsed": "0x1f2f5",
    "hash": "0xeec118ad2d16eebfd5fe3e6f77ec238b9a929a005a77c226021b0fec13d96c2e",
    "logsBloom": "0x00000000000000000000000000100000000100000000000000000200000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000400040000000000000000000200200000000000010000000000000000000000000000100000000000000000000000000000000000000400000000000000000000000000004000000000000000000000000000000000000100000000000000080000000000000000000000000000000000000000000000020008000000000040000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "miner": "0xfd5fb23e06e46347d8724486cdb681507592e237",
    "mixHash": "0xff05c1faa76fd86cca11e822d551971b8125ac7db94455f9e1845ffbd4f31e08",
    "nonce": "0x0000000000000000",
    "number": "0x1ebe187",
    "parentBeaconBlockRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "parentHash": "0x6e87a14c3e4bfb13a0f62fa40d2d35d733f6be232c03994c6a020e0001159da2",
    "receiptsRoot": "0x015745b710ecc8816af449a44e5dcd4559c72974a3644af3df3ec42cac940767",
    "requestsHash": "0xe3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x769",
    "stateRoot": "0x53269d3cb008a4c28dca0cc074527cf7d7156030a57dcde3fa45d0a1a9ab1719",
    "timestamp": "0x6ac36dc1",
    "transactions": [
      "0xa329b167d39433e366f2aded949a5c2bd3a920299919d6c63eb540f2279f5306"
    ],
    "transactionsRoot": "0xbd6846dbe72a4f1f0fcc89678282dc4dab43329d1e6e80df81d72e7d0cc88e85",
    "uncles": [],
    "withdrawals": [],
    "withdrawalsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
