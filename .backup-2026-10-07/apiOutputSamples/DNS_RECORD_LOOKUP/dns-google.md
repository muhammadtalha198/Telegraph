---
intent: DNS_RECORD_LOOKUP
slug: dns-google
status: pending_review
captured_at: 2026-10-05T09:33:00Z
request_url: https://dns.google/resolve?name=dns.google&type=A
content_type: application/json
inputs: |
  {"name": "dns.google", "type": "A"}
intent_description: |
  Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.
answer_requirement: |
  Must return the DNS records (A/AAAA/CNAME/MX/TXT) for the name and type asked.
capture_note: |
  golden-test PASS: Google Public DNS
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": "dns.google.",
      "type": 1
    }
  ],
  "Answer": [
    {
      "name": "dns.google.",
      "type": 1,
      "TTL": 220,
      "data": "8.8.8.8"
    },
    {
      "name": "dns.google.",
      "type": 1,
      "TTL": 220,
      "data": "8.8.4.4"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
