---
intent: SSL_CERTIFICATE_VERIFY
slug: ssl-networkcalc
status: pending_review
captured_at: 2026-10-05T09:33:22Z
request_url: https://networkcalc.com/api/security/certificate/github.com
content_type: application/json
inputs: |
  {"host": "github.com"}
intent_description: |
  Validates TLS/SSL certificate chains, cipher suites, expiration dates, and revocation statuses.
answer_requirement: |
  Must return TLS certificate details (issuer, validity dates, chain/validity status) for the host.
capture_note: |
  golden-test PASS: NetworkCalc
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "status": "OK",
  "meta": {
    "protocol": "https:",
    "hostname": "github.com",
    "port": 443
  },
  "certificate": {
    "protocol": "https:",
    "hostname": "github.com",
    "port": 443,
    "issued_to": "github.com",
    "issued_by": "Sectigo Public Server Authentication CA DV E36",
    "valid_from": "2026-09-01T00:00:00.000Z",
    "valid_to": "2026-11-29T23:59:59.000Z",
    "alternate_names": [
      "DNS:github.com",
      "DNS:www.github.com"
    ],
    "serial_number": "A59EBDB596751DB7F5C095079613953C",
    "fingerprint": "D3:B6:3E:61:C6:4F:D2:9B:A9:B8:72:96:28:F8:69:7F:55:6A:34:1F",
    "raw": "-----BEGIN CERTIFICATE-----\nMIID7TCCA5SgAwIBAgIRAKWevbWWdR239cCVB5YTlTwwCgYIKoZIzj0EAwIwYDEL\nMAkGA1UEBhMCR0IxGDAWBgNVBAoTD1NlY3RpZ28gTGltaXRlZDE3MDUGA1UEAxMu\nU2VjdGlnbyBQdWJsaWMgU2VydmVyIEF1dGhlbnRpY2F0aW9uIENBIERWIEUzNjAe\nFw0yNjA5MDEwMDAwMDBaFw0yNjExMjkyMzU5NTlaMBUxEzARBgNVBAMTCmdpdGh1\nYi5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASFNhs0vLNR9yDpqprL6Cct\nYNExex040djH16D6WrHxLyjnmVFGYSI4sj6wK3V17ADiaabPE04vQk76djW0DT8q\no4ICeDCCAnQwHwYDVR0jBBgwFoAUF5moBMFv5C1wqAoQPQPT6Rq4JmMwHQYDVR0O\nBBYEFGaY7EwRNfdLUISLqBw2ZdAXVtTgMA4GA1UdDwEB/wQEAwIHgDAMBgNVHRMB\nAf8EAjAAMBMGA1UdJQQMMAoGCCsGAQUFBwMBMEkGA1UdIARCMEAwNAYLKwYBBAGy\nMQECAgcwJTAjBggrBgEFBQcCARYXaHR0cHM6Ly9zZWN0aWdvLmNvbS9DUFMwCAYG\nZ4EMAQIBMIGEBggrBgEFBQcBAQR4MHYwTwYIKwYBBQUHMAKGQ2h0dHA6Ly9jcnQu\nc2VjdGlnby5jb20vU2VjdGlnb1B1YmxpY1NlcnZlckF1dGhlbnRpY2F0aW9uQ0FE\nVkUzNi5jcnQwIwYIKwYBBQUHMAGGF2h0dHA6Ly9vY3NwLnNlY3RpZ28uY29tMIIB\nBAYKKwYBBAHWeQIEAgSB9QSB8gDwAHYA1219ENGn9XfCx+lf1wC/+YLJM1pl4dCz\nAXMXwMjFaXcAAAGgWk2g0QAABAMARzBFAiB6u6CCyQsap+pmTuz7Ab9THPLWVtQR\nPTqSNuC8ZWO6eQIhALM3rJpdu0XVcvSW2985RjODh+9BBR5n8fB5lL7LOXnmAHYA\nyKPEf8ezrbk1awE/anoSbeM6TkOlxkb5l605dZkdz5oAAAGgWk2grQAABAMARzBF\nAiBwsQvwfVSuEcGqKp4lN/jWPUUuudUX+St4fImVDxCKmQIhANHJvWdzsXH/A9uC\nrSz1sQ4k3yowTYxtVtfTJc91oze2MCUGA1UdEQQeMByCCmdpdGh1Yi5jb22CDnd3\ndy5naXRodWIuY29tMAoGCCqGSM49BAMCA0cAMEQCIBdBV7Y/5t2o988vMBDGLJEl\nLWALzPJkt3dphmsZk9CEAiAJqxa/1c8JYYWHsGy1rQNUb3ffuCJU7pnjjqJfdiim\nhQ==\n-----END CERTIFICATE-----"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
