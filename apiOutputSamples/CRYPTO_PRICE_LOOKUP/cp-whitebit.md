---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-whitebit
status: approved
captured_at: 2026-10-08T04:41:50Z
request_url: https://whitebit.com/api/v1/public/ticker?market=BTC_USDT
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the current last price of BTC in USD."
reviewed_at: 2026-10-08T04:55:04Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "success": true,
  "message": null,
  "result": {
    "open": "84111.43",
    "bid": "82543.69",
    "ask": "82543.7",
    "low": "82255.58",
    "high": "84367.06",
    "last": "82525.24",
    "volume": "1379.997337",
    "deal": "114969520.26881713",
    "change": "-1.89"
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the current last price of BTC in USD._
