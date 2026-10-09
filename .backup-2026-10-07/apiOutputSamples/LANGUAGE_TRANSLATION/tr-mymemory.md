---
intent: LANGUAGE_TRANSLATION
slug: tr-mymemory
status: pending_review
captured_at: 2026-10-05T09:34:13Z
request_url: https://api.mymemory.translated.net/get?q=Hello%2C%20how%20are%20you%3F&langpair=en|fr
content_type: application/json
inputs: |
  {"q": "Hello, how are you?", "qe": "Hello%2C%20how%20are%20you%3F", "src": "en", "tgt": "fr", "src3": "eng", "tgt3": "fra", "tgt_up": "FR"}
intent_description: |
  Translates multilingual text between source and target language pairs preserving semantic intent and idiom.
answer_requirement: |
  Must return the text translated into the target language, preserving meaning.
capture_note: |
  golden-test PASS: MyMemory
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "responseData": {
    "translatedText": "Bonjour, comment vas-tu?",
    "match": 1
  },
  "quotaFinished": false,
  "mtLangSupported": null,
  "responseDetails": "",
  "responseStatus": 200,
  "responderId": null,
  "exception_code": null,
  "matches": [
    {
      "id": "803894684855682920",
      "segment": "Hello, how are you?",
      "translation": "Bonjour, comment vas-tu?",
      "source": "en-GB",
      "target": "fr-FR",
      "quality": "74",
      "reference": null,
      "usage-count": 2,
      "subject": "All",
      "created-by": "MateCat",
      "last-updated-by": "MateCat",
      "create-date": "2024-03-04 11:58:17",
      "last-update-date": "2024-03-04 11:58:17",
      "match": 1,
      "penalty": 0
    },
    {
      "id": "817378300",
      "segment": "Hello, how are you? ",
      "translation": "Bonjour, comment allez-vous ? ",
      "source": "en-GB",
      "target": "fr-FR",
      "quality": "74",
      "reference": null,
      "usage-count": 2,
      "subject": "All",
      "created-by": "MateCat",
      "last-updated-by": "MateCat",
      "create-date": "2022-01-28 12:53:42",
      "last-update-date": "2022-01-28 12:53:42",
      "match": 1,
      "penalty": 0
    },
    {
      "id": "817357094",
      "segment": "Hello, how are you?",
      "translation": "Bonjour, comment allez-vous ?",
      "source": "en-GB",
      "target": "fr-FR",
      "quality": "74",
      "reference": null,
      "usage-count": 3,
      "subject": "All",
      "created-by": "MateCat",
      "last-updated-by": "MateCat",
      "create-date": "2022-01-28 11:55:16",
      "last-update-date": "2022-01-28 11:55:16",
      "match": 1,
      "penalty": 0
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
