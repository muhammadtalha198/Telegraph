---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-coingecko
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: CoinGecko
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "bitcoin": {
    "usd": 85843
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
