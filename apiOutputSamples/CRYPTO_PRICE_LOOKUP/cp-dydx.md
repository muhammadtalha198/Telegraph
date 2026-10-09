---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-dydx
status: pending_review
captured_at: 2026-10-08T04:41:45Z
request_url: https://indexer.dydx.trade/v4/perpetualMarkets?ticker=BTC-USD
content_type: application/json
inputs: |
  {"sym": "BTC", "sym_lower": "btc", "deribit_idx": "btc_usd", "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "dsx_pair": "0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35", "ir": "xbt", "cl_feed": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"}
intent_description: |
  Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.
answer_requirement: |
  Must return the current price of the token asked (any quote currency is fine).
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "markets": {
    "BTC-USD": {
      "clobPairId": "0",
      "ticker": "BTC-USD",
      "status": "ACTIVE",
      "oraclePrice": "82501",
      "priceChange24H": "-1550.43998",
      "volume24H": "7782607.3308",
      "trades24H": 2042,
      "nextFundingRate": "0.00000258536585365854",
      "initialMarginFraction": "0.02",
      "maintenanceMarginFraction": "0.012",
      "openInterest": "228.1848",
      "atomicResolution": -10,
      "quantumConversionExponent": -9,
      "tickSize": "1",
      "stepSize": "0.0001",
      "stepBaseQuantums": 1000000,
      "subticksPerTick": 100000,
      "marketType": "CROSS",
      "openInterestLowerCap": "0",
      "openInterestUpperCap": "0",
      "baseOpenInterest": "782.0931",
      "defaultFundingRate1H": "0"
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
