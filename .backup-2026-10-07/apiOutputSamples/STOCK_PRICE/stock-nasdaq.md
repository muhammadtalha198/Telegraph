---
intent: STOCK_PRICE
slug: stock-nasdaq
status: approved
captured_at: 2026-10-05T05:45:07Z
request_url: https://api.nasdaq.com/api/quote/BTC/info?assetclass=stocks
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 4 keyless.
answer_requirement: |
  Must satisfy catalog intent STOCK_PRICE via upstream Nasdaq.com
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:33Z
---

## Raw API output

```json
{
  "data": null,
  "message": null,
  "status": {
    "rCode": 400,
    "bCodeMessage": [
      {
        "code": 1001,
        "errorMessage": "Symbol not exists."
      }
    ],
    "developerMessage": null
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
