---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-bitstamp
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://www.bitstamp.net/api/v2/ticker/btcusd/
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Bitstamp
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "timestamp": "1791193016",
  "open": "86490.27",
  "high": "86968.58",
  "low": "85090.60",
  "last": "85864.00",
  "volume": "1277.88750357",
  "vwap": "86039.58",
  "bid": "85864.00",
  "ask": "85864.01",
  "side": "1",
  "open_24": "85200.65",
  "percent_change_24": "0.78",
  "market_type": "SPOT"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
