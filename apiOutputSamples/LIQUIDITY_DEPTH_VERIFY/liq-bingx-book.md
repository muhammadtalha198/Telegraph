---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-bingx-book
status: approved
captured_at: 2026-10-08T04:41:59Z
request_url: https://open-api.bingx.com/openApi/spot/v1/market/depth?symbol=BTC-USDT&limit=5
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
reviewed_at: 2026-10-08T04:56:05Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "code": 0,
  "timestamp": 1791434519550,
  "data": {
    "bids": [
      [
        "82525.10",
        "0.003924"
      ],
      [
        "82520.44",
        "7.418738"
      ],
      [
        "82520.42",
        "0.006782"
      ],
      [
        "82519.92",
        "0.000108"
      ],
      [
        "82519.61",
        "0.000058"
      ]
    ],
    "asks": [
      [
        "82531.09",
        "0.000108"
      ],
      [
        "82530.99",
        "0.006098"
      ],
      [
        "82530.60",
        "0.000550"
      ],
      [
        "82529.79",
        "0.008917"
      ],
      [
        "82525.12",
        "0.000770"
      ]
    ],
    "ts": 1791434519550,
    "lastUpdateId": 16434675525
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the bid and ask order book levels as requested._
