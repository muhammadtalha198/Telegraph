---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-kucoin
status: pending_review
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: KuCoin
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "code": "200000",
  "data": {
    "time": 1791193016682,
    "sequence": "38197422259",
    "price": "85869.5",
    "size": "0.00003945",
    "bestBid": "85869.4",
    "bestBidSize": "0.83636459",
    "bestAsk": "85869.5",
    "bestAskSize": "0.02153713"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
