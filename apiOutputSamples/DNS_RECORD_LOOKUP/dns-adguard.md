---
intent: DNS_RECORD_LOOKUP
slug: dns-adguard
status: pending_review
captured_at: 2026-10-05T09:33:00Z
request_url: https://dns.adguard-dns.com/resolve?name=dns.google&type=A
content_type: application/json
inputs: |
  {"name": "dns.google", "type": "A"}
intent_description: |
  Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.
answer_requirement: |
  Must return the DNS records (A/AAAA/CNAME/MX/TXT) for the name and type asked.
capture_note: |
  golden-test PASS: AdGuard DNS
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "Question": [
    {
      "name": "dns.google.",
      "type": 1
    }
  ],
  "Answer": [
    {
      "name": "dns.google.",
      "data": "8.8.4.4",
      "TTL": 606,
      "type": 1,
      "class": 1
    },
    {
      "name": "dns.google.",
      "data": "8.8.8.8",
      "TTL": 606,
      "type": 1,
      "class": 1
    }
  ],
  "Extra": null,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": false,
  "CD": false,
  "Status": 0
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
