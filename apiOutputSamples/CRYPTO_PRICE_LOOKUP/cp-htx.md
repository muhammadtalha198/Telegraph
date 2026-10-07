---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-htx
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.huobi.pro/market/detail/merged?symbol=btcusdt
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: HTX
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "ch": "market.btcusdt.detail.merged",
  "status": "ok",
  "ts": 1791193028871,
  "tick": {
    "id": 388314945222,
    "version": 388314945222,
    "open": 85182.01,
    "close": 85816.59,
    "low": 85059.57,
    "high": 86931.79,
    "amount": 4365.804875821033,
    "vol": 374836779.5022099,
    "count": 970821,
    "bid": [
      85816.59,
      2.436028
    ],
    "ask": [
      85816.6,
      0.112215
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
