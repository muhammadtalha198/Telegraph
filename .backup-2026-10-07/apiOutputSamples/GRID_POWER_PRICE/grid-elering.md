---
intent: GRID_POWER_PRICE
slug: grid-elering
status: approved
captured_at: 2026-10-05T09:36:48Z
request_url: https://dashboard.elering.ee/api/nps/price/EE/current
content_type: application/json
inputs: |
  {}
intent_description: |
  Ingests real-time nodal marginal locational prices (LMP) and day-ahead electricity spot rates from regional grid operators.
answer_requirement: |
  Must return current/day-ahead electricity spot prices for the grid region asked.
capture_note: |
  golden-test PASS: Elering (Estonia)
reviewer_note: "auto_review: [1.00|heuristic+llm] API response contains the current electricity spot price for the specified grid region."
reviewed_at: 2026-10-05T11:32:32Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "success": true,
  "data": [
    {
      "timestamp": 1791192600,
      "price": 15.0
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] API response contains the current electricity spot price for the specified grid region._
