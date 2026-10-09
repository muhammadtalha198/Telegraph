---
intent: PAYMENT_METHOD_VERIFY
slug: pay-binlist
status: approved
captured_at: 2026-10-05T09:41:06Z
request_url: https://lookup.binlist.net/45717360
content_type: application/json
inputs: |
  {"bin": "45717360"}
intent_description: |
  Verifies card BIN validity, tokenization credentials, bank account routing, and active account standing.
answer_requirement: |
  Must return the validity/details of the card BIN, bank account (IBAN) or routing number asked.
capture_note: |
  golden-test PASS: binlist.net
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the card brand, type, and issuing bank details."
reviewed_at: 2026-10-05T12:34:21Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "number": {},
  "scheme": "visa",
  "type": "debit",
  "brand": "Visa Classic/Dankort",
  "country": {
    "numeric": "208",
    "alpha2": "DK",
    "name": "Denmark",
    "emoji": "🇩🇰",
    "currency": "DKK",
    "latitude": 56,
    "longitude": 10
  },
  "bank": {
    "name": "Jyske Bank A/S"
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the card brand, type, and issuing bank details._
