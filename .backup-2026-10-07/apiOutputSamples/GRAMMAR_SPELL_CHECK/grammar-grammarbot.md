---
intent: GRAMMAR_SPELL_CHECK
slug: grammar-grammarbot
status: pending_review
captured_at: 2026-10-05T09:34:58Z
request_url: https://api.grammarbot.io/v2/check?api_key=guest&language=en-US&text=I%20has%20a%20apple%20and%20teh%20dog%20runned
content_type: application/json
inputs: |
  {"text": "I has a apple and teh dog runned", "qe": "I%20has%20a%20apple%20and%20teh%20dog%20runned"}
intent_description: |
  Detects typographical, orthographic, punctuation, and grammatical syntax errors with correction offsets.
answer_requirement: |
  Must return the detected spelling/grammar errors with corrections/offsets for the text.
capture_note: |
  golden-test PASS: GrammarBot
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "software": {
    "name": "GrammarBot",
    "version": "4.3.1",
    "status": "invalid key"
  },
  "warnings": {
    "incompleteResults": true
  },
  "matches": []
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
