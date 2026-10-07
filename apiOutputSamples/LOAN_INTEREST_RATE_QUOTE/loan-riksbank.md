---
intent: LOAN_INTEREST_RATE_QUOTE
slug: loan-riksbank
status: pending_review
captured_at: 2026-10-05T09:41:30Z
request_url: https://api.riksbank.se/swea/v1/Observations/Latest/SECBREPOEFF
content_type: application/json
inputs: |
  {}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a current lending/mortgage/benchmark interest rate.
capture_note: |
  golden-test PASS: Riksbank (Sweden)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "date": "2026-10-05",
  "value": 1.75
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
