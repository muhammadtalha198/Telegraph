---
intent: SSL_CERTIFICATE_VERIFY
slug: ssl-ssllabs
status: pending_review
captured_at: 2026-10-05T09:33:22Z
request_url: https://api.ssllabs.com/api/v3/analyze?host=github.com&fromCache=on&maxAge=48
content_type: application/json
inputs: |
  {"host": "github.com"}
intent_description: |
  Validates TLS/SSL certificate chains, cipher suites, expiration dates, and revocation statuses.
answer_requirement: |
  Must return TLS certificate details (issuer, validity dates, chain/validity status) for the host.
capture_note: |
  golden-test PASS: Qualys SSL Labs
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "host": "github.com",
  "port": 443,
  "protocol": "http",
  "isPublic": false,
  "status": "READY",
  "startTime": 1791178432287,
  "testTime": 1791178527821,
  "engineVersion": "2.4.3",
  "criteriaVersion": "2009q",
  "endpoints": [
    {
      "ipAddress": "140.82.112.4",
      "serverName": "lb-140-82-112-4-iad.github.com",
      "statusMessage": "Ready",
      "grade": "A+",
      "gradeTrustIgnored": "A+",
      "hasWarnings": false,
      "isExceptional": true,
      "progress": 100,
      "duration": 95502,
      "delegation": 1
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
