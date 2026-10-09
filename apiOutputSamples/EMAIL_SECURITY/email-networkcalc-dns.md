---
intent: EMAIL_SECURITY
slug: email-networkcalc-dns
status: rejected
captured_at: 2026-10-08T04:42:34Z
request_url: https://networkcalc.com/api/dns/lookup/gmail.com
content_type: application/json
inputs: |
  {"name": "gmail.com", "wire": "AAABAAABAAAAAAAABWdtYWlsA2NvbQAAEAAB"}
intent_description: |
  Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.
answer_requirement: |
  Must return the domain's SPF/DKIM/DMARC records or a spoofing-protection assessment.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response only provides DNS records for the domain, not specific email security settings."
reviewed_at: 2026-10-08T04:59:41Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "status": "OK",
  "hostname": "gmail.com",
  "records": {
    "A": [
      {
        "address": "142.251.211.197",
        "ttl": 30
      }
    ],
    "CNAME": [],
    "MX": [
      {
        "exchange": "gmail-smtp-in.l.google.com",
        "priority": 5
      },
      {
        "exchange": "alt1.gmail-smtp-in.l.google.com",
        "priority": 10
      },
      {
        "exchange": "alt2.gmail-smtp-in.l.google.com",
        "priority": 20
      },
      {
        "exchange": "alt3.gmail-smtp-in.l.google.com",
        "priority": 30
      },
      {
        "exchange": "alt4.gmail-smtp-in.l.google.com",
        "priority": 40
      }
    ],
    "NS": [
      {
        "nameserver": "ns2.google.com"
      },
      {
        "nameserver": "ns3.google.com"
      },
      {
        "nameserver": "ns1.google.com"
      },
      {
        "nameserver": "ns4.google.com"
      }
    ],
    "SOA": [
      {
        "nameserver": "ns1.google.com",
        "hostmaster": "dns-admin.google.com"
      }
    ],
    "TXT": [
      "globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=",
      "v=spf1 redirect=_spf.google.com",
      "yahoo-verification-key=dKYwfVbaxatmcXiXy6LDAxMRirqpOq5tj98iJv9qWVk=",
      "yahoo-verification-key=+eZwIPSgRxkAUzDtqT8Qhk+j4A1JF6V/wtGoyGTkELY="
    ]
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response only provides DNS records for the domain, not specific email security settings._
