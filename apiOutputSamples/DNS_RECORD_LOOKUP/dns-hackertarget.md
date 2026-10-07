---
intent: DNS_RECORD_LOOKUP
slug: dns-hackertarget
status: pending_review
captured_at: 2026-10-05T09:33:00Z
request_url: https://api.hackertarget.com/dnslookup/?q=dns.google
content_type: application/json
inputs: |
  {"name": "dns.google", "type": "A"}
intent_description: |
  Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.
answer_requirement: |
  Must return the DNS records (A/AAAA/CNAME/MX/TXT) for the name and type asked.
capture_note: |
  golden-test PASS: HackerTarget
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```text
A : 8.8.8.8
A : 8.8.4.4
AAAA : 2001:4860:4860::8888
AAAA : 2001:4860:4860::8844
NS : ns4.zdns.google.
NS : ns3.zdns.google.
NS : ns1.zdns.google.
NS : ns2.zdns.google.
TXT : https://xkcd.com/1361/
TXT : v=spf1 -all
SOA : ns1.zdns.google. cloud-dns-hostmaster.google.com. 1 21600 3600 259200 300
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
