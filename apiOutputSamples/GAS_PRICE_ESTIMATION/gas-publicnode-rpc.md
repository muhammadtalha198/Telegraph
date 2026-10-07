---
intent: GAS_PRICE_ESTIMATION
slug: gas-publicnode-rpc
status: approved
captured_at: 2026-10-05T09:28:27Z
request_url: https://ethereum-rpc.publicnode.com
content_type: application/json
inputs: |
  {}
intent_description: |
  Estimates dynamic base fee, tip priority, and gas limits across standard transaction speed tiers.
answer_requirement: |
  Must return the current Ethereum gas price / fee estimate.
capture_note: |
  golden-test PASS: PublicNode ETH RPC
reviewer_note: "auto_review: [1.00|heuristic+llm] API response provided the current gas price in hexadecimal format."
reviewed_at: 2026-10-05T12:38:46Z
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
  "result": "0x6f81cfd"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] API response provided the current gas price in hexadecimal format._
