---
intent: CRYPTO_PRICE
slug: cp-kraken
status: approved
captured_at: 2026-10-05T05:45:09Z
request_url: https://api.kraken.com/0/public/Ticker?pair={kraken_pair}
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream Kraken
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
{
  "error": [
    "EQuery:Unknown asset pair"
  ]
}
```

## Why this matches (or not)

_[0.95|hard-check] JSON error object_
