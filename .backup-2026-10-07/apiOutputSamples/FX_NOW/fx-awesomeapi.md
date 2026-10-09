---
intent: FX_NOW
slug: fx-awesomeapi
status: pending_review
captured_at: 2026-10-05T09:37:51Z
request_url: https://economia.awesomeapi.com.br/json/last/USD-EUR
content_type: application/json
inputs: |
  {"base": "USD", "quote": "EUR", "pair": "USDEUR"}
intent_description: |
  Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.
answer_requirement: |
  Must return the current exchange rate between the two currencies asked.
capture_note: |
  golden-test PASS: AwesomeAPI (Brazil)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "USDEUR": {
    "code": "USD",
    "codein": "EUR",
    "name": "Dólar Americano/Euro",
    "high": "0.89587998",
    "low": "0.8883",
    "varBid": "0.00311",
    "pctChange": "0.350015",
    "bid": "0.89164",
    "ask": "0.89168",
    "timestamp": "1791192923",
    "create_date": "2026-10-05 06:35:23"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
