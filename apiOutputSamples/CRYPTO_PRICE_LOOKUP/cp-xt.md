---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-xt
status: approved
captured_at: 2026-10-09T10:35:24Z
request_url: https://sapi.xt.com/v4/public/ticker/price?symbol=btc_usdt
content_type: application/json
inputs: |
  btc_usdt
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current price of BTC (in USDT) as requested."
reviewed_at: 2026-10-09T10:38:34Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "rc": 0,
  "mc": "SUCCESS",
  "ma": [],
  "result": [
    {
      "s": "btc_usdt",
      "t": 1791542123932,
      "p": "82513.03"
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current price of BTC (in USDT) as requested._
