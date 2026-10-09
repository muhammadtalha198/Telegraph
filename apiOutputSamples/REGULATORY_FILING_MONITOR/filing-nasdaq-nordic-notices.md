---
intent: REGULATORY_FILING_MONITOR
slug: filing-nasdaq-nordic-notices
status: approved
captured_at: 2026-10-08T04:42:47Z
request_url: https://api.news.eu.nasdaq.com/news/query.action?globalGroup=exchangeNotice&displayLanguage=en&timeZone=CET&company=Nokia&start=0&limit=5&countResults=false&globalName=NordicAllMarkets&dir=DESC&callback=cb
content_type: application/javascript
inputs: |
  {"company": "Nokia"}
intent_description: |
  Parses statutory regulatory filings, 10-K/10-Q disclosures, and disclosure updates from financial oversight portals.
answer_requirement: |
  Must return the company's recent regulatory filings / disclosure notices (type/headline + date) for the pinned issuer.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the requested regulatory filings for the company Nokia."
reviewed_at: 2026-10-08T05:01:28Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```text
cb({
  "results" : {
    "item" : [ {
      "disclosureId" : 1462354,
      "categoryId" : 69,
      "headline" : "Changes in Nokia Corporation's own shares",
      "language" : "en",
      "languages" : [ "en", "fi" ],
      "cnsCategory" : "Changes in company's own shares",
      "messageUrl" : "https://view.news.eu.nasdaq.com/view?id=bcfc55230ca20d9c0d4d38eb1d2cd5b5e&lang=en&src=listed",
      "releaseTime" : "2026-09-08 16:00:00 +0200",
      "published" : "2026-09-08 16:00:00 +0200",
      "market" : "Main Market, Helsinki",
      "attachment" : [ ],
      "company" : "Nokia",
      "cnsTypeId" : "6"
    }, {
      "disclosureId" : 1460634,
      "categoryId" : 69,
      "headline" : "Changes in Nokia Corporation's own shares",
      "language" : "en",
      "languages" : [ "en", "fi" ],
      "cnsCategory" : "Changes in company's own shares",
      "messageUrl" : "https://view.news.eu.nasdaq.com/view?id=bdf6003c8b36ea202983a1fa3dd804ca9&lang=en&src=listed",
      "releaseTime" : "2026-08-27 18:00:00 +0200",
      "published" : "2026-08-27 18:00:00 +0200",
      "market" : "Main Market, Helsinki",
      "attachment" : [ ],
      "company" : "Nokia",
      "cnsTypeId" : "6"
    }, {
      "disclosureId" : 1458447,
      "categoryId" : 66,
      "headline" : "Nokia Corporation - Managers' transactions (Sahgal)",
      "language" : "en",
      "languages" : [ "en", "fi" ],
      "cnsCategory" : "Managers' Transactions",
      "messageUrl" : "https://view.news.eu.nasdaq.com/view?id=be2c6f35a28858e7a9efa8ea807d42ae5&lang=en&src=listed",
      "releaseTime" : "2026-08-14 14:30:00 +0200",
      "published" : "2026-08-14 14:30:00 +0200",
      "market" : "Main Market, Helsinki",
      "attachment" : [ ],
      "company" : "Nokia",
      "cnsTypeId" : "6"
    }, {
      "disclosureId" : 1458446,
      "categoryId" : 66,
      "headline" : "Nokia Corporation - Managers' transactions (Heard)",
      "language" : "en",
      "languages" : [ "fi", "en" ],
      "cnsCategory" : "Managers' Transactions",
      "messageUrl" : "https://view.news.eu.nasdaq.com/view?id=b7c179e48c5746e36f41ae9b578ae0cf4&lang=en&src=listed",
      "releaseTime" : "2026-08-14 14:30:00 +0200",
      "published" : "2026-08-14 14:30:00 +0200",
      "market" : "Main Market, Helsinki",
      "attachment" : [ ],
      "company" : "Nokia",
      "cnsTypeId" : "6"
    }, {
      "disclosureId" : 1458445,
      "categoryId" : 66,
      "headline" : "Nokia Corporation - Managers' transactions (Fisk)",
      "language" : "en",
      "languages" : [ "fi", "en" ],
      "cnsCategory" : "Managers' Transactions",
      "messageUrl" : "https://view.news.eu.nasdaq.com/view?id=b6017d8b298b9ecfd27b1f11ed1cea61c&lang=en&src=listed",
      "releaseTime" : "2026-08-14 14:30:00 +0200",
      "published" : "2026-08-14 14:30:00 +0200",
      "market" : "Main Market, Helsinki",
      "attachment" : [ ],
      "company" : "Nokia",
      "cnsTypeId" : "6"
    } ]
  }
} )
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the requested regulatory filings for the company Nokia._
