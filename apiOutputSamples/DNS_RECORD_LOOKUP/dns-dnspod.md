---
intent: DNS_RECORD_LOOKUP
slug: dns-dnspod
status: pending_review
captured_at: 2026-10-05T09:33:00Z
request_url: https://doh.pub/dns-query?name=dns.google&type=A
content_type: application/json
inputs: |
  {"name": "dns.google", "type": "A"}
intent_description: |
  Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.
answer_requirement: |
  Must return the DNS records (A/AAAA/CNAME/MX/TXT) for the name and type asked.
capture_note: |
  golden-test PASS: DNSPod (Tencent)
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
  "AD": false,
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
      "TTL": 393,
      "data": "8.8.8.8"
    },
    {
      "name": "dns.google.",
      "type": 1,
      "TTL": 393,
      "data": "8.8.4.4"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
