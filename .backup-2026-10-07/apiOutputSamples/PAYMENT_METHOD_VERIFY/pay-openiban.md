---
intent: PAYMENT_METHOD_VERIFY
slug: pay-openiban
status: approved
captured_at: 2026-10-05T09:41:06Z
request_url: https://openiban.com/validate/DE89370400440532013000?getBIC=true&validateBankCode=true
content_type: application/json
inputs: |
  {"iban": "DE89370400440532013000"}
intent_description: |
  Verifies card BIN validity, tokenization credentials, bank account routing, and active account standing.
answer_requirement: |
  Must return the validity/details of the card BIN, bank account (IBAN) or routing number asked.
capture_note: |
  golden-test PASS: OpenIBAN
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the validity of the IBAN, the bank code, and the bank's details including the BIC."
reviewed_at: 2026-10-05T11:54:49Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "valid": true,
  "messages": [
    "Bank code valid: 37040044"
  ],
  "iban": "DE89370400440532013000",
  "bankData": {
    "bankCode": "37040044",
    "name": "Commerzbank",
    "zip": "50447",
    "city": "Köln",
    "bic": "COBADEFFXXX"
  },
  "checkResults": {
    "bankCode": true
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the validity of the IBAN, the bank code, and the bank's details including the BIC._
