---
intent: EVENT_OUTCOME_RESOLUTION
slug: event-manifold
status: approved
captured_at: 2026-10-05T09:29:35Z
request_url: https://api.manifold.markets/v0/search-markets?term=presidential%20election&filter=resolved&limit=5
content_type: application/json
inputs: |
  {}
intent_description: |
  Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.
answer_requirement: |
  Must state the settled result of the real-world event asked (who won / final outcome).
capture_note: |
  golden-test PASS: Manifold Markets
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response contains the resolved result for the specified event."
reviewed_at: 2026-10-05T12:19:12Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "id": "UVHhF9M4jfGQcjdBshzd",
    "creatorId": "4UrkF8yHd2PKzmgXB77GGkNRgXO2",
    "creatorUsername": "GustavoMafra",
    "creatorName": "Gustavo Mafra",
    "createdTime": 1673284551719,
    "creatorAvatarUrl": "https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-images%2FGustavoMafra%2FTPftSeT7dB.jpg?alt=media&token=ead35656-54d8-46f1-a8e3-8d7a4f86a32e",
    "closeTime": 1791162158205,
    "question": "Will Lula be a candidate for the 2026 Brazilian presidential election?",
    "slug": "will-lula-be-a-candidate-for-the-20",
    "url": "https://manifold.markets/GustavoMafra/will-lula-be-a-candidate-for-the-20",
    "pool": {
      "NO": 13598.155947854511,
      "YES": 335.84750101757936
    },
    "probability": 0.9899999999999999,
    "p": 0.7097329828350025,
    "totalLiquidity": 1000,
    "outcomeType": "BINARY",
    "mechanism": "cpmm-1",
    "volume": 16215.438491348315,
    "volume24Hours": 5718.174252841723,
    "isResolved": true,
    "resolution": "YES",
    "resolutionTime": 1791162158205,
    "resolutionProbability": 0.9899999999999999,
    "resolverId": "4UrkF8yHd2PKzmgXB77GGkNRgXO2",
    "uniqueBettorCount": 39,
    "lastUpdatedTime": 1791162158205,
    "lastBetTime": 1791129760571,
    "lastCommentTime": 1761274143821,
    "token": "MANA"
  },
  {
    "id": "5pcLg2QtSA",
    "creatorId": "BvJf104FBFXOnHH4kNQf9K1qWCb2",
    "creatorUsername": "bbno",
    "creatorName": "bbno",
    "createdTime": 1791094482821,
    "creatorAvatarUrl": "https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-images%2Fbbno%2FNRNphd8AEs.jpg?alt=media&token=ec1aefb6-d43c-4821-a399-cb5997aae38e",
    "closeTime": 1791162000000,
    "question": "Brazil Presidential Election First Round Winner",
    "slug": "brazil-presidential-election-first",
    "url": "https://manifold.markets/bbno/brazil-presidential-election-first",
    "totalLiquidity": 100,
    "outcomeType": "MULTIPLE_CHOICE",
    "mechanism": "cpmm-multi-1",
    "volume": 1367.2269075990155,
    "volume24Hours": 1357.2269075990152,
    "isResolved": true,
    "resolution": "8QLtNRRNgO",
    "resolutionTime": 1791162233725,
    "resolverId": "BvJf104FBFXOnHH4kNQf9K1qWCb2",
    "uniqueBettorCount": 19,
    "lastUpdatedTime": 1791162000000,
    "lastBetTime": 1791158824977,
    "lastCommentTime": 1791160529827,
    "token": "MANA"
  },
  {
    "id": "Ss7VLXukYkrHyRLmkkZB",
    "creatorId": "4UrkF8yHd2PKzmgXB77GGkNRgXO2",
    "creatorUsername": "GustavoMafra",
    "creatorName": "Gustavo Mafra",
    "createdTime": 1689705367683,
    "creatorAvatarUrl": "https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-images%2FGustavoMafra%2FTPftSeT7dB.jpg?alt=media&token=ead35656-54d8-46f1-a8e3-8d7a4f86a32e",
    "closeTime": 1791162062542,
    "question": "Will Michelle Bolsonaro be a candidate for the 2026 Brazilian presidential election?",
    "slug": "will-michele-bolsonaro-be-a-candida",
    "url": "https://manifold.markets/GustavoMafra/will-michele-bolsonaro-be-a-candida",
    "pool": {
      "NO": 23.910166894710073,
      "YES": 1754.5807793657368
    },
    "probability": 0.010000000000000007,
    "p": 0.4256947824593641,
    "totalLiquidity": 150,
    "outcomeType": "BINARY",
    "mechanism": "cpmm-1",
    "volume": 1653.4603416237746,
    "volume24Hours": 991.5401753226398,
    "isResolved": true,
    "resolution": "NO",
    "resolutionTime": 1791162062542,
    "resolutionProbability": 0.010000000000000007,
    "resolverId": "4UrkF8yHd2PKzmgXB77GGkNRgXO2",
    "uniqueBettorCount": 12,
    "lastUpdatedTime": 1791162062542,
    "lastBetTime": 1791124452415,
    "lastCommentTime": 1791124472221,
    "token": "MANA"
  },
  {
    "id": "g4demYcVGHlAHhlbDGed",
    "creatorId": "4UrkF8yHd2PKzmgXB77GGkNRgXO2",
    "creatorUsername": "GustavoMafra",
    "creatorName": "Gustavo Mafra",
    "createdTime": 1687120617752,
    "creatorAvatarUrl": "https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-images%2FGustavoMafra%2FTPftSeT7dB.jpg?alt=media&token=ead35656-54d8-46f1-a8e3-8d7a4f86a32e",
    "closeTime": 1791162171708,
    "question": "Will Tarcísio de Freitas be a candidate for the 2026 Brazilian presidential election?",
    "slug": "will-tarcisio-de-freitas-be-a-candi",
    "url": "https://manifold.markets/GustavoMafra/will-tarcisio-de-freitas-be-a-candi",
    "pool": {
      "NO": 19.385519658572093,
      "YES": 1636.9056346466477
    },
    "probability": 0.010000000000000023,
    "p": 0.46031283883805707,
    "totalLiquidity": 150,
    "outcomeType": "BINARY",
    "mechanism": "cpmm-1",
    "volume": 1741.9521466209394,
    "volume24Hours": 726.155546152955,
    "isResolved": true,
    "resolution": "NO",
    "resolutionTime": 1791162171708,
    "resolutionProbability": 0.010000000000000024,
    "resolverId": "4UrkF8yHd2PKzmgXB77GGkNRgXO2",
    "uniqueBettorCount": 12,
    "lastUpdatedTime": 1791162171708,
    "lastBetTime": 1791124383208,
    "lastCommentTime": 1791124396861,
    "token": "MANA"
  },
  {
    "id": "hghgQ9h5Ul",
    "creatorId": "RxP08QZGClaU5QqutJvYndXKX3e2",
    "creatorUsername": "Brierbr",
    "creatorName": "BrierBR",
    "createdTime": 1764634544591,
    "creatorAvatarUrl": "https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-images%2FPedro%2FxAFregT6Jv.jpg?alt=media&token=eb7fb718-ffbf-44b9-9287-0ce4519ba1a4",
    "closeTime": 1791158340000,
    "question": "Brazil 2026 Election: Will the presidential election be decided in first round?",
    "slug": "brazils-2026-presidential-election",
    "url": "https://manifold.markets/Brierbr/brazils-2026-presidential-election",
    "pool": {
      "NO": 10.0503781525921,
      "YES": 994.9874371066196
    },
    "probability": 0.01000000000000001,
    "p": 0.5000000000000007,
    "totalLiquidity": 100,
    "outcomeType": "BINARY",
    "mechanism": "cpmm-1",
    "volume": 2106.944710966138,
    "volume24Hours": 981.8486176796883,
    "isResolved": true,
    "resolution": "NO",
    "resolutionTime": 1791165252302,
    "resolutionProbability": 0.01000000000000001,
    "resolverId": "RxP08QZGClaU5QqutJvYndXKX3e2",
    "uniqueBettorCount": 16,
    "lastUpdatedTime": 1791158340000,
    "lastBetTime": 1791155026611,
    "token": "MANA"
  }
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response contains the resolved result for the specified event._
