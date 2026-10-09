---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-haskoin
status: pending_review
captured_at: 2026-10-05T09:28:17Z
request_url: https://api.haskoin.com/btc/address/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa/balance
content_type: application/json
inputs: |
  {"addr": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: Haskoin Store
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
  "confirmed": 10758434552,
  "unconfirmed": 546,
  "utxo": 80252,
  "txs": 66821,
  "received": 10758435098
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
