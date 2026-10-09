---
intent: MACRO_ECONOMIC_INDICATOR
slug: macro-statcan-wds
status: approved
captured_at: 2026-10-08T04:42:41Z
request_url: https://www150.statcan.gc.ca/t1/wds/rest/getDataFromVectorByReferencePeriodRange?vectorIds=%222062815%22&startRefPeriod=2019-12-01&endReferencePeriod=2019-12-01
content_type: application/json
inputs: |
  {"oecd_ref": "CAN", "oecd_freq": "M", "period": "2019-12"}
intent_description: |
  Aggregates released central bank interest rates, consumer price index (CPI) updates, and unemployment figures.
answer_requirement: |
  Must return the unemployment rate (percent of labour force, ages 15+, total sexes) for the pinned country and period as a plain number.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the exact unemployment rate for Canada in the specified period."
reviewed_at: 2026-10-08T05:00:30Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "status": "SUCCESS",
    "object": {
      "responseStatusCode": 0,
      "productId": 14100287,
      "coordinate": "1.7.1.1.1.1.0.0.0.0",
      "vectorId": 2062815,
      "vectorDataPoint": [
        {
          "refPer": "2019-12-01",
          "refPer2": "",
          "refPerRaw": "2019-12-01",
          "refPerRaw2": "",
          "value": 5.6,
          "decimals": 1,
          "scalarFactorCode": 0,
          "symbolCode": 0,
          "statusCode": 0,
          "securityLevelCode": 0,
          "releaseTime": "2025-01-24T08:30",
          "frequencyCode": 6
        }
      ]
    }
  }
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the exact unemployment rate for Canada in the specified period._
