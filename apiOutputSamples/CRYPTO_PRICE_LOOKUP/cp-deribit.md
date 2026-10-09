---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-deribit
status: approved
captured_at: 2026-10-08T04:41:44Z
request_url: https://www.deribit.com/api/v2/public/get_index_price?index_name=btc_usd
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the current BTC/USD price as requested."
reviewed_at: 2026-10-08T04:54:19Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "jsonrpc": "2.0",
  "result": {
    "estimated_delivery_price": 82477.96,
    "index_price": 82477.96
  },
  "usIn": 1791434504596178,
  "usOut": 1791434504601145,
  "usDiff": 4967,
  "testnet": false
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the current BTC/USD price as requested._
