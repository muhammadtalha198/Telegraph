---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-lbank
status: approved
captured_at: 2026-10-08T04:41:48Z
request_url: https://api.lbank.info/v2/ticker/24hr.do?symbol=btc_usdt
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the latest price of BTC/USDT."
reviewed_at: 2026-10-08T04:54:58Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "msg": "Success",
  "result": "true",
  "data": [
    {
      "symbol": "btc_usdt",
      "ticker": {
        "high": "84382.9",
        "vol": "6261.0207",
        "low": "82284.18",
        "change": "-1.83",
        "turnover": "522648591.23",
        "latest": "82552.04"
      },
      "timestamp": 1791434507424
    }
  ],
  "error_code": 0,
  "ts": 1791434508783
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the latest price of BTC/USDT._
