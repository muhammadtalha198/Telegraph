---
intent: MINING_HASHPRICE_VERIFY
slug: hash-blockchain-stats
status: pending_review
captured_at: 2026-10-05T09:41:44Z
request_url: https://api.blockchain.info/stats
content_type: application/json
inputs: |
  {}
intent_description: |
  Calculates instantaneous proof-of-work mining revenue per unit of hashing power based on block rewards and network difficulty.
answer_requirement: |
  Must return mining revenue per unit of hashrate (hashprice) or the inputs to compute it.
capture_note: |
  golden-test PASS: Blockchain.com stats
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "timestamp": 1791193160000.0,
  "market_price_usd": 86303.18,
  "hash_rate": 1095159811329.552,
  "total_fees_btc": -51875000000,
  "n_btc_mined": 51875000000,
  "n_tx": 872969,
  "n_blocks_mined": 166,
  "minutes_between_blocks": 8.1697,
  "totalbc": 2009371875000000,
  "n_blocks_total": 969990,
  "estimated_transaction_volume_usd": 4238459922.3757358,
  "blocks_size": 261439765,
  "miners_revenue_usd": 0.0,
  "nextretarget": 971711,
  "difficulty": 132716002350731,
  "estimated_btc_sent": 4911128329658,
  "miners_revenue_btc": 0,
  "total_btc_sent": 78896528516930,
  "trade_volume_btc": 2861.73,
  "trade_volume_usd": 246976399.30139998
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
