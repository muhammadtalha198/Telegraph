---
intent: WEB_SEARCH_QUERY
slug: search-wikipedia
status: pending_review
captured_at: 2026-10-05T09:34:54Z
request_url: https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=python%20programming%20language&format=json
content_type: application/json
inputs: |
  {"qe": "python%20programming%20language"}
intent_description: |
  Executes programmatic web search queries and returns top ranked organic URLs, snippets, and knowledge graphs.
answer_requirement: |
  Must return top-ranked results (URLs/snippets) for the query asked.
capture_note: |
  golden-test PASS: Wikipedia search
reviewer_note: ""
reviewed_at: ""
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
      "totalhits": 4500
    },
    "search": [
      {
        "ns": 0,
        "title": "Python (programming language)",
        "pageid": 23862,
        "size": 145099,
        "wordcount": 11680,
        "snippet": " and garbage collection. <span class=\"searchmatch\">Python</span> supports multiple <span class=\"searchmatch\">programming</span> paradigms but with an emphasis on object-oriented <span class=\"searchmatch\">programming</span> and dynamic typing. Guido",
        "timestamp": "2026-10-02T22:31:00Z"
      },
      {
        "ns": 0,
        "title": "Outline of the Python programming language",
        "pageid": 81118035,
        "size": 12149,
        "wordcount": 838,
        "snippet": "functional <span class=\"searchmatch\">programming</span>. ABC (<span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span>) – precursor to <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">Python</span> was started by Guido van Rossum in 1989 and first released in 1991. <span class=\"searchmatch\">Python</span> 2 —",
        "timestamp": "2026-08-24T15:15:14Z"
      },
      {
        "ns": 0,
        "title": "Mojo (programming language)",
        "pageid": 73729965,
        "size": 21581,
        "wordcount": 1690,
        "snippet": "Mojo is a <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span> for Linux and macOS. It is a system <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span> with semantics inspired by Rust such as static typing and a borrow",
        "timestamp": "2026-10-01T06:55:07Z"
      },
      {
        "ns": 0,
        "title": "History of Python",
        "pageid": 21356332,
        "size": 59915,
        "wordcount": 4349,
        "snippet": "The <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span> <span class=\"searchmatch\">Python</span> was conceived in the late 1980s, and its implementation was started in December 1989 by Guido van Rossum at CWI in the",
        "timestamp": "2026-10-02T21:57:22Z"
      },
      {
        "ns": 0,
        "title": "Python syntax and semantics",
        "pageid": 5250192,
        "size": 69693,
        "wordcount": 7920,
        "snippet": "The syntax of the <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span> is the set of rules that defines how a <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">program</span> will be written and interpreted (by both the runtime",
        "timestamp": "2026-09-25T19:53:01Z"
      },
      {
        "ns": 0,
        "title": "Core Python Programming",
        "pageid": 25061839,
        "size": 3874,
        "wordcount": 316,
        "snippet": "Core <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">Programming</span> is a textbook on the <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span>, written by Wesley J. Chun. The first edition of the book was released on December",
        "timestamp": "2026-04-10T11:05:03Z"
      },
      {
        "ns": 0,
        "title": "Guido van Rossum",
        "pageid": 226402,
        "size": 24441,
        "wordcount": 1977,
        "snippet": "January 1956) is a Dutch programmer. He is the creator of the <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span>, for which he was the &quot;benevolent dictator for life&quot; (BDFL) until",
        "timestamp": "2026-10-05T03:04:00Z"
      },
      {
        "ns": 0,
        "title": "List of Python software",
        "pageid": 3673376,
        "size": 38301,
        "wordcount": 3721,
        "snippet": "The <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span> is actively used by many people, both in industry and academia, for a wide variety of purposes. Atom — an open-source",
        "timestamp": "2026-10-01T00:32:08Z"
      },
      {
        "ns": 0,
        "title": "Zen of Python",
        "pageid": 46448252,
        "size": 11211,
        "wordcount": 1130,
        "snippet": "<span class=\"searchmatch\">Python</span> is a collection of 19 &quot;guiding principles&quot; for writing computer <span class=\"searchmatch\">programs</span> that influence the design of the <span class=\"searchmatch\">Python</span> <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span>. <span class=\"searchmatch\">Python</span> code",
        "timestamp": "2026-03-11T00:04:23Z"
      },
      {
        "ns": 0,
        "title": "General-purpose programming language",
        "pageid": 891926,
        "size": 14675,
        "wordcount": 1502,
        "snippet": "domains. Conversely, a domain-specific <span class=\"searchmatch\">programming</span> <span class=\"searchmatch\">language</span> (DSL) is used within a specific area. For example, <span class=\"searchmatch\">Python</span> is a GPL, while SQL is a DSL for querying",
        "timestamp": "2026-08-15T07:45:18Z"
      }
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
