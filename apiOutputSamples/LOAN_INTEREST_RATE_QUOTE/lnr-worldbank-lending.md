---
intent: LOAN_INTEREST_RATE_QUOTE
slug: lnr-worldbank-lending
status: approved
captured_at: 2026-10-08T04:42:08Z
request_url: https://api.worldbank.org/v2/country/US/indicator/FR.INR.LEND?date=2019&format=json
content_type: application/json
inputs: |
  {"wb_iso2": "US", "year": "2019"}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a published lending / policy / benchmark interest rate (percent) for the pinned country and date or period.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the 2019 lending interest rate for the US, which directly answers the intent."
reviewed_at: 2026-10-08T04:56:46Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "page": 1,
    "pages": 1,
    "per_page": 50,
    "total": 1,
    "sourceid": "2",
    "lastupdated": "2026-07-13"
  },
  [
    {
      "indicator": {
        "id": "FR.INR.LEND",
        "value": "Lending interest rate (%)"
      },
      "country": {
        "id": "US",
        "value": "United States"
      },
      "countryiso3code": "USA",
      "date": "2019",
      "value": 5.2825,
      "unit": "",
      "obs_status": "",
      "decimal": 1
    }
  ]
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the 2019 lending interest rate for the US, which directly answers the intent._
