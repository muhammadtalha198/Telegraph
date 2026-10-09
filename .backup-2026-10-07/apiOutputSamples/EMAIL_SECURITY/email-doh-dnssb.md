---
intent: EMAIL_SECURITY
slug: email-doh-dnssb
status: rejected
captured_at: 2026-10-05T09:40:57Z
request_url: https://doh.dns.sb/dns-query?name=gmail.com&type=TXT
content_type: application/json
inputs: |
  {"name": "gmail.com"}
intent_description: |
  Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.
answer_requirement: |
  Must return the domain's SPF/DKIM/DMARC records or a spoofing-protection assessment.
capture_note: |
  golden-test PASS: DNS.SB
reviewer_note: "auto_review: [1.00|heuristic+llm] The response lacks DMARC record information and does not assess email security measures."
reviewed_at: 2026-10-05T10:44:23Z
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
      "Expires": "Mon, 05 Oct 2026 09:45:50 UTC",
      "data": "\"yahoo-verification-key=dKYwfVbaxatmcXiXy6LDAxMRirqpOq5tj98iJv9qWVk=\""
    },
    {
      "name": "gmail.com.",
      "type": 16,
      "TTL": 300,
      "Expires": "Mon, 05 Oct 2026 09:45:50 UTC",
      "data": "\"v=spf1 redirect=_spf.google.com\""
    },
    {
      "name": "gmail.com.",
      "type": 16,
      "TTL": 300,
      "Expires": "Mon, 05 Oct 2026 09:45:50 UTC",
      "data": "\"yahoo-verification-key=+eZwIPSgRxkAUzDtqT8Qhk+j4A1JF6V/wtGoyGTkELY=\""
    },
    {
      "name": "gmail.com.",
      "type": 16,
      "TTL": 300,
      "Expires": "Mon, 05 Oct 2026 09:45:50 UTC",
      "data": "\"globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8=\""
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response lacks DMARC record information and does not assess email security measures._
