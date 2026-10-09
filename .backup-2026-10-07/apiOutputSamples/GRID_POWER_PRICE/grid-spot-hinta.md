---
intent: GRID_POWER_PRICE
slug: grid-spot-hinta
status: approved
captured_at: 2026-10-05T09:36:48Z
request_url: https://api.spot-hinta.fi/JustNow
content_type: application/json
inputs: |
  {}
intent_description: |
  Ingests real-time nodal marginal locational prices (LMP) and day-ahead electricity spot rates from regional grid operators.
answer_requirement: |
  Must return current/day-ahead electricity spot prices for the grid region asked.
capture_note: |
  golden-test PASS: spot-hinta.fi
reviewer_note: "auto_review: [1.00|heuristic+llm] API response contains the requested day-ahead electricity spot price."
reviewed_at: 2026-10-05T11:33:09Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "Rank": 84,
  "DateTime": "2026-10-05T12:30:00+03:00",
  "PriceNoTax": 0.015,
  "PriceWithTax": 0.01882
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] API response contains the requested day-ahead electricity spot price._
