---
intent: CRYPTO_PRICE
slug: cp-gemini
status: approved
captured_at: 2026-10-05T05:45:12Z
request_url: https://api.gemini.com/v2/ticker/btcusd
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream Gemini
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
{
  "symbol": "BTCUSD",
  "open": "84914.96",
  "high": "86980",
  "low": "84887.66",
  "close": "85756.83",
  "changes": [
    "84907.59",
    "85044.63",
    "85100",
    "85098.66",
    "85221.21",
    "85268.31",
    "85305.73",
    "85132.28",
    "85245",
    "85279.45",
    "85248.35",
    "85357.94",
    "85307.72",
    "85330.01",
    "85420.02",
    "85819.36",
    "85842.76",
    "86446.54",
    "86521.75",
    "86628.85",
    "86608.57",
    "86512.72",
    "86071.76",
    "85511.91"
  ],
  "bid": "85744.01000",
  "ask": "85744.02000"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
