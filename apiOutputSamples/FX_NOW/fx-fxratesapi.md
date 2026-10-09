---
intent: FX_NOW
slug: fx-fxratesapi
status: approved
captured_at: 2026-10-08T04:41:57Z
request_url: https://api.fxratesapi.com/latest?base=USD&currencies=EUR
content_type: application/json
inputs: |
  {"base": "USD", "quote": "EUR", "pair": "USDEUR"}
intent_description: |
  Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.
answer_requirement: |
  Must return the current exchange rate (units of quote currency per 1 unit of base currency) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the requested USDEUR exchange rate in real-time."
reviewed_at: 2026-10-08T04:55:35Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "success": true,
  "terms": "https://fxratesapi.com/legal/terms-conditions",
  "privacy": "https://fxratesapi.com/legal/privacy-policy",
  "timestamp": 1791434460,
  "date": "2026-10-08T04:41:00.000Z",
  "base": "USD",
  "rates": {
    "EUR": 0.892507177
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the requested USDEUR exchange rate in real-time._
