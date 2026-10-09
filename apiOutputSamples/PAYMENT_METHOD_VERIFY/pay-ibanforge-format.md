---
intent: PAYMENT_METHOD_VERIFY
slug: pay-ibanforge-format
status: pending_review
captured_at: 2026-10-08T04:42:44Z
request_url: https://api.ibanforge.com/v1/iban/format?iban=DE89370400440532013000
content_type: application/json
inputs: |
  {"iban": "DE89370400440532013000"}
intent_description: |
  Verifies card BIN validity, tokenization credentials, bank account routing, and active account standing.
answer_requirement: |
  Must return the validity/details of the card BIN, bank account (IBAN) or routing number asked.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "iban": "DE89370400440532013000",
  "formatted": "DE89 3704 0044 0532 0130 00",
  "valid": true,
  "country": {
    "code": "DE",
    "name": "Germany"
  },
  "check_digits": "89",
  "bban": {
    "bank_code": "37040044",
    "account_number": "0532013000"
  },
  "upgrade_to_full_validation": "valid: true here means the IBAN is well formed (length, structure, mod-97), nothing more. POST /v1/iban/validate ($0.005, or keyless for the first 25 calls a week per source address) names the bank and its BIC with the source of that answer (where we hold bank-code data we may use), SEPA and VoP readiness, and, where it reads the national register (DE, AT, BE, SK, CZ, BG, CH, LI), whether the bank code is allocated at all. Real answers of that full validation, readable with a plain GET: https://api.ibanforge.com/v1/demo"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
