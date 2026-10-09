---
intent: DNS_RECORD_LOOKUP
slug: dns-dnssb
status: pending_review
captured_at: 2026-10-05T09:33:00Z
request_url: https://doh.dns.sb/dns-query?name=dns.google&type=A
content_type: application/json
inputs: |
  {"name": "dns.google", "type": "A"}
intent_description: |
  Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.
answer_requirement: |
  Must return the DNS records (A/AAAA/CNAME/MX/TXT) for the name and type asked.
capture_note: |
  golden-test PASS: DNS.SB
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
      "TTL": 166,
      "Expires": "Mon, 05 Oct 2026 09:35:27 UTC",
      "data": "8.8.8.8"
    },
    {
      "name": "dns.google.",
      "type": 1,
      "TTL": 166,
      "Expires": "Mon, 05 Oct 2026 09:35:27 UTC",
      "data": "8.8.4.4"
    },
    {
      "name": "dns.google.",
      "type": 46,
      "TTL": 166,
      "Expires": "Mon, 05 Oct 2026 09:35:27 UTC",
      "data": "A 8 2 900 20261024234900 20261002234900 44839 dns.google. EcKrGPZk0075qpX650Y9zeNH3YfJMmGlz7XRt2x9ijK9D+q4pcJb4wOU8nCHQbzURG5YkHSAgZKZqHnExSdO/0ET9AXFQvSp4NZf6ychoctj8P+76uxIkCSqYO4siRLdBjmJeAzcm+fGQ+CgvVYxOl/1IDkwRicLC9llFS1weKc="
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
