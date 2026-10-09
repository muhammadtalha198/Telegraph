---
intent: OPTIMAL_EXECUTION_ROUTE
slug: route-jupiter
status: approved
captured_at: 2026-10-05T09:27:49Z
request_url: https://lite-api.jup.ag/swap/v1/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000
content_type: application/json
inputs: |
  {"sol_in": "So11111111111111111111111111111111111111112", "sol_out": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "sol_amount": "1000000000"}
intent_description: |
  Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.
answer_requirement: |
  Must return the best swap route / expected output amount for the trade asked.
capture_note: |
  golden-test PASS: Jupiter (Solana)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the expected output amount and its USD value, which answers the intent to determine the best swap route and expected output amount for the trade asked. | heuristic: Route quote output amount present"
reviewed_at: 2026-10-05T12:33:07Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "inputMint": "So11111111111111111111111111111111111111112",
  "inAmount": "1000000000",
  "outputMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
  "outAmount": "120704786",
  "otherAmountThreshold": "120101263",
  "swapMode": "ExactIn",
  "slippageBps": 50,
  "platformFee": null,
  "priceImpactPct": "0",
  "routePlan": [
    {
      "swapInfo": {
        "ammKey": "GMCJvYGf5Ex2ARiMquaBDqU6iKM8uiEQkB8jCnoNfHpC",
        "label": "GoonFi V2",
        "inputMint": "So11111111111111111111111111111111111111112",
        "outputMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "inAmount": "1000000000",
        "outAmount": "120704786",
        "updateContextSlot": "453538720"
      },
      "percent": 100,
      "bps": null
    }
  ],
  "contextSlot": 453538721,
  "timeTaken": 0.001986187,
  "swapUsdValue": "120.6730159301947",
  "mostReliableAmmsQuoteReport": {
    "info": {
      "Czfq3xZZDmsdGdUyrNLtRhGc47cXcZtLG4crryfu44zE": "120646491",
      "BZtgQEyS6eXUXicYPHecYQ7PybqodXQMvkjUbP4R8mUU": "120677080"
    }
  },
  "longtailMarketQuoteReport": null,
  "useIncurredSlippageForQuoting": null,
  "useRewards": null,
  "otherRoutePlans": null,
  "loadedLongtailToken": false,
  "instructionVersion": null,
  "transactionVersion": 0
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the expected output amount and its USD value, which answers the intent to determine the best swap route and expected output amount for the trade asked. | heuristic: Route quote output amount present_
