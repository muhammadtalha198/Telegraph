---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-bitrue
status: approved
captured_at: 2026-10-09T10:35:25Z
request_url: https://openapi.bitrue.com/api/v1/ticker/price?symbol=BTCUSDT
content_type: application/json
inputs: |
  BTCUSDT
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current price of BTCUSDT as requested."
reviewed_at: 2026-10-09T10:39:13Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "symbol": "BTCUSDT",
  "price": "82522.80"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current price of BTCUSDT as requested._
