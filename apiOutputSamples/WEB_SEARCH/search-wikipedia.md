---
intent: WEB_SEARCH
slug: search-wikipedia
status: approved
captured_at: 2026-10-05T05:45:01Z
request_url: https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=EUR&format=json
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - only 9 candidates; 4 keyless. Keyless web-search is scarce; Brave/Google/Mojeek/Tavily/Jina need free keys (you already have JINA_API_KEY). Distinct publishers: 9.
answer_requirement: |
  Must satisfy catalog intent WEB_SEARCH via upstream Wikipedia search
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:34Z
---

## Raw API output

```json
{
  "batchcomplete": "",
  "continue": {
    "sroffset": 10,
    "continue": "-||"
  },
  "query": {
    "searchinfo": {
      "totalhits": 14745
    },
    "search": [
      {
        "ns": 0,
        "title": "Euro",
        "pageid": 9472,
        "size": 111526,
        "wordcount": 10626,
        "snippet": "The euro (symbol: €; currency code: <span class=\"searchmatch\">EUR</span>) is the official currency of 21 of the 27 member states of the European Union. This group of states is officially",
        "timestamp": "2026-10-05T01:14:02Z"
      },
      {
        "ns": 0,
        "title": "EUR-pallet",
        "pageid": 31777521,
        "size": 13190,
        "wordcount": 1544,
        "snippet": "The <span class=\"searchmatch\">EUR</span>-pallet, also known as Euro-pallet or EPAL-pallet, is the standard European pallet as specified by the UIC pallet working group and the UIC 435-2",
        "timestamp": "2026-09-28T18:26:23Z"
      },
      {
        "ns": 0,
        "title": "EUR, Rome",
        "pageid": 220724,
        "size": 17684,
        "wordcount": 1609,
        "snippet": "<span class=\"searchmatch\">EUR</span> is a residential area and the major business district in Rome, Italy, part of Municipio IX. It is considered Rome’s business district. The area was",
        "timestamp": "2026-09-20T04:52:17Z"
      },
      {
        "ns": 0,
        "title": "EUR (disambiguation)",
        "pageid": 2330960,
        "size": 703,
        "wordcount": 136,
        "snippet": "<span class=\"searchmatch\">EUR</span> is the ISO 4217 currency code for the Euro, the European Union currency. <span class=\"searchmatch\">EUR</span> may also refer to: Look up <span class=\"searchmatch\">EUR</span> or <span class=\"searchmatch\">eur</span> in Wiktionary, the free dictionary",
        "timestamp": "2022-03-10T10:32:19Z"
      },
      {
        "ns": 0,
        "title": "EUR-Lex",
        "pageid": 414745,
        "size": 17766,
        "wordcount": 1794,
        "snippet": "<span class=\"searchmatch\">EUR</span>-Lex is the official online database of European Union law and other public documents of the European Union (EU), published in 24 official languages",
        "timestamp": "2026-09-22T05:40:51Z"
      },
      {
        "ns": 0,
        "title": "ISO 4217",
        "pageid": 15403,
        "size": 73689,
        "wordcount": 3942,
        "snippet": "be highly mnemonic if possible. An example is the assignment of the code <span class=\"searchmatch\">EUR</span> to the euro. ISO 4217 amendment 94, which created this code, states &quot;The",
        "timestamp": "2026-09-28T23:01:26Z"
      },
      {
        "ns": 0,
        "title": "European Engineer",
        "pageid": 958534,
        "size": 17794,
        "wordcount": 1968,
        "snippet": "(<span class=\"searchmatch\">EUR</span> ING) is an international professional qualification and title for highly qualified engineers used in over 32 European countries. Contemporary <span class=\"searchmatch\">EUR</span>",
        "timestamp": "2026-10-01T22:01:13Z"
      },
      {
        "ns": 0,
        "title": "List of European countries by minimum wage",
        "pageid": 22219814,
        "size": 142904,
        "wordcount": 9568,
        "snippet": "1st level - 816 <span class=\"searchmatch\">eur</span> • 2nd level - 932 <span class=\"searchmatch\">eur</span> • 3rd level - 1,048 <span class=\"searchmatch\">eur</span> • 4th level - 1,164 <span class=\"searchmatch\">eur</span> • 5th level - 1,280 <span class=\"searchmatch\">eur</span> • 6th level - 1,396 <span class=\"searchmatch\">eur</span> For an employee",
        "timestamp": "2026-10-04T05:15:18Z"
      },
      {
        "ns": 0,
        "title": "LunEur",
        "pageid": 21650515,
        "size": 8540,
        "wordcount": 466,
        "snippet": "Lun<span class=\"searchmatch\">Eur</span> (complete name Luna Park Permanente di Roma) is an amusement park in Rome and the oldest (still operating) in Italy, dating back to 1953. It took",
        "timestamp": "2026-07-25T13:41:51Z"
      },
      {
        "ns": 0,
        "title": "Master of European Law",
        "pageid": 18317568,
        "size": 2895,
        "wordcount": 318,
        "snippet": "Master of European Law (LL.M. <span class=\"searchmatch\">Eur</span>) is a specialized Master of Laws (LL.M.) degree, awarded after successful completion of a course of study in the law",
        "timestamp": "2025-11-12T18:29:54Z"
      }
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
