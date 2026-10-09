---
intent: ROUTE_ETA
slug: eta-osrm-fossgis
status: approved
captured_at: 2026-10-05T09:36:16Z
request_url: https://routing.openstreetmap.de/routed-car/route/v1/driving/13.405,52.52;11.582,48.1351?overview=false
content_type: application/json
inputs: |
  {"lat1": "52.52", "lon1": "13.405", "lat2": "48.1351", "lon2": "11.582", "vjson": "%7B%22locations%22%3A%5B%7B%22lat%22%3A52.52%2C%22lon%22%3A13.405%7D%2C%7B%22lat%22%3A48.1351%2C%22lon%22%3A11.582%7D%5D%2C%22costing%22%3A%22auto%22%7D"}
intent_description: |
  Computes multimodal routing itineraries, live traffic transit times, and turn-by-turn arrival estimations.
answer_requirement: |
  Must return the driving travel time/distance between the two points.
capture_note: |
  golden-test PASS: OSRM (routing.openstreetmap.de)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the driving travel time/distance between the two points as 21085.4 seconds."
reviewed_at: 2026-10-05T11:55:40Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "code": "Ok",
  "routes": [
    {
      "legs": [
        {
          "steps": [],
          "weight": 21085.4,
          "summary": "",
          "duration": 21085.4,
          "distance": 585248.6
        }
      ],
      "weight_name": "routability",
      "weight": 21085.4,
      "duration": 21085.4,
      "distance": 585248.6
    }
  ],
  "waypoints": [
    {
      "hint": "Tio4hf___38CAAAABAAAAF8AAAAAAAAAfPYRQOBO3D_7t6ZCAAAAAAIAAAAEAAAAXwAAAAAAAAAvKAEAS4vMAEFkIQNIi8wAQGQhAwoAHxQAAAAA",
      "location": [
        13.405003,
        52.520001
      ],
      "name": "Spandauer Straße",
      "distance": 0.2320382638
    },
    {
      "hint": "F1wBgP___38EAAAADwAAABQAAAAYAAAASkEoQGTY5UD66oVB1yyAQQQAAAAPAAAAFAAAABgAAAAvKAEArrqwABl83gIwurAAvHveAgQAfxMAAAAA",
      "location": [
        11.582126,
        48.135193
      ],
      "name": "Tal",
      "distance": 13.96138374
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the driving travel time/distance between the two points as 21085.4 seconds._
