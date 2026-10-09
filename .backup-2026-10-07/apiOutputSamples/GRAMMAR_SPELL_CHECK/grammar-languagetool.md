---
intent: GRAMMAR_SPELL_CHECK
slug: grammar-languagetool
status: approved
captured_at: 2026-10-05T09:34:58Z
request_url: https://api.languagetool.org/v2/check?language=en-US&text=I%20has%20a%20apple%20and%20teh%20dog%20runned
content_type: application/json
inputs: |
  {"text": "I has a apple and teh dog runned", "qe": "I%20has%20a%20apple%20and%20teh%20dog%20runned"}
intent_description: |
  Detects typographical, orthographic, punctuation, and grammatical syntax errors with correction offsets.
answer_requirement: |
  Must return the detected spelling/grammar errors with corrections/offsets for the text.
capture_note: |
  golden-test PASS: LanguageTool
reviewer_note: "auto_review: [1.00|heuristic+llm] Corrected errors are provided but the full corrected text is not included in the response."
reviewed_at: 2026-10-05T11:31:57Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "software": {
    "name": "LanguageTool",
    "version": "6.9-SNAPSHOT",
    "buildDate": "2026-09-01 15:16:00 +0000",
    "apiVersion": 1,
    "premium": true,
    "premiumHint": "You might be missing errors only the Premium version can find. Contact us at support<at>languagetoolplus.com.",
    "status": ""
  },
  "warnings": {
    "incompleteResults": false
  },
  "language": {
    "name": "English (US)",
    "code": "en-US",
    "detectedLanguage": {
      "name": "English (US)",
      "code": "en-US",
      "confidence": 0.9999998,
      "source": "ngram"
    }
  },
  "matches": [
    {
      "message": "Possible agreement error — use the base form here.",
      "shortMessage": "",
      "replacements": [
        {
          "value": "have"
        }
      ],
      "offset": 2,
      "length": 3,
      "context": {
        "text": "I has a apple and teh dog runned",
        "offset": 2,
        "length": 3
      },
      "sentence": "I has a apple and teh dog runned",
      "type": {
        "typeName": "Other"
      },
      "rule": {
        "id": "BASE_FORM",
        "subId": "2",
        "sourceFile": "grammar.xml",
        "description": "base form after I/you/we/they",
        "issueType": "grammar",
        "urls": [
          {
            "value": "https://languagetool.org/insights/post/grammar-subject-verb-agreement/#1-singular-subjects-must-go-with-singular-verbs-and-plural-subjects-with-plural-verbs"
          }
        ],
        "category": {
          "id": "GRAMMAR",
          "name": "Grammar"
        },
        "isPremium": false,
        "confidence": 0.57
      },
      "ignoreForIncompleteSentence": true,
      "contextForSureMatch": 4
    },
    {
      "message": "Use “an” instead of ‘a’ if the following word starts with a vowel sound, e.g. ‘an article’, ‘an hour’.",
      "shortMessage": "Wrong article",
      "replacements": [
        {
          "value": "an"
        }
      ],
      "offset": 6,
      "length": 1,
      "context": {
        "text": "I has a apple and teh dog runned",
        "offset": 6,
        "length": 1
      },
      "sentence": "I has a apple and teh dog runned",
      "type": {
        "typeName": "Other"
      },
      "rule": {
        "id": "EN_A_VS_AN",
        "description": "Use of 'a' vs. 'an'",
        "issueType": "misspelling",
        "urls": [
          {
            "value": "https://languagetool.org/insights/post/indefinite-articles/"
          }
        ],
        "category": {
          "id": "MISC",
          "name": "Miscellaneous"
        },
        "isPremium": false,
        "confidence": 0.58
      },
      "ignoreForIncompleteSentence": false,
      "contextForSureMatch": 1
    },
    {
      "message": "Possible spelling mistake found.",
      "shortMessage": "Spelling mistake",
      "replacements": [
        {
          "value": "the"
        },
        {
          "value": "ten"
        },
        {
          "value": "tea"
        },
        {
          "value": "tech"
        },
        {
          "value": "Ted"
        },
        {
          "value": "TeX"
        },
        {
          "value": "tee"
        },
        {
          "value": "eh"
        },
        {
          "value": "tel"
        },
        {
          "value": "TEF"
        },
        {
          "value": "BEH"
        },
        {
          "value": "GEH"
        },
        {
          "value": "NEH"
        },
        {
          "value": "Neh"
        },
        {
          "value": "TAH"
        },
        {
          "value": "TBH"
        },
        {
          "value": "TCH"
        },
        {
          "value": "TEB"
        },
        {
          "value": "TEC"
        },
        {
          "value": "TED"
        },
        {
          "value": "TEE"
        },
        {
          "value": "TEI"
        },
        {
          "value": "TEL"
        },
        {
          "value": "TEM"
        },
        {
          "value": "TEP"
        },
        {
          "value": "TEQ"
        },
        {
          "value": "TER"
        },
        {
          "value": "TES"
        },
        {
          "value": "TEU"
        },
        {
          "value": "TEV"
        },
        {
          "value": "TH"
        },
        {
          "value": "TLH"
        },
        {
          "value": "TSH"
        },
        {
          "value": "TVH"
        },
        {
          "value": "Te"
        },
        {
          "value": "Tet"
        },
        {
          "value": "Tex"
        },
        {
          "value": "Th"
        },
        {
          "value": "heh"
        },
        {
          "value": "meh"
        }
      ],
      "offset": 18,
      "length": 3,
      "context": {
        "text": "I has a apple and teh dog runned",
        "offset": 18,
        "length": 3
      },
      "sentence": "I has a apple and teh dog runned",
      "type": {
        "typeName": "UnknownWord"
      },
      "rule": {
        "id": "MORFOLOGIK_RULE_EN_US",
        "description": "Possible spelling mistake",
        "issueType": "misspelling",
        "category": {
          "id": "TYPOS",
          "name": "Possible Typo"
        },
        "isPremium": false,
        "confidence": 0.68
      },
      "ignoreForIncompleteSentence": false,
      "contextForSureMatch": 0
    },
    {
      "message": "Possible spelling mistake found.",
      "shortMessage": "Spelling mistake",
      "replacements": [
        {
          "value": "runner"
        },
        {
          "value": "ruined"
        },
        {
          "value": "gunned"
        },
        {
          "value": "punned"
        },
        {
          "value": "runnel"
        },
        {
          "value": "sunned"
        },
        {
          "value": "dunned"
        },
        {
          "value": "funned"
        }
      ],
      "offset": 26,
      "length": 6,
      "context": {
        "text": "I has a apple and teh dog runned",
        "offset": 26,
        "length": 6
      },
      "sentence": "I has a apple and teh dog runned",
      "type": {
        "typeName": "UnknownWord"
      },
      "rule": {
        "id": "MORFOLOGIK_RULE_EN_US",
        "description": "Possible spelling mistake",
        "issueType": "misspelling",
        "category": {
          "id": "TYPOS",
          "name": "Possible Typo"
        },
        "isPremium": false,
        "confidence": 0.68
      },
      "ignoreForIncompleteSentence": false,
      "contextForSureMatch": 0
    }
  ],
  "sentenceRanges": [
    [
      0,
      32
    ]
  ],
  "extendedSentenceRanges": [
    {
      "from": 0,
      "to": 32,
      "detectedLanguages": [
        {
          "language": "en",
          "rate": 1.0
        }
      ]
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] Corrected errors are provided but the full corrected text is not included in the response._
