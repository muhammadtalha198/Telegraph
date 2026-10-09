---
intent: DNS_RECORD_LOOKUP
slug: dns-networkcalc
status: approved
captured_at: 2026-10-08T04:42:32Z
request_url: https://networkcalc.com/api/dns/lookup/dns.google
content_type: application/json
inputs: |
  {"name": "dns.google", "type": "A", "wire": "AAABAAABAAAAAAAAA2RucwZnb29nbGUAAAEAAQ"}
intent_description: |
  Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.
answer_requirement: |
  Must return the DNS records (A/AAAA/CNAME/MX/TXT) for the name and type asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the requested A records for dns.google."
reviewed_at: 2026-10-08T04:59:38Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "status": "OK",
  "hostname": "dns.google",
  "records": {
    "A": [
      {
        "address": "8.8.8.8",
        "ttl": 30
      },
      {
        "address": "8.8.4.4",
        "ttl": 30
      }
    ],
    "CNAME": [],
    "MX": [],
    "NS": [
      {
        "nameserver": "ns3.zdns.google"
      },
      {
        "nameserver": "ns4.zdns.google"
      },
      {
        "nameserver": "ns1.zdns.google"
      },
      {
        "nameserver": "ns2.zdns.google"
      }
    ],
    "SOA": [
      {
        "nameserver": "ns1.zdns.google",
        "hostmaster": "cloud-dns-hostmaster.google.com"
      }
    ],
    "TXT": [
      "https://xkcd.com/1361/",
      "v=spf1 -all"
    ]
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the requested A records for dns.google._
