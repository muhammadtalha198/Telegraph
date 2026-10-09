---
intent: CARRIER_SERVICEABILITY
slug: car-zippopotam
status: approved
captured_at: 2026-10-08T04:42:23Z
request_url: https://api.zippopotam.us/no/0150
content_type: application/json
inputs: |
  {"cc": "NO", "cc_l": "no", "pc": "0150", "locality": "oslo"}
intent_description: |
  Evaluates freight and courier delivery coverage, weight limits, and hazardous material restrictions for target routes.
answer_requirement: |
  Must confirm that the pinned destination postcode (Norway 0150 = OSLO) is a valid, deliverable postal code and return the locality name 'Oslo' (case-insensitive). Proxy for 'lane serviceable or not': weight / hazmat limits are NOT answerable by any keyless source.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response correctly identifies the locality as 'Oslo' for the given postcode."
reviewed_at: 2026-10-08T04:58:32Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "country": "Norway",
  "country abbreviation": "NO",
  "post code": "0150",
  "places": [
    {
      "place name": "Oslo",
      "longitude": "10.7461",
      "latitude": "59.9127",
      "state": "Oslo",
      "state abbreviation": "03"
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response correctly identifies the locality as 'Oslo' for the given postcode._
