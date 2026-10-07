---
intent: LANGUAGE_TRANSLATION
slug: tr-apertium
status: approved
captured_at: 2026-10-05T09:34:13Z
request_url: https://apertium.org/apy/translate?q=Thank%20you%20very%20much&langpair=eng|spa
content_type: application/json
inputs: |
  {"q": "Thank you very much", "qe": "Thank%20you%20very%20much", "src": "en", "tgt": "es", "src3": "eng", "tgt3": "spa", "tgt_up": "ES"}
intent_description: |
  Translates multilingual text between source and target language pairs preserving semantic intent and idiom.
answer_requirement: |
  Must return the text translated into the target language, preserving meaning.
capture_note: |
  golden-test PASS: Apertium
reviewer_note: "auto_review: [1.00|heuristic+llm] The API response provides the translated text as requested."
reviewed_at: 2026-10-05T12:24:07Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "responseData": {
    "translatedText": "Muchas gracias"
  },
  "responseDetails": null,
  "responseStatus": 200
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The API response provides the translated text as requested._
