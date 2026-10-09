---
intent: EMAIL_SECURITY
slug: email-doh-adguard
status: approved
captured_at: 2026-10-05T09:40:57Z
request_url: https://dns.adguard-dns.com/resolve?name=gmail.com&type=TXT
content_type: application/json
inputs: |
  {"name": "gmail.com"}
intent_description: |
  Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.
answer_requirement: |
  Must return the domain's SPF/DKIM/DMARC records or a spoofing-protection assessment.
capture_note: |
  golden-test PASS: AdGuard DNS
reviewer_note: "auto_review: [1.00|heuristic+llm] SPF records are provided but no DKIM or DMARC records are present."
reviewed_at: 2026-10-05T11:26:00Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "Question": [
    {
      "name": "gmail.com.",
      "type": 16
    }
  ],
  "Answer": [
    {
      "name": "gmail.com.",
      "data": "\"v=spf1 redirect=_spf.google.com\"",
      "TTL": 300,
      "type": 16,
      "class": 1
    },
    {
      "name": "gmail.com.",
      "data": "\"yahoo-verification-key=dKYwfVbaxatmcXiXy6LDAxMRirqpOq5tj98iJv9qWVk=\"",
      "TTL": 300,
      "type": 16,
      "class": 1
    },
    {
      "name": "gmail.com.",
      "data": "\"yahoo-verification-key=+eZwIPSgRxkAUzDtqT8Qhk+j4A1JF6V/wtGoyGTkELY=\"",
      "TTL": 300,
      "type": 16,
      "class": 1
    },
    {
      "name": "gmail.com.",
      "data": "\"globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=\"",
      "TTL": 300,
      "type": 16,
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

_[1.00|heuristic+llm] SPF records are provided but no DKIM or DMARC records are present._
