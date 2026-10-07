---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-coinpaprika
status: approved
captured_at: 2026-10-05T09:37:27Z
request_url: https://api.coinpaprika.com/v1/tickers/btc-bitcoin
content_type: application/json
inputs: |
  {"sym": "BTC", "cg": "bitcoin", "paprika": "btc-bitcoin", "kraken_pair": "XBTUSD", "kraken_key": "XXBTZUSD", "pyth": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43", "coinlore": "90"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  golden-test PASS: CoinPaprika
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current price of BTC in USD."
reviewed_at: 2026-10-05T12:36:56Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "id": "btc-bitcoin",
  "name": "Bitcoin",
  "symbol": "BTC",
  "rank": 1,
  "total_supply": 20093703,
  "max_supply": 21000000,
  "beta_value": 1.03058,
  "first_data_at": "2010-07-17T00:00:00Z",
  "last_updated": "2026-10-05T09:36:15Z",
  "quotes": {
    "USD": {
      "price": 85836.8634397365,
      "volume_24h": 20475465924.682415,
      "volume_24h_change_24h": 62.36000061035156,
      "market_cap": 1724781212941,
      "market_cap_change_24h": 0.6000000238418579,
      "percent_change_15m": -0.05000000074505806,
      "percent_change_30m": -0.23000000417232513,
      "percent_change_1h": -0.44999998807907104,
      "percent_change_6h": -0.47999998927116394,
      "percent_change_12h": -0.12999999523162842,
      "percent_change_24h": 0.5899999737739563,
      "percent_change_7d": 3.609999895095825,
      "percent_change_30d": 0,
      "percent_change_1y": 0,
      "ath_price": 126173.1777846797,
      "ath_date": "2025-10-06T19:00:40Z",
      "percent_from_price_ath": -31.94
    }
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current price of BTC in USD._
