---
intent: EMAIL_SECURITY
slug: email-hackertarget
status: rejected
captured_at: 2026-10-05T09:40:57Z
request_url: https://api.hackertarget.com/dnslookup/?q=gmail.com
content_type: application/json
inputs: |
  {"name": "gmail.com"}
intent_description: |
  Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.
answer_requirement: |
  Must return the domain's SPF/DKIM/DMARC records or a spoofing-protection assessment.
capture_note: |
  golden-test PASS: HackerTarget
reviewer_note: "auto_review: [1.00|heuristic+llm] The response lacks the specific records needed for email security verification."
reviewed_at: 2026-10-05T10:44:26Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```text
A : 108.177.14.18
A : 108.177.14.17
A : 108.177.14.19
A : 108.177.14.83
AAAA : 2a00:1450:4010:c0f::13
AAAA : 2a00:1450:4010:c0f::11
AAAA : 2a00:1450:4010:c0f::53
AAAA : 2a00:1450:4010:c0f::12
MX : 10 alt1.gmail-smtp-in.l.google.com.
MX : 5 gmail-smtp-in.l.google.com.
MX : 40 alt4.gmail-smtp-in.l.google.com.
MX : 30 alt3.gmail-smtp-in.l.google.com.
MX : 20 alt2.gmail-smtp-in.l.google.com.
NS : ns4.google.com.
NS : ns1.google.com.
NS : ns3.google.com.
NS : ns2.google.com.
TXT : yahoo-verification-key=+eZwIPSgRxkAUzDtqT8Qhk+j4A1JF6V/wtGoyGTkELY=
TXT : yahoo-verification-key=dKYwfVbaxatmcXiXy6LDAxMRirqpOq5tj98iJv9qWVk=
TXT : globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=
TXT : v=spf1 redirect=_spf.google.com
SOA : ns1.google.com. dns-admin.google.com. 993157628 900 900 1800 60
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response lacks the specific records needed for email security verification._
