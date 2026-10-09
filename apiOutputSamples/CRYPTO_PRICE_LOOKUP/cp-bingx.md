---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-bingx
status: approved
captured_at: 2026-10-08T04:41:44Z
request_url: https://open-api.bingx.com/openApi/spot/v1/ticker/price?symbol=BTC-USDT
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the current price of BTC (BTC_USDT) in USDT quote currency."
reviewed_at: 2026-10-08T04:54:16Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "code": 0,
  "timestamp": 1791434504095,
  "data": [
    {
      "symbol": "BTC_USDT",
      "trades": [
        {
          "timestamp": 1791434503694,
          "tradeId": "240717242",
          "price": "82533.23",
          "amount": "",
          "type": 1,
          "volume": "0.000012"
        }
      ]
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the current price of BTC (BTC_USDT) in USDT quote currency._
