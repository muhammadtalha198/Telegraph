---
intent: TOKEN_TOTAL_SUPPLY_VERIFY
slug: supply-coinlore
status: approved
captured_at: 2026-10-08T04:42:16Z
request_url: https://api.coinlore.net/api/ticker/?id=2751
content_type: application/json
inputs: |
  {"token": "0x514910771AF9Ca656af840dff83E8264EcF986CA", "sym": "LINK", "coinlore_id": "2751", "cmc_id": "1975"}
intent_description: |
  Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.
answer_requirement: |
  Must return the token's TOTAL supply (minted count, in whole tokens), not circulating/max.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the total supply of the LINK token, which is the main information requested."
reviewed_at: 2026-10-08T04:57:25Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "id": "2751",
    "symbol": "LINK",
    "name": "ChainLink",
    "nameid": "chainlink",
    "rank": 18,
    "price_usd": "13.12",
    "percent_change_24h": "-3.31",
    "percent_change_1h": "-0.54",
    "percent_change_7d": "-9.13",
    "price_btc": "0.000167",
    "market_cap_usd": "8895988985.76",
    "volume24": 275269789.9583737,
    "volume24a": 243359710.1683575,
    "csupply": "678099970.45",
    "tsupply": "1000000000",
    "msupply": "1000000000"
  }
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the total supply of the LINK token, which is the main information requested._
