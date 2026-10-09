---
intent: VENDOR_VERIFY
slug: vendor-vatcomply
status: approved
captured_at: 2026-10-05T09:41:08Z
request_url: https://api.vatcomply.com/vat?vat_number=IE6388047V
content_type: application/json
inputs: |
  {"cc": "IE", "num": "6388047V", "full": "IE6388047V"}
intent_description: |
  Audits vendor tax identifiers, compliance credentials, banking details, and sanctions list clearance.
answer_requirement: |
  Must return whether the vendor tax/VAT ID is valid and the registered business details.
capture_note: |
  golden-test PASS: VATcomply
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the required information about the vendor's tax/VAT ID and registered business details."
reviewed_at: 2026-10-05T12:00:28Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "valid": true,
  "vat_number": "6388047V",
  "country_code": "IE",
  "name": "GOOGLE IRELAND LIMITED",
  "address": "3RD FLOOR, GORDON HOUSE, BARROW STREET, DUBLIN 4"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the required information about the vendor's tax/VAT ID and registered business details._
