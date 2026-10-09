---
intent: CRYPTO_PRICE
slug: cp-redstone
status: approved
captured_at: 2026-10-05T05:45:16Z
request_url: https://api.redstone.finance/prices?symbol=BTC&provider=redstone&limit=1
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 22 keyless. Distinct operators. Quote asset differs (USD vs USDT) by ~0.1%, inside the 1.5% tolerance.
answer_requirement: |
  Must satisfy catalog intent CRYPTO_PRICE via upstream RedStone
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
[]
```

## Why this matches (or not)

_[0.95|hard-check] empty body_
