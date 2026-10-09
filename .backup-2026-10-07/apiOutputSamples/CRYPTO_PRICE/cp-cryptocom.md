---
intent: CRYPTO_PRICE
slug: cp-cryptocom
status: approved
captured_at: 2026-10-05T05:45:15Z
request_url: https://api.crypto.com/exchange/v1/public/get-tickers?instrument_name=BTC_USDT
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream Crypto.com Exchange
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:31Z
---

## Raw API output

```json
{
  "id": -1,
  "method": "public/get-tickers",
  "code": 0,
  "result": {
    "data": [
      {
        "i": "BTC_USDT",
        "h": "87000.00",
        "l": "84870.33",
        "a": "85768.30",
        "v": "1042.4626",
        "vv": "89605257.17",
        "c": "0.0099",
        "b": "85765.12",
        "k": "85765.13",
        "oi": "0",
        "t": 1791179115094
      }
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
