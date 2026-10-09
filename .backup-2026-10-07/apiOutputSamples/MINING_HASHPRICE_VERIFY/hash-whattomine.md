---
intent: MINING_HASHPRICE_VERIFY
slug: hash-whattomine
status: pending_review
captured_at: 2026-10-05T09:41:44Z
request_url: https://whattomine.com/coins/1.json
content_type: application/json
inputs: |
  {}
intent_description: |
  Calculates instantaneous proof-of-work mining revenue per unit of hashing power based on block rewards and network difficulty.
answer_requirement: |
  Must return mining revenue per unit of hashrate (hashprice) or the inputs to compute it.
capture_note: |
  golden-test PASS: WhatToMine
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "id": 1,
  "name": "Bitcoin",
  "tag": "BTC",
  "algorithm": "SHA-256",
  "block_time": "512.0",
  "block_reward": 3.1443778833333336,
  "block_reward24": 3.139072599718309,
  "block_reward3": 3.1497133803298905,
  "block_reward7": 3.1520428400161533,
  "last_block": 969991,
  "difficulty": 132716002350731.3,
  "difficulty24": 132716002350731.61,
  "difficulty3": 132728495214498.03,
  "difficulty7": 132744914872466.8,
  "nethash": 1113302519047363281250,
  "exchange_rate": 85956.45,
  "exchange_rate24": 85806.60585915495,
  "exchange_rate3": 85228.9857400887,
  "exchange_rate7": 84498.1020294824,
  "exchange_rate_vol": 12869.25211,
  "exchange_rate_curr": "BTC",
  "market_cap": "$1,727,174,523,720",
  "pool_fee": "0.000006",
  "estimated_rewards": "0.000271",
  "btc_revenue": "0.00027091",
  "revenue": "$23.29",
  "cost": "$13.22",
  "profit": "$10.06",
  "status": "Active",
  "lagging": false,
  "testing": false,
  "listed": true,
  "timestamp": 1791192973
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
