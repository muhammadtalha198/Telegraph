---
intent: LANGUAGE_TRANSLATION
slug: tr-popcat
status: pending_review
captured_at: 2026-10-05T09:34:13Z
request_url: https://api.popcat.xyz/translate?to=fr&text=Hello%2C%20how%20are%20you%3F
content_type: application/json
inputs: |
  {"q": "Hello, how are you?", "qe": "Hello%2C%20how%20are%20you%3F", "src": "en", "tgt": "fr", "src3": "eng", "tgt3": "fra", "tgt_up": "FR"}
intent_description: |
  Translates multilingual text between source and target language pairs preserving semantic intent and idiom.
answer_requirement: |
  Must return the text translated into the target language, preserving meaning.
capture_note: |
  golden-test PASS: Popcat API
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "translated": "Bonjour comment allez-vous?"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
