---
intent: LOAN_INTEREST_RATE_QUOTE
slug: loan-nyfed-sofr
status: pending_review
captured_at: 2026-10-05T09:41:30Z
request_url: https://markets.newyorkfed.org/api/rates/secured/sofr/last/1.json
content_type: application/json
inputs: |
  {}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a current lending/mortgage/benchmark interest rate.
capture_note: |
  golden-test PASS: NY Fed SOFR
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "refRates": [
    {
      "effectiveDate": "2026-10-01",
      "type": "SOFR",
      "percentRate": 3.87,
      "percentPercentile1": 3.83,
      "percentPercentile25": 3.84,
      "percentPercentile75": 3.92,
      "percentPercentile99": 3.97,
      "volumeInBillions": 3067,
      "revisionIndicator": ""
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
