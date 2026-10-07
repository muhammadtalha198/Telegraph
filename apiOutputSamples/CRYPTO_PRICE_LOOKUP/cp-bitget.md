---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-bitget
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.bitget.com/api/v2/spot/market/tickers?symbol=BTCUSDT
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: Bitget
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1791193037018,
  "data": [
    {
      "open": "85223.94",
      "symbol": "BTCUSDT",
      "high24h": "86993.9",
      "low24h": "85091.61",
      "lastPr": "85888.43",
      "quoteVolume": "189677574.341427",
      "baseVolume": "2206.283847",
      "usdtVolume": "189677574.34142648",
      "ts": "1791193035326",
      "bidPr": "85888.42",
      "askPr": "85888.43",
      "bidSz": "0.432037",
      "askSz": "0.198338",
      "openUtc": "86511",
      "changeUtc24h": "-0.0072",
      "change24h": "0.0078"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
