---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-coinlore
status: approved
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.coinlore.net/api/ticker/?id=90
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: CoinLore
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the BTC/USD price as requested."
reviewed_at: 2026-10-05T12:36:02Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "id": "90",
    "symbol": "BTC",
    "name": "Bitcoin",
    "nameid": "bitcoin",
    "rank": 1,
    "price_usd": "85894.82",
    "percent_change_24h": "0.73",
    "percent_change_1h": "-0.64",
    "percent_change_7d": "1.52",
    "price_btc": "1.00",
    "market_cap_usd": "1715392727275.70",
    "volume24": 22872303928.937515,
    "volume24a": 14454465964.030243,
    "csupply": "19970852.00",
    "tsupply": "19970852",
    "msupply": "21000000"
  }
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the BTC/USD price as requested._
