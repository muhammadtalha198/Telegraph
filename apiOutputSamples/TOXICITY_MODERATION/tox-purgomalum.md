---
intent: TOXICITY_MODERATION
slug: tox-purgomalum
status: pending_review
captured_at: 2026-10-08T04:43:51Z
request_url: https://www.purgomalum.com/service/containsprofanity?text=Thank%20you%20so%20much%20for%20your%20help%2C%20have%20a%20wonderful%20day%21
content_type: text/plain
inputs: |
  {"text": "Thank you so much for your help, have a wonderful day!", "qe": "Thank%20you%20so%20much%20for%20your%20help%2C%20have%20a%20wonderful%20day%21"}
intent_description: |
  Evaluates user submitted text for hate speech, harassment, sexual content, self-harm incitement, and toxicity.
answer_requirement: |
  Must flag the pinned threatening/harassing text (threat) as unsafe/toxic and must NOT flag the benign thank-you text.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
false
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
