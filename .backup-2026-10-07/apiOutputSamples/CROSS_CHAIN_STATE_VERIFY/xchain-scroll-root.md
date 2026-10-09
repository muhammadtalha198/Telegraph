---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-scroll-root
status: pending_review
captured_at: 2026-10-05T09:28:52Z
request_url: https://rpc.scroll.io
content_type: application/json
inputs: |
  {}
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must return verifiable state roots / cross-chain message status between networks.
capture_note: |
  golden-test PASS: Scroll
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x1d4c8",
    "difficulty": "0x1",
    "extraData": "0x",
    "gasLimit": "0x1312d00",
    "gasUsed": "0x9412",
    "hash": "0xdc016bef36174b066bf892ba2294528700ae30145fba8734672d43ac9eef5d34",
    "logsBloom": "0x00000000000000000000000040000000000000000200000000000000000000000000000000000000000000000000000080000000002000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000040000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000400000000000000000200000000000000000000000010000000000000000000000000000000000000000080000000000008000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x21a5ae1",
    "parentHash": "0x8a83513ece524d25ad2f3c7cb2bea0d08ad4749c4b72fdaf52b6b39215073b4e",
    "receiptsRoot": "0x5b05a89ce650c2206a761f579fcdde1155b8e67ceab943bf92cd5f79c22e26b2",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x2fd",
    "stateRoot": "0xffadf0eed193d36d4f152c0c49784a90feb0412aa140c94725f227b3d63a7202",
    "timestamp": "0x6ac36db0",
    "totalDifficulty": "0x2fdd131",
    "transactions": [
      "0xee64b10585f6c4943955647d09c68912bbdc3f4ad19da5396855b4e47237d5ec"
    ],
    "transactionsRoot": "0x383d1a81f68d64a1372ad68362511d1b0d88f0b96f71796c30cafbafadbe39a9",
    "uncles": []
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
