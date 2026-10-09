---
intent: REGULATORY_FILING_MONITOR
slug: filing-asx-announcements
status: approved
captured_at: 2026-10-08T04:42:46Z
request_url: https://asx.api.markitdigital.com/asx-research/1.0/companies/BHP/announcements
content_type: application/json
inputs: |
  {"asx_code": "BHP"}
intent_description: |
  Parses statutory regulatory filings, 10-K/10-Q disclosures, and disclosure updates from financial oversight portals.
answer_requirement: |
  Must return the company's recent regulatory filings / disclosure notices (type/headline + date) for the pinned issuer.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains multiple recent regulatory filings and disclosure notices for the specified ASX code 'BHP'."
reviewed_at: 2026-10-08T05:01:24Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "data": {
    "displayName": "BHP GROUP LIMITED",
    "issueType": "CS",
    "items": [
      {
        "announcementType": "DISTRIBUTION ANNOUNCEMENT",
        "date": "2026-10-07T22:23:09.000Z",
        "documentKey": "2924-03145894-3A703622",
        "fileSize": "16KB",
        "headline": "Update - Dividend/Distribution - BHP",
        "isPriceSensitive": false,
        "url": ""
      },
      {
        "announcementType": "SECURITY HOLDER DETAILS",
        "date": "2026-10-07T07:28:56.000Z",
        "documentKey": "2924-03145697-3A703571",
        "fileSize": "293KB",
        "headline": "Change in substantial holding",
        "isPriceSensitive": false,
        "url": ""
      },
      {
        "announcementType": "PERIODIC REPORTS",
        "date": "2026-09-15T22:55:24.000Z",
        "documentKey": "2924-03135917-3A701845",
        "fileSize": "3071KB",
        "headline": "BHP 2026 ESG Roundtable",
        "isPriceSensitive": false,
        "url": ""
      },
      {
        "announcementType": "NOTICE OF MEETING",
        "date": "2026-09-14T22:14:39.000Z",
        "documentKey": "2924-03135386-3A701734",
        "fileSize": "705KB",
        "headline": "BHP 2026 Proxy Form",
        "isPriceSensitive": false,
        "url": ""
      },
      {
        "announcementType": "OTHER",
        "date": "2026-09-14T22:14:04.000Z",
        "documentKey": "2924-03135379-3A701731",
        "fileSize": "5489KB",
        "headline": "BHP 2026 Notice of Annual General Meeting",
        "isPriceSensitive": false,
        "url": ""
      }
    ],
    "symbol": "BHP",
    "xid": "60947"
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains multiple recent regulatory filings and disclosure notices for the specified ASX code 'BHP'._
