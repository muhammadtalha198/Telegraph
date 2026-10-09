---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-gemini
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.gemini.com/v2/ticker/btcusd
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Gemini
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "symbol": "BTCUSD",
  "open": "85190.81",
  "high": "86980",
  "low": "85102.71",
  "close": "85846.26",
  "changes": [
    "85221.21",
    "85268.31",
    "85305.73",
    "85132.28",
    "85245",
    "85279.45",
    "85248.35",
    "85357.94",
    "85307.72",
    "85330.01",
    "85420.02",
    "85819.36",
    "85842.76",
    "86446.54",
    "86521.75",
    "86628.85",
    "86608.57",
    "86512.72",
    "86071.76",
    "85511.91",
    "85731.99",
    "86207.41",
    "86186.53",
    "86215.45"
  ],
  "bid": "85868.36000",
  "ask": "85868.37000"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
