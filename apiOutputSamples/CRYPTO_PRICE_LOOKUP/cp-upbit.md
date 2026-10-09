---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-upbit
status: approved
captured_at: 2026-10-08T04:41:50Z
request_url: https://api.upbit.com/v1/ticker?markets=USDT-BTC
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the current trade price of BTC (USDT) which directly answers the intent."
reviewed_at: 2026-10-08T04:55:02Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "market": "USDT-BTC",
    "trade_date": "20261008",
    "trade_time": "044144",
    "trade_date_kst": "20261008",
    "trade_time_kst": "134144",
    "trade_timestamp": 1791434504705,
    "opening_price": 83354.25,
    "high_price": 83529.34,
    "low_price": 82447.23,
    "trade_price": 82615.68,
    "prev_closing_price": 83615.27,
    "change": "FALL",
    "change_price": 999.59,
    "change_rate": 0.0119546346,
    "signed_change_price": -999.59,
    "signed_change_rate": -0.0119546346,
    "trade_volume": 0.00065976,
    "acc_trade_price": 135484.0974467679,
    "acc_trade_price_24h": 447831.72399788,
    "acc_trade_volume": 1.63455971,
    "acc_trade_volume_24h": 5.37475098,
    "highest_52_week_price": 122774.75,
    "highest_52_week_date": "2025-10-10",
    "lowest_52_week_price": 58010.01,
    "lowest_52_week_date": "2026-07-01",
    "timestamp": 1791434505038
  }
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the current trade price of BTC (USDT) which directly answers the intent._
