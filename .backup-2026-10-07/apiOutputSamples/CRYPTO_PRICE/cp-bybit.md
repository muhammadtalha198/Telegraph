---
intent: CRYPTO_PRICE
slug: cp-bybit
status: approved
captured_at: 2026-10-05T05:45:11Z
request_url: https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream Bybit
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:31Z
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
        "bid1Price": "85766.7",
        "bid1Size": "0.233476",
        "ask1Price": "85766.8",
        "ask1Size": "0.253817",
        "lastPrice": "85766.8",
        "prevPrice24h": "84922.3",
        "price24hPcnt": "0.0099",
        "highPrice24h": "86996.9",
        "lowPrice24h": "84875.3",
        "turnover24h": "343699779.01773839",
        "volume24h": "4002.208824",
        "usdIndexPrice": "85740.684418"
      }
    ]
  },
  "retExtInfo": {},
  "time": 1791179111237
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
