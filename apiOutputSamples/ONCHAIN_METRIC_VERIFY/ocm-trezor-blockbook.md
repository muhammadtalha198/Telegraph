---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-trezor-blockbook
status: approved
captured_at: 2026-10-05T09:28:17Z
request_url: https://btc1.trezor.io/api/v2/address/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa?details=basic
content_type: application/json
inputs: |
  {"addr": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: Trezor Blockbook
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the on-chain balance for the specified address. | heuristic: Returns wallet/token balance (partial vs full logs/gas description)"
reviewed_at: 2026-10-05T11:49:14Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
  "balance": "10758434552",
  "totalReceived": "10758434552",
  "totalSent": "0",
  "unconfirmedTxs": 13,
  "txs": 66820
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the on-chain balance for the specified address. | heuristic: Returns wallet/token balance (partial vs full logs/gas description)_
