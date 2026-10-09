---
intent: WEB_SEARCH
slug: search-duckduckgo-ia
status: approved
captured_at: 2026-10-05T05:45:00Z
request_url: https://api.duckduckgo.com/?q=EUR&format=json&no_html=1
content_type: application/x-javascript
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - only 9 candidates; 4 keyless. Keyless web-search is scarce; Brave/Google/Mojeek/Tavily/Jina need free keys (you already have JINA_API_KEY). Distinct publishers: 9.
answer_requirement: |
  Must satisfy catalog intent WEB_SEARCH via upstream DuckDuckGo Instant Answer
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:34Z
---

## Raw API output

```json
{
  "Abstract": "",
  "AbstractSource": "Wikipedia",
  "AbstractText": "",
  "AbstractURL": "https://en.wikipedia.org/wiki/EUR_(disambiguation)",
  "Answer": "",
  "AnswerType": "",
  "Definition": "",
  "DefinitionSource": "",
  "DefinitionURL": "",
  "Entity": "",
  "Heading": "EUR",
  "Image": "",
  "ImageHeight": 0,
  "ImageIsLogo": 0,
  "ImageWidth": 0,
  "Infobox": "",
  "Redirect": "",
  "RelatedTopics": [
    {
      "FirstURL": "https://duckduckgo.com/Euro",
      "Icon": {
        "Height": "",
        "URL": "",
        "Width": ""
      },
      "Result": "<a href=\"https://duckduckgo.com/Euro\">EUR</a> The official currency of 19 of the 27 member states of the European Union.",
      "Text": "EUR The official currency of 19 of the 27 member states of the European Union."
    },
    {
      "FirstURL": "https://duckduckgo.com/EUR.1_movement_certificate",
      "Icon": {
        "Height": "",
        "URL": "",
        "Width": ""
      },
      "Result": "<a href=\"https://duckduckgo.com/EUR.1_movement_certificate\">EUR.1 movement certificate</a> The EUR.1 movement certificate is a form used in international commodity traffic.",
      "Text": "EUR.1 movement certificate The EUR.1 movement certificate is a form used in international commodity traffic."
    },
    {
      "FirstURL": "https://duckduckgo.com/Erasmus_University_Rotterdam",
      "Icon": {
        "Height": "",
        "URL": "/i/a726b664.jpg",
        "Width": ""
      },
      "Result": "<a href=\"https://duckduckgo.com/Erasmus_University_Rotterdam\">Erasmus University Rotterdam</a>A public research university located in Rotterdam, Netherlands.",
      "Text": "Erasmus University Rotterdam A public research university located in Rotterdam, Netherlands."
    },
    {
      "FirstURL": "https://duckduckgo.com/EUR%2C_Rome",
      "Icon": {
        "Height": "",
        "URL": "/i/e2dd563b.jpg",
        "Width": ""
      },
      "Result": "<a href=\"https://duckduckgo.com/EUR%2C_Rome\">EUR, Rome</a>A residential and business district in Rome, Italy, part of the Municipio IX. The area was...",
      "Text": "EUR, Rome A residential and business district in Rome, Italy, part of the Municipio IX. The area was..."
    },
    {
      "FirstURL": "https://duckduckgo.com/Eastern_Union_Railway",
      "Icon": {
        "Height": "",
        "URL": "",
        "Width": ""
      },
      "Result": "<a href=\"https://duckduckgo.com/Eastern_Union_Railway\">Eastern Union Railway</a>An English railway company, at first built from Colchester to Ipswich; it opened in 1846.",
      "Text": "Eastern Union Railway An English railway company, at first built from Colchester to Ipswich; it opened in 1846."
    },
    {
      "FirstURL": "https://duckduckgo.com/Bureau_of_European_and_Eurasian_Affairs",
      "Icon": {
        "Height": "",
        "URL": "",
        "Width": ""
      },
      "Result": "<a href=\"https://duckduckgo.com/Bureau_of_European_and_Eurasian_Affairs\">Bureau of European and Eurasian Affairs</a>In the United States Government, the Bureau of European and Eurasian Affairs is part of the...",
      "Text": "Bureau of European and Eurasian Affairs In the United States Government, the Bureau of European and Eurasian Affairs is part of the..."
    },
    {
      "FirstURL": "https://duckduckgo.com/Estimated_ultimate_recovery",
      "Icon": {
        "Height": "",
        "URL": "",
        "Width": ""
      },
      "Result": "<a href=\"https://duckduckgo.com/Estimated_ultimate_recovery\">Estimated ultimate recovery</a> The sum of the proven reserves at a specific time and the cumulative production up to that point.",
      "Text": "Estimated ultimate recovery The sum of the proven reserves at a specific time and the cumulative production up to that point."
    },
    {
      "FirstURL": "https://duckduckgo.com/EUR-Lex",
      "Icon": {
        "Height": 16,
        "URL": "/i/eur-lex.europa.eu.ico",
        "Width": 16
      },
      "Result": "<a href=\"https://duckduckgo.com/EUR-Lex\">EUR-Lex</a>An official website of European Union law and other public documents of the European Union...",
      "Text": "EUR-Lex An official website of European Union law and other public documents of the European Union..."
    }
  ],
  "Results": [],
  "Type": "D",
  "meta": {
    "attribution": null,
    "blockgroup": null,
    "created_date": null,
    "description": "Wikipedia",
    "designer": null,
    "dev_date": null,
    "dev_milestone": "live",
    "developer": [
      {
        "name": "DDG Team",
        "type": "ddg",
        "url": "http://www.duckduckhack.com"
      }
    ],
    "example_query": "nikola tesla",
    "id": "wikipedia_fathead",
    "is_stackexchange": null,
    "js_callback_name": "wikipedia",
    "live_date": null,
    "maintainer": {
      "github": "duckduckgo"
    },
    "name": "Wikipedia",
    "perl_module": "DDG::Fathead::Wikipedia",
    "producer": null,
    "production_state": "online",
    "repo": "fathead",
    "signal_from": "wikipedia_fathead",
    "src_domain": "en.wikipedia.org",
    "src_id": 1,
    "src_name": "Wikipedia",
    "src_options": {
      "directory": "",
      "is_fanon": 0,
      "is_mediawiki": 1,
      "is_wikipedia": 1,
      "language": "en",
      "min_abstract_length": "20",
      "skip_abstract": 0,
      "skip_abstract_paren": 0,
      "skip_end": "0",
      "skip_icon": 0,
      "skip_image_name": 0,
      "skip_qr": "",
      "source_skip": "",
      "src_info": ""
    },
    "src_url": null,
    "status": "live",
    "tab": "About",
    "topic": [
      "productivity"
    ],
    "unsafe": 0
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
