---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-cryptocom
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.crypto.com/exchange/v1/public/get-tickers?instrument_name=BTC_USDT
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Crypto.com Exchange
reviewer_note: ""
reviewed_at: ""
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
        "l": "85087.86",
        "a": "85884.72",
        "v": "1185.3316",
        "vv": "102005045.39",
        "c": "0.0077",
        "b": "85885.87",
        "k": "85885.88",
        "oi": "0",
        "t": 1791193035073
      }
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
