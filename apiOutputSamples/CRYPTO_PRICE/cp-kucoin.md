---
intent: CRYPTO_PRICE
slug: cp-kucoin
status: approved
captured_at: 2026-10-05T05:45:12Z
request_url: https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream KuCoin
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
{
  "code": "200000",
  "data": {
    "time": 1791179106413,
    "sequence": "38189558362",
    "price": "85771.9",
    "size": "0.00011652",
    "bestBid": "85771.9",
    "bestBidSize": "0.02645122",
    "bestAsk": "85772",
    "bestAskSize": "0.48267826"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
