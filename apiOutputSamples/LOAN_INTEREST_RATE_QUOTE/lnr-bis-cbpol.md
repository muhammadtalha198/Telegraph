---
intent: LOAN_INTEREST_RATE_QUOTE
slug: lnr-bis-cbpol
status: rejected
captured_at: 2026-10-08T04:42:06Z
request_url: https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CBPOL/1.0/D.CH?startPeriod=2025-06-18&endPeriod=2025-06-18&format=csv
content_type: text/csv
inputs: |
  {"bis_area": "CH", "d": "2025-06-18", "snb_date": "2025-06-18"}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a published lending / policy / benchmark interest rate (percent) for the pinned country and date or period.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response is about the SNB policy rate, not a residential mortgage interest rate."
reviewed_at: 2026-10-08T04:56:40Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```text
FREQ,REF_AREA,UNIT_MEASURE,UNIT_MULT,TIME_FORMAT,COMPILATION,DECIMALS,SOURCE_REF,SUPP_INFO_BREAKS,TITLE,TIME_PERIOD,OBS_VALUE,OBS_STATUS,OBS_CONF,OBS_PRE_BREAK
D,CH,368,0,,From 13 June 2019 onwards SNB Policy rate; From 1 Jan 2000 to 12 June 2019 mid-point of the SNB target range; from 1 Jan 1946 to 31 Dec 1999: discount rate.,4,Swiss National Bank,, Central bank policy rates - Switzerland - Daily - End of period,2025-06-18,0.25,A,F,
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response is about the SNB policy rate, not a residential mortgage interest rate._
