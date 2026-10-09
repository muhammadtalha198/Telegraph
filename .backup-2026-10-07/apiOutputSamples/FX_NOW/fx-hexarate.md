---
intent: FX_NOW
slug: fx-hexarate
status: approved
captured_at: 2026-10-05T09:37:51Z
request_url: https://hexarate.paikama.co/api/rates/latest/USD?target=EUR
content_type: application/json
inputs: |
  {"base": "USD", "quote": "EUR", "pair": "USDEUR"}
intent_description: |
  Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.
answer_requirement: |
  Must return the current exchange rate between the two currencies asked.
capture_note: |
  golden-test PASS: HexaRate
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the current exchange rate between USD and EUR as requested."
reviewed_at: 2026-10-05T12:19:31Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "status_code": 200,
  "data": {
    "base": "USD",
    "target": "EUR",
    "mid": 0.888494,
    "unit": 1,
    "timestamp": "2026-10-04T23:59:01.509Z"
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the current exchange rate between USD and EUR as requested._
