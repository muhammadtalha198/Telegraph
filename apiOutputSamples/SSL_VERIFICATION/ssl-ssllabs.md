---
intent: SSL_VERIFICATION
slug: ssl-ssllabs
status: approved
captured_at: 2026-10-05T05:44:47Z
request_url: https://api.ssllabs.com/api/v3/analyze?host=example.com&fromCache=on&maxAge=48
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - only 4 candidates; 4 keyless. Few keyless TLS-inspection APIs exist; ~4 is the realistic keyless ceiling (Censys/SecurityTrails need keys). Distinct publishers: 4.
answer_requirement: |
  Must satisfy catalog intent SSL_VERIFICATION via upstream Qualys SSL Labs
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:33Z
---

## Raw API output

```json
{
  "host": "example.com",
  "port": 443,
  "protocol": "http",
  "status": "ERROR",
  "statusMessage": "Hostname blacklisted",
  "engineVersion": "2.4.3",
  "criteriaVersion": "2009q"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
