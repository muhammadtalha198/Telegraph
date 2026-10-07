---
intent: CRYPTO_PRICE
slug: cp-mexc
status: approved
captured_at: 2026-10-05T05:45:14Z
request_url: https://api.mexc.com/api/v3/ticker/price?symbol=BTCUSDT
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream MEXC
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
{
  "symbol": "BTCUSDT",
  "price": "85782.65"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
