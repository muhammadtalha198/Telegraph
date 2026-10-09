---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-blockchain-info
status: rejected
captured_at: 2026-10-05T09:28:17Z
request_url: https://blockchain.info/q/addressbalance/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
content_type: application/json
inputs: |
  {"addr": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: Blockchain.com
reviewer_note: "auto_review: [0.75|heuristic] no balance / on-chain value field found"
reviewed_at: 2026-10-05T09:43:40Z
review_source: auto_review
review_mode: heuristic
llm_used: false
review_confidence: 0.750
---

## Raw API output

```json
10758435098
```

## Why this matches (or not)

_[0.75|heuristic] no balance / on-chain value field found_
