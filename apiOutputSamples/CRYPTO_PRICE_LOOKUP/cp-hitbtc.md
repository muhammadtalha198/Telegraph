---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-hitbtc
status: approved
captured_at: 2026-10-09T10:35:27Z
request_url: https://api.hitbtc.com/api/3/public/ticker/BTCUSDT
content_type: application/json
inputs: |
  BTCUSDT
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the last price of BTCUSDT, which directly answers the intent to fetch the current price."
reviewed_at: 2026-10-09T10:39:47Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "ask": "82531.25",
  "bid": "82503.59",
  "last": "82645.07",
  "low": "80500.00",
  "high": "82760.76",
  "open": "82764.26",
  "volume": "760.59126",
  "volume_quote": "62236003.6201516",
  "timestamp": "2026-10-09T10:35:27.056Z"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the last price of BTCUSDT, which directly answers the intent to fetch the current price._
