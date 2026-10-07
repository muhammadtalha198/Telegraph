---
intent: MACRO_ECONOMIC_INDICATOR
slug: macro-worldbank
status: pending_review
captured_at: 2026-10-05T09:36:33Z
request_url: https://api.worldbank.org/v2/country/US/indicator/SL.UEM.TOTL.ZS?date=2019&format=json
content_type: application/json
inputs: |
  {"iso2": "US", "iso3": "USA"}
intent_description: |
  Aggregates released central bank interest rates, consumer price index (CPI) updates, and unemployment figures.
answer_requirement: |
  Must return the requested macro indicator value (unemployment / CPI / policy rate) for the country and period.
capture_note: |
  golden-test PASS: World Bank (ILO modelled)
reviewer_note: ""
reviewed_at: ""
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
        "id": "SL.UEM.TOTL.ZS",
        "value": "Unemployment, total (% of total labor force) (modeled ILO estimate)"
      },
      "country": {
        "id": "US",
        "value": "United States"
      },
      "countryiso3code": "USA",
      "date": "2019",
      "value": 3.669,
      "unit": "",
      "obs_status": "",
      "decimal": 1
    }
  ]
]
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
