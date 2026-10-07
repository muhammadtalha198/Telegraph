---
intent: GRAMMAR_SPELL_CHECK
slug: grammar-datamuse
status: approved
captured_at: 2026-10-05T05:45:01Z
request_url: https://api.datamuse.com/sug?s=teh
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - only 5 candidates; 3 keyless. Keyless ceiling is ~2; the rest are free-key. Distinct publishers: 5.
answer_requirement: |
  Must satisfy catalog intent GRAMMAR_SPELL_CHECK via upstream Datamuse
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:32Z
---

## Raw API output

```json
[
  {
    "word": "teh",
    "score": 2010
  },
  {
    "word": "teheran",
    "score": 1017
  },
  {
    "word": "tehuelche",
    "score": 1009
  },
  {
    "word": "tehsil",
    "score": 1005
  },
  {
    "word": "tehan",
    "score": 1004
  },
  {
    "word": "tehani",
    "score": 1003
  },
  {
    "word": "tehara",
    "score": 1001
  },
  {
    "word": "tehran",
    "score": 17
  },
  {
    "word": "tehuantepec",
    "score": 9
  },
  {
    "word": "tehachapi mountains",
    "score": 7
  }
]
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
