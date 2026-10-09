---
intent: MACRO_ECONOMIC_INDICATOR
slug: macro-bls
status: approved
captured_at: 2026-10-05T09:36:33Z
request_url: https://api.bls.gov/publicAPI/v1/timeseries/data/
content_type: application/json
inputs: |
  {"iso2": "US", "iso3": "USA"}
intent_description: |
  Aggregates released central bank interest rates, consumer price index (CPI) updates, and unemployment figures.
answer_requirement: |
  Must return the requested macro indicator value (unemployment / CPI / policy rate) for the country and period.
capture_note: |
  golden-test PASS: US BLS
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the requested unemployment rate for the US, but it only covers the period from January 2019 to December 2019."
reviewed_at: 2026-10-05T12:36:05Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "status": "REQUEST_SUCCEEDED",
  "responseTime": 75,
  "message": [],
  "Results": {
    "series": [
      {
        "seriesID": "LNS14000000",
        "data": [
          {
            "year": "2019",
            "period": "M12",
            "periodName": "December",
            "value": "3.6",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M11",
            "periodName": "November",
            "value": "3.6",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M10",
            "periodName": "October",
            "value": "3.6",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M09",
            "periodName": "September",
            "value": "3.5",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M08",
            "periodName": "August",
            "value": "3.6",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M07",
            "periodName": "July",
            "value": "3.7",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M06",
            "periodName": "June",
            "value": "3.6",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M05",
            "periodName": "May",
            "value": "3.6",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M04",
            "periodName": "April",
            "value": "3.7",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M03",
            "periodName": "March",
            "value": "3.8",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M02",
            "periodName": "February",
            "value": "3.8",
            "footnotes": [
              {}
            ]
          },
          {
            "year": "2019",
            "period": "M01",
            "periodName": "January",
            "value": "4.0",
            "footnotes": [
              {}
            ]
          }
        ]
      }
    ]
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the requested unemployment rate for the US, but it only covers the period from January 2019 to December 2019._
