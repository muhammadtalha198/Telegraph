---
intent: FX_NOW
slug: fx-frankfurter
status: pending_review
captured_at: 2026-10-05T09:37:51Z
request_url: https://api.frankfurter.dev/v1/latest?base=USD&symbols=EUR
content_type: application/json
inputs: |
  {"base": "USD", "quote": "EUR", "pair": "USDEUR"}
intent_description: |
  Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.
answer_requirement: |
  Must return the current exchange rate between the two currencies asked.
capture_note: |
  golden-test PASS: ECB via Frankfurter
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "amount": 1.0,
  "base": "USD",
  "date": "2026-10-02",
  "rates": {
    "EUR": 0.89087
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
