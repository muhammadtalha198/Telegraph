---
intent: EMAIL_SECURITY
slug: email-doh-alidns
status: approved
captured_at: 2026-10-05T09:40:57Z
request_url: https://dns.alidns.com/resolve?name=gmail.com&type=TXT
content_type: application/json
inputs: |
  {"name": "gmail.com"}
intent_description: |
  Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.
answer_requirement: |
  Must return the domain's SPF/DKIM/DMARC records or a spoofing-protection assessment.
capture_note: |
  golden-test PASS: AliDNS
reviewer_note: "auto_review: [1.00|heuristic+llm] SPF records are provided but no comprehensive email security details are given."
reviewed_at: 2026-10-05T11:26:19Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
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
  "Question": {
    "name": "gmail.com.",
    "type": 16
  },
  "Answer": [
    {
      "name": "gmail.com.",
      "TTL": 300,
      "type": 16,
      "data": "\"v=spf1 redirect=_spf.google.com\""
    },
    {
      "name": "gmail.com.",
      "TTL": 300,
      "type": 16,
      "data": "\"yahoo-verification-key=+eZwIPSgRxkAUzDtqT8Qhk+j4A1JF6V/wtGoyGTkELY=\""
    },
    {
      "name": "gmail.com.",
      "TTL": 300,
      "type": 16,
      "data": "\"globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=\""
    },
    {
      "name": "gmail.com.",
      "TTL": 300,
      "type": 16,
      "data": "\"yahoo-verification-key=dKYwfVbaxatmcXiXy6LDAxMRirqpOq5tj98iJv9qWVk=\""
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] SPF records are provided but no comprehensive email security details are given._
