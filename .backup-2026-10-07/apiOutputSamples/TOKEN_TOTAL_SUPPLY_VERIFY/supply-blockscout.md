---
intent: TOKEN_TOTAL_SUPPLY_VERIFY
slug: supply-blockscout
status: approved
captured_at: 2026-10-05T09:28:22Z
request_url: https://eth.blockscout.com/api/v2/tokens/0x514910771AF9Ca656af840dff83E8264EcF986CA
content_type: application/json
inputs: |
  {"token": "0x514910771AF9Ca656af840dff83E8264EcF986CA", "cg": "chainlink", "paprika": "link-chainlink"}
intent_description: |
  Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.
answer_requirement: |
  Must return the token's total supply (minted/circulating count).
capture_note: |
  golden-test PASS: Blockscout
reviewer_note: "auto_review: [1.00|heuristic+llm] API response contains the token's total supply which answers the intent."
reviewed_at: 2026-10-05T11:56:35Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "address_hash": "0x514910771AF9Ca656af840dff83E8264EcF986CA",
  "circulating_market_cap": "10544844121.744276",
  "circulating_supply": null,
  "decimals": "18",
  "exchange_rate": "14.1",
  "holders_count": "1006794",
  "icon_url": "https://assets.coingecko.com/coins/images/877/small/Chainlink_Logo_500.png?1760023405",
  "name": "Chainlink",
  "reputation": "ok",
  "symbol": "LINK",
  "total_supply": "1000000000000000000000000000",
  "type": "ERC-20",
  "volume_24h": "252800738.07781413"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] API response contains the token's total supply which answers the intent._
