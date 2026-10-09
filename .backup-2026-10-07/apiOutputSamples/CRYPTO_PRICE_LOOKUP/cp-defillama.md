---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-defillama
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://coins.llama.fi/prices/current/coingecko:bitcoin
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: DefiLlama Coins
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "coins": {
    "coingecko:bitcoin": {
      "price": 85843.26694429338,
      "symbol": "BTC",
      "timestamp": 1791192890,
      "confidence": 0.99
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
