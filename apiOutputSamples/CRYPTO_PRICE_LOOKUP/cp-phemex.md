---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-phemex
status: approved
captured_at: 2026-10-09T10:35:23Z
request_url: https://api.phemex.com/md/spot/ticker/24hr?symbol=sBTCUSDT
content_type: application/json
inputs: |
  BTCUSDT
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  lastEp is price x1e8 fixed-point
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current price of BTCUSDT (sBTCUSDT) from Phemex CEX Spot market."
reviewed_at: 2026-10-09T10:37:59Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "error": null,
  "id": 0,
  "result": {
    "askEp": 8252000000000,
    "bidEp": 8251600000000,
    "highEp": 8276999000000,
    "indexEp": 8244773710000,
    "lastEp": 8252200000000,
    "lowEp": 8050000000000,
    "openEp": 8275534000000,
    "symbol": "sBTCUSDT",
    "timestamp": 1791542122401704232,
    "turnoverEv": 29297261063011557,
    "volumeEv": 356947139500
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current price of BTCUSDT (sBTCUSDT) from Phemex CEX Spot market._
