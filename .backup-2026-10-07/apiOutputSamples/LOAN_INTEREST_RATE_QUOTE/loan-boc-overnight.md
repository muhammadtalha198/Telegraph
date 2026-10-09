---
intent: LOAN_INTEREST_RATE_QUOTE
slug: loan-boc-overnight
status: rejected
captured_at: 2026-10-05T09:41:30Z
request_url: https://www.bankofcanada.ca/valet/observations/V39079/json?recent=1
content_type: application/json
inputs: |
  {}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a current lending/mortgage/benchmark interest rate.
capture_note: |
  golden-test PASS: Bank of Canada
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the overnight rate, not a current lending/mortgage/benchmark interest rate."
reviewed_at: 2026-10-05T10:44:27Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "terms": {
    "url": "https://www.bankofcanada.ca/terms/"
  },
  "seriesDetail": {
    "V39079": {
      "label": "Target for the overnight rate (business daily)",
      "description": "Also called the policy interest rate, the average rate that the Bank of Canada wants to see in the market for overnight money market financing. (V39079)",
      "dimension": {
        "key": "d",
        "name": "Date"
      }
    }
  },
  "observations": [
    {
      "d": "2026-10-01",
      "V39079": {
        "v": "2.25"
      }
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the overnight rate, not a current lending/mortgage/benchmark interest rate._
