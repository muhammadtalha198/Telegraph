---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-bybit
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Bybit
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "category": "spot",
    "list": [
      {
        "symbol": "BTCUSDT",
        "bid1Price": "85890",
        "bid1Size": "0.341275",
        "ask1Price": "85890.1",
        "ask1Size": "0.230573",
        "lastPrice": "85890",
        "prevPrice24h": "85196.2",
        "price24hPcnt": "0.0081",
        "highPrice24h": "86996.9",
        "lowPrice24h": "85097.9",
        "turnover24h": "494134723.75799243",
        "volume24h": "5737.18264",
        "usdIndexPrice": "85853.102558"
      }
    ]
  },
  "retExtInfo": {},
  "time": 1791193019498
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
