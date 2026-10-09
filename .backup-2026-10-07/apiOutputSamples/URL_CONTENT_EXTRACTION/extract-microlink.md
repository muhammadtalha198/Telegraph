---
intent: URL_CONTENT_EXTRACTION
slug: extract-microlink
status: pending_review
captured_at: 2026-10-05T09:34:50Z
request_url: https://api.microlink.io?url=https%3A%2F%2Fexample.com
content_type: application/json
inputs: |
  {"url": "https://example.com", "urle": "https%3A%2F%2Fexample.com"}
intent_description: |
  Scrapes target web pages, cleans boilerplate DOM nodes, and extracts clean markdown article content.
answer_requirement: |
  Must return the cleaned main content of the target web page.
capture_note: |
  golden-test PASS: Microlink
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "status": "success",
  "data": {
    "publisher": "example.com",
    "title": "Example Domain",
    "lang": "en",
    "url": "https://example.com/",
    "image": null,
    "date": null,
    "logo": null,
    "author": null,
    "description": "This domain is for use in documentation examples without needing permission. This is not a service; avoid relying on it for testing and monitoring purposes."
  },
  "statusCode": 200,
  "redirects": [],
  "headers": {
    "age": "1690",
    "allow": "GET, HEAD",
    "alt-svc": "h3=\":443\"; ma=86400",
    "cf-cache-status": "HIT",
    "cf-ray": "a4585f48dd1e27f6-EWR",
    "content-encoding": "br",
    "content-type": "text/html; charset=utf-8",
    "date": "Mon, 05 Oct 2026 00:39:57 GMT",
    "last-modified": "Sun, 04 Oct 2026 20:44:03 GMT",
    "server": "cloudflare"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
