---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-poloniex-book
status: approved
captured_at: 2026-10-08T04:42:04Z
request_url: https://api.poloniex.com/markets/BTC_USDT/orderBook?limit=5
content_type: application/json
inputs: |
  {"upbit": "USDT-BTC", "poloniex": "BTC_USDT", "lbank": "btc_usdt", "bingx": "BTC-USDT", "whitebit": "BTC_USDT", "deribit": "BTC_USDC", "ir": "xbt", "hl": "BTC", "dydx": "BTC-USD", "binance": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the required bid and ask order book data for the specified pair."
reviewed_at: 2026-10-08T04:56:34Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "bids": [
    "82488.88",
    "0.097243",
    "82488.87",
    "0.031056",
    "82477.43",
    "0.202167",
    "82451.85",
    "0.107893",
    "82451.78",
    "0.10789"
  ],
  "asks": [
    "82559.08",
    "0.000045",
    "82597.47",
    "0.278103",
    "82598.77",
    "0.163521",
    "82607.02",
    "0.199856",
    "82611.14",
    "0.24427"
  ],
  "scale": "0.01",
  "time": 1791434523675,
  "ts": 1791434524136
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the required bid and ask order book data for the specified pair._
