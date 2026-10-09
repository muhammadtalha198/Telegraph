---
intent: CORPORATE_REGISTRY_LOOKUP
slug: corp-eu-vies
status: pending_review
captured_at: 2026-10-08T04:42:27Z
request_url: https://ec.europa.eu/taxation_customs/vies/rest-api/ms/PL/vat/7740001454
content_type: application/json
inputs: |
  {"vies_ms": "PL", "vies_vat": "7740001454", "nip": "7740001454", "wl_date": "2026-09-01"}
intent_description: |
  Queries national business registers for incorporation status, registered agent details, and beneficial ownership filings.
answer_requirement: |
  Must return the company's registry record (legal name, status/validity, identifiers) for the pinned company.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "isValid": true,
  "requestDate": "2026-10-08T04:42:27.326Z",
  "userError": "VALID",
  "name": "ORLEN SPÓŁKA AKCYJNA",
  "address": "CHEMIKÓW 7\n09-411 PŁOCK",
  "requestIdentifier": "",
  "originalVatNumber": "7740001454",
  "vatNumber": "7740001454",
  "viesApproximate": {
    "name": "---",
    "street": "---",
    "postalCode": "---",
    "city": "---",
    "companyType": "---",
    "matchName": 3,
    "matchStreet": 3,
    "matchPostalCode": 3,
    "matchCity": 3,
    "matchCompanyType": 3
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
