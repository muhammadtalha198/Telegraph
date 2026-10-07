---
intent: TOKEN_TOTAL_SUPPLY_VERIFY
slug: supply-coinpaprika
status: approved
captured_at: 2026-10-05T09:28:22Z
request_url: https://api.coinpaprika.com/v1/tickers/link-chainlink
content_type: application/json
inputs: |
  {"token": "0x514910771AF9Ca656af840dff83E8264EcF986CA", "cg": "chainlink", "paprika": "link-chainlink"}
intent_description: |
  Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.
answer_requirement: |
  Must return the token's total supply (minted/circulating count).
capture_note: |
  golden-test PASS: CoinPaprika
reviewer_note: "auto_review: [1.00|heuristic+llm] API response contains the required total supply information."
reviewed_at: 2026-10-05T12:34:57Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "id": "link-chainlink",
  "name": "Chainlink",
  "symbol": "LINK",
  "rank": 14,
  "total_supply": 1000000000,
  "max_supply": 1000000000,
  "beta_value": 1.49093,
  "first_data_at": "2017-09-20T00:00:00Z",
  "last_updated": "2026-10-05T09:25:13Z",
  "quotes": {
    "USD": {
      "price": 14.162995516929973,
      "volume_24h": 213032571.3749024,
      "volume_24h_change_24h": 17.299999237060547,
      "market_cap": 10595336521,
      "market_cap_change_24h": 0.3799999952316284,
      "percent_change_15m": 0.05999999865889549,
      "percent_change_30m": 0.15000000596046448,
      "percent_change_1h": -0.20000000298023224,
      "percent_change_6h": -0.05000000074505806,
      "percent_change_12h": -0.23999999463558197,
      "percent_change_24h": 0.3799999952316284,
      "percent_change_7d": 3.180000066757202,
      "percent_change_30d": 0,
      "percent_change_1y": 0,
      "ath_price": 53.01223529,
      "ath_date": "2021-05-10T00:10:00Z",
      "percent_from_price_ath": -73.27
    }
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] API response contains the required total supply information._
