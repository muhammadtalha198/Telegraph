---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-deribit-book
status: pending_review
captured_at: 2026-10-08T04:41:59Z
request_url: https://www.deribit.com/api/v2/public/get_order_book?instrument_name=BTC_USDC&depth=5
content_type: application/json
inputs: |
  {"upbit": "USDT-BTC", "poloniex": "BTC_USDT", "lbank": "btc_usdt", "bingx": "BTC-USDT", "whitebit": "BTC_USDT", "deribit": "BTC_USDC", "ir": "xbt", "hl": "BTC", "dydx": "BTC-USD", "binance": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "jsonrpc": "2.0",
  "result": {
    "timestamp": 1791434519816,
    "state": "open",
    "stats": {
      "high": 84365.25,
      "low": 82161.31,
      "price_change": -1.9132,
      "volume": 7075.57926735
    },
    "change_id": 9528167774,
    "index_price": 82471.6,
    "instrument_name": "BTC_USDC",
    "bids": [
      [
        82457.66,
        4.923e-05
      ],
      [
        82455.76,
        1.4e-05
      ],
      [
        82451.11,
        0.00623526
      ],
      [
        82448.44,
        0.09703033
      ],
      [
        82447.76,
        0.01223697
      ]
    ],
    "asks": [
      [
        82457.67,
        0.30284909
      ],
      [
        82457.79,
        0.023
      ],
      [
        82457.87,
        0.09701924
      ],
      [
        82458.91,
        0.04499454
      ],
      [
        82459.33,
        0.05702334
      ]
    ],
    "last_price": 82500.0,
    "min_price": 80822.16,
    "max_price": 84121.04,
    "mark_price": 82471.6,
    "best_ask_price": 82457.67,
    "best_bid_price": 82457.66,
    "best_ask_amount": 0.30284909,
    "best_bid_amount": 4.923e-05
  },
  "usIn": 1791434519825069,
  "usOut": 1791434519826925,
  "usDiff": 1856,
  "testnet": false
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
