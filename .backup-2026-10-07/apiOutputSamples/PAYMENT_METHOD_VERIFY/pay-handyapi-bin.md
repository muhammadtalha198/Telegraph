---
intent: PAYMENT_METHOD_VERIFY
slug: pay-handyapi-bin
status: approved
captured_at: 2026-10-05T09:41:06Z
request_url: https://data.handyapi.com/bin/45717360
content_type: application/json
inputs: |
  {"bin": "45717360"}
intent_description: |
  Verifies card BIN validity, tokenization credentials, bank account routing, and active account standing.
answer_requirement: |
  Must return the validity/details of the card BIN, bank account (IBAN) or routing number asked.
capture_note: |
  golden-test PASS: HandyAPI BIN
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the card scheme, type, issuer, card tier, country details and Luhn validation for the provided BIN."
reviewed_at: 2026-10-05T11:54:30Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "Status": "SUCCESS",
  "Scheme": "VISA",
  "Type": "DEBIT",
  "Issuer": "JYSKE BANK",
  "CardTier": "DANKORT",
  "Country": {
    "A2": "DK",
    "A3": "DNK",
    "N3": "208",
    "ISD": "45",
    "Name": "Denmark",
    "Cont": "Europe"
  },
  "Luhn": true
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the card scheme, type, issuer, card tier, country details and Luhn validation for the provided BIN._
