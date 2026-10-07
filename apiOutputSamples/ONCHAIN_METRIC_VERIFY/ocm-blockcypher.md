---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-blockcypher
status: pending_review
captured_at: 2026-10-05T09:28:17Z
request_url: https://api.blockcypher.com/v1/btc/main/addrs/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa/balance
content_type: application/json
inputs: |
  {"addr": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must return the on-chain value asked (address balance / token balance / tx state).
capture_note: |
  golden-test PASS: BlockCypher
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
  "total_received": 10758434552,
  "total_sent": 0,
  "balance": 10758434552,
  "unconfirmed_balance": 0,
  "final_balance": 10758434552,
  "n_tx": 66820,
  "unconfirmed_n_tx": 0,
  "final_n_tx": 66820
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
