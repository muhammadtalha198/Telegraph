---
intent: CRYPTO_PRICE
slug: cp-htx
status: approved
captured_at: 2026-10-05T05:45:14Z
request_url: https://api.huobi.pro/market/detail/merged?symbol=btcusdt
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream HTX
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
{
  "ch": "market.btcusdt.detail.merged",
  "status": "ok",
  "ts": 1791179114957,
  "tick": {
    "id": 388306023296,
    "version": 388306023296,
    "open": 84885.89,
    "close": 85728.3,
    "low": 84852.6,
    "high": 86931.79,
    "amount": 4027.5973326944095,
    "vol": 345100877.7631338,
    "count": 892900,
    "bid": [
      85727.3,
      0.018273
    ],
    "ask": [
      85727.31,
      1.567085
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
