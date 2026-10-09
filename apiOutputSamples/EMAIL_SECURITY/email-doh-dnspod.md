---
intent: EMAIL_SECURITY
slug: email-doh-dnspod
status: pending_review
captured_at: 2026-10-05T09:40:57Z
request_url: https://doh.pub/dns-query?name=gmail.com&type=TXT
content_type: application/json
inputs: |
  {"name": "gmail.com"}
intent_description: |
  Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.
answer_requirement: |
  Must return the domain's SPF/DKIM/DMARC records or a spoofing-protection assessment.
capture_note: |
  golden-test PASS: DNSPod
reviewer_note: "2026-10-07 re-review: judge approved but its own reason says the answer is missing (enum-echo/contradiction bug, fixed)"
reviewed_at: ""
review_source: manual
review_mode: manual
llm_used: false
review_confidence: 1.000
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
      "name": "gmail.com.",
      "type": 16
    }
  ],
  "Answer": [
    {
      "name": "gmail.com.",
      "type": 16,
      "TTL": 300,
      "data": "\"yahoo-verification-key=dKYwfVbaxatmcXiXy6LDAxMRirqpOq5tj98iJv9qWVk=\""
    },
    {
      "name": "gmail.com.",
      "type": 16,
      "TTL": 300,
      "data": "\"v=spf1 redirect=_spf.google.com\""
    },
    {
      "name": "gmail.com.",
      "type": 16,
      "TTL": 300,
      "data": "\"yahoo-verification-key=+eZwIPSgRxkAUzDtqT8Qhk+j4A1JF6V/wtGoyGTkELY=\""
    },
    {
      "name": "gmail.com.",
      "type": 16,
      "TTL": 300,
      "data": "\"globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=\""
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains relevant SPF and DKIM records but lacks DMARC information needed for a complete email security assessment._
