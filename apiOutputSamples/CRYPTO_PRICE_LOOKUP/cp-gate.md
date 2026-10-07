---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-gate
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.gateio.ws/api/v4/spot/tickers?currency_pair=BTC_USDT
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Gate.io
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
[
  {
    "currency_pair": "BTC_USDT",
    "last": "85886.9",
    "lowest_ask": "85886.9",
    "lowest_size": "3.175936",
    "highest_bid": "85886.8",
    "highest_size": "2.833187",
    "change_percentage": "0.78",
    "base_volume": "6238.937138",
    "quote_volume": "537294080.9913638",
    "high_24h": "86989.4",
    "low_24h": "85092"
  }
]
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
