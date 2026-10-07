---
intent: TOKEN_TOTAL_SUPPLY_VERIFY
slug: supply-ethplorer
status: approved
captured_at: 2026-10-05T09:28:22Z
request_url: https://api.ethplorer.io/getTokenInfo/0x514910771AF9Ca656af840dff83E8264EcF986CA?apiKey=freekey
content_type: application/json
inputs: |
  {"token": "0x514910771AF9Ca656af840dff83E8264EcF986CA", "cg": "chainlink", "paprika": "link-chainlink"}
intent_description: |
  Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.
answer_requirement: |
  Must return the token's total supply (minted/circulating count).
capture_note: |
  golden-test PASS: Ethplorer
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the exact total supply of the token, which directly answers the intent."
reviewed_at: 2026-10-05T12:35:16Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "address": "0x514910771af9ca656af840dff83e8264ecf986ca",
  "decimals": "18",
  "lastUpdated": 1791191689,
  "name": "Chainlink",
  "owner": "",
  "contractInfo": {
    "creatorAddress": "0xf55037738604fddfc4043d12f25124e94d7d1780",
    "creationTransactionHash": "0x5488510df045770efbff57f25d0c6d2c1404d58c1199b21eb8dc5072b22d91d7",
    "creationTimestamp": 1505597189
  },
  "price": {
    "rate": 14.156626080873584,
    "diff": 0.7,
    "diff7d": 3.49,
    "ts": 1791191940,
    "marketCapUsd": 10590571552.41767,
    "availableSupply": 748099970.424884,
    "volume24h": 234575344.03293288,
    "volDiff1": 2.468637182308413,
    "volDiff7": -13.90178112895967,
    "volDiff30": 115.61816317633475,
    "diff30d": 21.71103104612864,
    "currency": "USD"
  },
  "symbol": "LINK",
  "totalSupply": "1000000000000000000000000000",
  "transfersCount": 24725693,
  "txsCount": 11186020,
  "holdersCount": 913596,
  "website": "https://chain.link/",
  "image": "/images/chainlink.jpg",
  "ethTransfersCount": 0,
  "countOps": 24725693
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the exact total supply of the token, which directly answers the intent._
