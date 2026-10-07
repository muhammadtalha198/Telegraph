---
intent: CRYPTO_PRICE
slug: cp-defillama
status: approved
captured_at: 2026-10-05T05:45:16Z
request_url: https://coins.llama.fi/prices/current/coingecko:ethereum
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream DefiLlama Coins
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:31Z
---

## Raw API output

```json
{
  "coins": {
    "coingecko:ethereum": {
      "price": 2701.406622981317,
      "symbol": "ETH",
      "timestamp": 1791178960,
      "confidence": 0.99
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
