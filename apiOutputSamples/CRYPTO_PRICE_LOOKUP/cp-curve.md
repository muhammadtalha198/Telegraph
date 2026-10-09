---
intent: CRYPTO_PRICE_LOOKUP
slug: cp-curve
status: pending_review
captured_at: 2026-10-08T04:41:44Z
request_url: https://prices.curve.finance/v1/usd_price/ethereum/0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599
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
  "data": {
    "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    "usd_price": 82297.62854627694,
    "last_updated": "2026-10-08T04:23:23"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
