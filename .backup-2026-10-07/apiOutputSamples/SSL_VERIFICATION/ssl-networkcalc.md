---
intent: SSL_VERIFICATION
slug: ssl-networkcalc
status: approved
captured_at: 2026-10-05T05:44:48Z
request_url: https://networkcalc.com/api/security/certificate/example.com
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - only 4 candidates; 4 keyless. Few keyless TLS-inspection APIs exist; ~4 is the realistic keyless ceiling (Censys/SecurityTrails need keys). Distinct publishers: 4.
answer_requirement: |
  Must satisfy catalog intent SSL_VERIFICATION via upstream NetworkCalc
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:33Z
---

## Raw API output

```json
{
  "status": "OK",
  "meta": {
    "protocol": "https:",
    "hostname": "example.com",
    "port": 443
  },
  "certificate": {
    "protocol": "https:",
    "hostname": "example.com",
    "port": 443,
    "issued_to": "example.com",
    "issued_by": "Cloudflare TLS Issuing ECC CA 3",
    "valid_from": "2026-09-26T22:49:11.000Z",
    "valid_to": "2026-12-25T22:56:35.000Z",
    "alternate_names": [
      "DNS:example.com",
      "DNS:*.example.com"
    ],
    "serial_number": "01EEE6AABB521D5E14FC315FD9985690",
    "fingerprint": "89:9C:B2:59:E7:DE:8D:F1:00:33:A2:AF:48:C2:2C:2F:65:80:A2:1D",
    "raw": "-----BEGIN CERTIFICATE-----\nMIID5jCCA42gAwIBAgIQAe7mqrtSHV4U/DFf2ZhWkDAKBggqhkjOPQQDAjBRMQsw\nCQYDVQQGEwJVUzEYMBYGA1UECgwPU1NMIENvcnBvcmF0aW9uMSgwJgYDVQQDDB9D\nbG91ZGZsYXJlIFRMUyBJc3N1aW5nIEVDQyBDQSAzMB4XDTI2MDkyNjIyNDkxMVoX\nDTI2MTIyNTIyNTYzNVowFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wWTATBgcqhkjO\nPQIBBggqhkjOPQMBBwNCAARqadExWzxTJ4S3LSzKIzAAeyF09q0Qt0F0XmLiZiaJ\nSD0SQPhVK36pUKlM55TUstJnrU7f+7elE0kZESKzzcbto4ICgDCCAnwwDAYDVR0T\nAQH/BAIwADAfBgNVHSMEGDAWgBSDA/3n9vVKTRVB9O0iFtMyCj7KZjBsBggrBgEF\nBQcBAQRgMF4wOQYIKwYBBQUHMAKGLWh0dHA6Ly9pLmNmLWkuc3NsLmNvbS9DbG91\nZGZsYXJlLVRMUy1JLUUzLmNlcjAhBggrBgEFBQcwAYYVaHR0cDovL28uY2YtaS5z\nc2wuY29tMCUGA1UdEQQeMByCC2V4YW1wbGUuY29tgg0qLmV4YW1wbGUuY29tMCMG\nA1UdIAQcMBowCAYGZ4EMAQIBMA4GDCsGAQQBgqkwAQMBATATBgNVHSUEDDAKBggr\nBgEFBQcDATBTBgNVHR8ETDBKMEigRqBEhkJodHRwOi8vYy5jZi1pLnNzbC5jb20v\nYWU4MDFlZDFjNTViYjU3OWQ3OTIwOGIwZDc3MmFjZmI4Y2MzYTIwOC5jcmwwDgYD\nVR0PAQH/BAQDAgeAMA8GCSsGAQQBgtpLLAQCBQAwggEEBgorBgEEAdZ5AgQCBIH1\nBIHyAPAAdgCUTkOH+uzB74HzGSQmqBhlAcfTXzgCAT9yZ31VNy4Z2AAAAaDf8a1i\nAAAEAwBHMEUCIQCuCUahRazwOcqj3A77y8eXdQBpLlGCjv9D/xvXd3X7hAIgbc0K\nMS+MsANY5WLGpHgTk3Uxk0g1VWTQB78vYRMga1EAdgDLOPcViXyEoURfW8Hd+8lu\n8ppZzUcKaQWFsMsUwxRY5wAAAaDf8a1+AAAEAwBHMEUCIB2YN/lZP6eSBMtV0BTr\nGD7KSyKVu/i68Zza97li96FcAiEA1mtvTnM8zbNKj6ArUpWmgTRURDDgOC4R1C2W\n5cSK6fIwCgYIKoZIzj0EAwIDRwAwRAIgNGlXxWLTTqn5+XQOkP06fTgaEbjDMAHU\nILmIapx8i5sCIAeTI/xpafGZNB9HwNfEeU05yh+aSv95pD8SNtIAWNr0\n-----END CERTIFICATE-----"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
