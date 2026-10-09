---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-whitebit-book
status: approved
captured_at: 2026-10-08T04:42:05Z
request_url: https://whitebit.com/api/v4/public/orderbook/BTC_USDT?limit=5
content_type: application/json
inputs: |
  {"upbit": "USDT-BTC", "poloniex": "BTC_USDT", "lbank": "btc_usdt", "bingx": "BTC-USDT", "whitebit": "BTC_USDT", "deribit": "BTC_USDC", "ir": "xbt", "hl": "BTC", "dydx": "BTC-USD", "binance": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the bid and ask order book depths as requested."
reviewed_at: 2026-10-08T04:56:37Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "ticker_id": "BTC_USDT",
  "timestamp": 1791434525,
  "asks": [
    [
      "82522.46",
      "0.012722"
    ],
    [
      "82522.79",
      "0.038777"
    ],
    [
      "82526.75",
      "0.000717"
    ],
    [
      "82528.67",
      "0.038099"
    ],
    [
      "82530.6",
      "0.073122"
    ]
  ],
  "bids": [
    [
      "82522.45",
      "0.012739"
    ],
    [
      "82520.08",
      "0.000041"
    ],
    [
      "82517.4",
      "0.000038"
    ],
    [
      "82515.39",
      "0.000134"
    ],
    [
      "82514.74",
      "0.000024"
    ]
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the bid and ask order book depths as requested._
