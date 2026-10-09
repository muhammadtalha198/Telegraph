---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-digifinex
status: approved
captured_at: 2026-10-09T10:35:28Z
request_url: https://openapi.digifinex.com/v3/ticker?symbol=btc_usdt
content_type: application/json
inputs: |
  btc_usdt
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current price of BTC/USDT as requested."
reviewed_at: 2026-10-09T10:40:24Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "date": 1791542128,
  "ticker": [
    {
      "buy": 82509,
      "high": 82790.01,
      "low": 80387.31,
      "sell": 82509.1,
      "vol": 9825.3728234,
      "base_vol": 803383586.39034,
      "last": 82509.09,
      "change": -0.29,
      "symbol": "btc_usdt"
    }
  ],
  "code": 0
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current price of BTC/USDT as requested._
