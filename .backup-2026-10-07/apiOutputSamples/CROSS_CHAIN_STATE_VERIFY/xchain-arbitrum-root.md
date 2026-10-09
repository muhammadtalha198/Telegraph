---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-arbitrum-root
status: approved
captured_at: 2026-10-05T09:28:52Z
request_url: https://arb1.arbitrum.io/rpc
content_type: application/json
inputs: |
  {}
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must return verifiable state roots / cross-chain message status between networks.
capture_note: |
  golden-test PASS: Arbitrum One
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the base fee per gas as requested."
reviewed_at: 2026-10-05T12:12:58Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "baseFeePerGas": "0x1312d00",
    "difficulty": "0x1",
    "extraData": "0x5415fe5b5fa72ff4ecaf578e7346f9ef8942c832a0f5564f05d8511e3576b334",
    "gasLimit": "0x4000000000000",
    "gasUsed": "0x3d721",
    "hash": "0x9f2a4542dcd73b3b7312c2b57ebf79e61dbcd36906c7e8ed500f56ea199fa803",
    "l1BlockNumber": "0x18ea3d7",
    "logsBloom": "0x00001000000000000000000008000000000000000004000000000000000000000000000000000000000080000000000000080201000020100000000000000000000000000200000840000408000000000000000010000040002000000000000000800000000000000000000004100000000000000000000000000012000800000000000000000000000000000001000000000400000000000000001000000000000000000000000000000000000004000000000200000000008000000000000000002002000040200000000000000000000000000000000000000000000000000000200000000000000000000000200000000000000000000000000020000000",
    "miner": "0xa4b000000000000000000073657175656e636572",
    "mixHash": "0x0000000000028aef00000000018ea3d7000000000000003d0001000000000000",
    "nonce": "0x00000000002770e4",
    "number": "0x1e82b4ad",
    "parentHash": "0xa31635fa277ca0ea0481d09fc59d1ca55b84b2a12e6c04384ce7532962b8b698",
    "receiptsRoot": "0x4bbc51c714c0499f97f4a4473864495eff600e521f9848f47a935b6c6422d82f",
    "sendCount": "0x28aef",
    "sendRoot": "0x5415fe5b5fa72ff4ecaf578e7346f9ef8942c832a0f5564f05d8511e3576b334",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x502",
    "stateRoot": "0x0af9d8afcffe1a8edabe67d676b274dc5642ccfbe938b935cab5a245bfc4b2da",
    "timestamp": "0x6ac36dbd",
    "transactions": [
      "0x6d7794b53cf25759c2824c31ee11fc2a682b0fbe69c6bf0da6335b440352e727",
      "0x8b2a0a41fac59f0ccbd3a446f0d8e9da2f57f05e39969c0cc6ae77a980db55e9",
      "0x8d7fd7cdace604327b7a28a4a31a1482e31eec0a727a7d69d1097d2fa53c023c",
      "0x71b35fa3abbd64420b404d77068394f7db2f868b80b224b1615628066f28ce1d"
    ],
    "transactionsRoot": "0x21cd50773adc2f667e9862eb9da63da3644a0c3631931681d00972a7ef350e74",
    "uncles": []
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the base fee per gas as requested._
