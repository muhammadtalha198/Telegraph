---
intent: DNS_RECORD_LOOKUP
slug: dns-nextdns
status: pending_review
captured_at: 2026-10-05T09:33:00Z
request_url: https://dns.nextdns.io/dns-query?name=dns.google&type=A
content_type: application/json
inputs: |
  {"name": "dns.google", "type": "A"}
intent_description: |
  Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.
answer_requirement: |
  Must return the DNS records (A/AAAA/CNAME/MX/TXT) for the name and type asked.
capture_note: |
  golden-test PASS: NextDNS
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
      "TTL": 639,
      "data": "8.8.4.4"
    },
    {
      "name": "dns.google.",
      "type": 1,
      "TTL": 639,
      "data": "8.8.8.8"
    }
  ],
  "Additional": [
    {
      "name": ".",
      "type": 41,
      "TTL": 0,
      "data": "\n;; OPT PSEUDOSECTION:\n; EDNS: version 0; flags:; udp: 1232"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
