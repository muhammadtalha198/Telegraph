---
intent: REGULATORY_FILING_MONITOR
slug: filing-esma-esef
status: pending_review
captured_at: 2026-10-05T09:41:41Z
request_url: https://filings.xbrl.org/api/filings?page[size]=1
content_type: application/json
inputs: |
  {"cik": "0000320193", "cik_int": "320193"}
intent_description: |
  Parses statutory regulatory filings, 10-K/10-Q disclosures, and disclosure updates from financial oversight portals.
answer_requirement: |
  Must return the company's regulatory filings (10-K/10-Q etc.) with dates/links.
capture_note: |
  golden-test PASS: filings.xbrl.org (ESEF)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "data": [
    {
      "type": "filing",
      "attributes": {
        "fxo_id": "EDRPOU-32033791-2020-12-31-UAIFRS-UA-0",
        "error_count": 0,
        "processed": "2023-11-14 15:49:47.074643",
        "viewer_url": "/EDRPOU-32033791/2020-12-31/UAIFRS/UA/0/ixbrlviewer.html",
        "sha256": "efd83933387621614d796dc9d7da2512a87ff6338c94c2105614f3cf1d9c1a9f",
        "json_url": "/EDRPOU-32033791/2020-12-31/UAIFRS/UA/0/32033791-2020-12-31.json",
        "date_added": "2023-11-09 18:26:01.957777",
        "country": "UA",
        "warning_count": 0,
        "inconsistency_count": 0,
        "period_end": "2020-12-31",
        "report_url": "/EDRPOU-32033791/2020-12-31/UAIFRS/UA/0/32033791-2020-12-31.html",
        "package_url": null
      },
      "relationships": {
        "entity": {
          "links": {
            "related": "/api/entities/32033791"
          }
        },
        "validation_messages": {
          "links": {
            "related": "/api/filings/9986/validation_messages"
          }
        }
      },
      "id": "9986",
      "links": {
        "self": "/api/filings/9986"
      }
    }
  ],
  "links": {
    "self": "https://filings.xbrl.org/api/filings?page%5Bsize%5D=1",
    "first": "https://filings.xbrl.org/api/filings?page%5Bsize%5D=1",
    "last": "https://filings.xbrl.org/api/filings?page%5Bsize%5D=1&page%5Bnumber%5D=25954",
    "next": "https://filings.xbrl.org/api/filings?page%5Bsize%5D=1&page%5Bnumber%5D=2"
  },
  "meta": {
    "count": 25954
  },
  "jsonapi": {
    "version": "1.0"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
