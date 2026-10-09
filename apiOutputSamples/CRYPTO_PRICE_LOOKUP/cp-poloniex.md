---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-poloniex
status: approved
captured_at: 2026-10-08T04:41:49Z
request_url: https://api.poloniex.com/markets/BTC_USDT/price
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the current price of BTC/USDT as requested."
reviewed_at: 2026-10-08T04:55:00Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "symbol": "BTC_USDT",
  "price": "82528.77",
  "dailyChange": "-0.0184",
  "time": 1791434509478,
  "ts": 1791434509486
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the current price of BTC/USDT as requested._
