---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-bitfinex
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api-pub.bitfinex.com/v2/ticker/tBTCUSD
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Bitfinex
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
[
  85853,
  0.99836638,
  85862,
  2.09182457,
  507,
  0.00594032,
  85856,
  428.46485518,
  86969,
  85095,
  1358182043000
]
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
