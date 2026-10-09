---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-upbit-book
status: rejected
captured_at: 2026-10-08T04:42:04Z
request_url: https://api.upbit.com/v1/orderbook?markets=USDT-BTC&level=0
content_type: application/json
inputs: |
  {"upbit": "USDT-BTC", "poloniex": "BTC_USDT", "lbank": "btc_usdt", "bingx": "BTC-USDT", "whitebit": "BTC_USDT", "deribit": "BTC_USDC", "ir": "xbt", "hl": "BTC", "dydx": "BTC-USD", "binance": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.80|heuristic] no bid/ask depth or pool liquidity structure found"
reviewed_at: 2026-10-08T04:56:35Z
review_source: auto_review
review_mode: heuristic
llm_used: false
review_confidence: 0.800
---

## Raw API output

```json
[
  {
    "market": "USDT-BTC",
    "timestamp": 1791434524608,
    "total_ask_size": 2.01355544,
    "total_bid_size": 1.10292106,
    "orderbook_units": [
      {
        "bid_price": 82615.68,
        "bid_size": 8.06e-06,
        "ask_price": 82615.69,
        "ask_size": 0.01392613
      },
      {
        "bid_price": 82567.43,
        "bid_size": 0.00181645,
        "ask_price": 82828.63,
        "ask_size": 0.0316
      },
      {
        "bid_price": 82551.23,
        "bid_size": 0.01210968,
        "ask_price": 82831.3,
        "ask_size": 0.02979146
      },
      {
        "bid_price": 82500,
        "bid_size": 0.00451612,
        "ask_price": 82832.3,
        "ask_size": 0.94
      },
      {
        "bid_price": 82478.34,
        "bid_size": 0.00606219,
        "ask_price": 82846.36,
        "ask_size": 0.01210674
      },
      {
        "bid_price": 82460.7,
        "bid_size": 0.01350508,
        "ask_price": 82865.03,
        "ask_size": 0.00241949
      },
      {
        "bid_price": 82460.69,
        "bid_size": 0.00111468,
        "ask_price": 82918.9,
        "ask_size": 0.00531467
      },
      {
        "bid_price": 82447.23,
        "bid_size": 0.00424513,
        "ask_price": 82926.9,
        "ask_size": 0.00600424
      },
      {
        "bid_price": 82420.87,
        "bid_size": 0.80444723,
        "ask_price": 82939.39,
        "ask_size": 0.03995653
      },
      {
        "bid_price": 82400.04,
        "bid_size": 6.31e-06,
        "ask_price": 83000,
        "ask_size": 0.00451612
      },
      {
        "bid_price": 82400,
        "bid_size": 0.00061892,
        "ask_price": 83104.79,
        "ask_size": 0.00795417
      },
      {
        "bid_price": 82362.61,
        "bid_size": 0.00910607,
        "ask_price": 83108.25,
        "ask_size": 0.01206859
      },
      {
        "bid_price": 82358.38,
        "bid_size": 0.00841145,
        "ask_price": 83260.39,
        "ask_size": 0.00143187
      },
      {
        "bid_price": 82357.99,
        "bid_size": 0.00121664,
        "ask_price": 83260.4,
        "ask_size": 0.00041488
      },
      {
        "bid_price": 82354.44,
        "bid_size": 0.017,
        "ask_price": 83300.75,
        "ask_size": 2.199e-05
      },
      {
        "bid_price": 82342,
        "bid_size": 0.00100631,
        "ask_price": 83324.67,
        "ask_size": 0.1561
      },
      {
        "bid_price": 82337.45,
        "bid_size": 0.01214514,
        "ask_price": 83324.68,
        "ask_size": 0.3
      },
      {
        "bid_price": 82324.63,
        "bid_size": 0.00123938,
        "ask_price": 83324.71,
        "ask_size": 0.23685223
      },
      {
        "bid_price": 82314.51,
        "bid_size": 0.035,
        "ask_price": 83342.23,
        "ask_size": 0.2
      },
      {
        "bid_price": 82312.04,
        "bid_size": 6.31e-06,
        "ask_price": 83358.69,
        "ask_size": 9.524e-05
      },
      {
        "bid_price": 82311.34,
        "bid_size": 0.00127439,
        "ask_price": 83362.31,
        "ask_size": 9.545e-05
      },
      {
        "bid_price": 82300,
        "bid_size": 0.00447696,
        "ask_price": 83362.32,
        "ask_size": 0.00019203
      },
      {
        "bid_price": 82282,
        "bid_size": 0.00443261,
        "ask_price": 83365.63,
        "ask_size": 9.529e-05
      },
      {
        "bid_price": 82273.94,
        "bid_size": 0.11380286,
        "ask_price": 83370.15,
        "ask_size": 0.01203068
      },
      {
        "bid_price": 82260,
        "bid_size": 0.004,
        "ask_price": 83372.95,
        "ask_size": 9.294e-05
      },
      {
        "bid_price": 82253.02,
        "bid_size": 0.0042607,
        "ask_price": 83373.14,
        "ask_size": 9.61e-05
      },
      {
        "bid_price": 82250,
        "bid_size": 0.00451885,
        "ask_price": 83373.15,
        "ask_size": 9.145e-05
      },
      {
        "bid_price": 82237.37,
        "bid_size": 6.32e-06,
        "ask_price": 83373.43,
        "ask_size": 9.61e-05
      },
      {
        "bid_price": 82226.56,
        "bid_size": 0.00121858,
        "ask_price": 83373.44,
        "ask_size": 9.61e-05
      },
      {
        "bid_price": 82200,
        "bid_size": 0.03134864,
        "ask_price": 83374.06,
        "ask_size": 9.495e-05
      }
    ],
    "level": 0
  }
]
```

## Why this matches (or not)

_[0.80|heuristic] no bid/ask depth or pool liquidity structure found_
