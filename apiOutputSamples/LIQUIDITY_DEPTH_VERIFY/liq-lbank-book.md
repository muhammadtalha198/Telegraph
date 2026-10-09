---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-lbank-book
status: approved
captured_at: 2026-10-08T04:42:03Z
request_url: https://api.lbank.info/v2/depth.do?symbol=btc_usdt&size=5
content_type: application/json
inputs: |
  {"upbit": "USDT-BTC", "poloniex": "BTC_USDT", "lbank": "btc_usdt", "bingx": "BTC-USDT", "whitebit": "BTC_USDT", "deribit": "BTC_USDC", "ir": "xbt", "hl": "BTC", "dydx": "BTC-USD", "binance": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the bid and ask order book levels as requested."
reviewed_at: 2026-10-08T04:56:32Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "result": "true",
  "msg": "Success",
  "data": {
    "asks": [
      [
        "82525.15",
        "4.06024"
      ],
      [
        "82525.16",
        "0.00051"
      ],
      [
        "82525.17",
        "0.00015"
      ],
      [
        "82525.74",
        "0.00009"
      ],
      [
        "82526.17",
        "0.00018"
      ]
    ],
    "bids": [
      [
        "82525.14",
        "1.84824"
      ],
      [
        "82522.49",
        "0.01907"
      ],
      [
        "82522.22",
        "0.00017"
      ],
      [
        "82521.17",
        "0.01859"
      ],
      [
        "82521.04",
        "0.00016"
      ]
    ],
    "timestamp": 1791434523432
  },
  "error_code": 0,
  "ts": 1791434523432
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the bid and ask order book levels as requested._
