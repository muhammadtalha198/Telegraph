---
intent: PAYMENT_METHOD_VERIFY
slug: pay-binlist-io
status: approved
captured_at: 2026-10-05T09:41:06Z
request_url: https://binlist.io/lookup/45717360/
content_type: application/json
inputs: |
  {"bin": "45717360"}
intent_description: |
  Verifies card BIN validity, tokenization credentials, bank account routing, and active account standing.
answer_requirement: |
  Must return the validity/details of the card BIN, bank account (IBAN) or routing number asked.
capture_note: |
  golden-test PASS: binlist.io
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the card scheme (VISA), type (DEBIT), category (DANKORT), country (DENMARK), and bank details."
reviewed_at: 2026-10-05T12:34:00Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "number": {
    "iin": "45717360",
    "length": 16,
    "luhn": true
  },
  "scheme": "VISA",
  "type": "DEBIT",
  "category": "DANKORT",
  "country": {
    "alpha2": "DK",
    "alpha3": "DNK",
    "name": "DENMARK",
    "emoji": "🇩🇰"
  },
  "bank": {
    "name": "JYSKE BANK",
    "phone": "89 89 89 89",
    "url": "www.jyskebank.dk"
  },
  "success": true
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the card scheme (VISA), type (DEBIT), category (DANKORT), country (DENMARK), and bank details._
