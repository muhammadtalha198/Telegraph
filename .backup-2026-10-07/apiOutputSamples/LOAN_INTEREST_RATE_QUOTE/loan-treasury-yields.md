---
intent: LOAN_INTEREST_RATE_QUOTE
slug: loan-treasury-yields
status: pending_review
captured_at: 2026-10-05T09:41:30Z
request_url: https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates?sort=-record_date&page[size]=1
content_type: application/json
inputs: |
  {}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a current lending/mortgage/benchmark interest rate.
capture_note: |
  golden-test PASS: US Treasury
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "data": [
    {
      "record_date": "2026-08-31",
      "security_type_desc": "Marketable",
      "security_desc": "Treasury Bills",
      "avg_interest_rate_amt": "3.788",
      "src_line_nbr": "1",
      "record_fiscal_year": "2026",
      "record_fiscal_quarter": "4",
      "record_calendar_year": "2026",
      "record_calendar_quarter": "3",
      "record_calendar_month": "08",
      "record_calendar_day": "31"
    }
  ],
  "meta": {
    "count": 1,
    "labels": {
      "record_date": "Record Date",
      "security_type_desc": "Security Type Description",
      "security_desc": "Security Description",
      "avg_interest_rate_amt": "Average Interest Rate Amount",
      "src_line_nbr": "Source Line Number",
      "record_fiscal_year": "Fiscal Year",
      "record_fiscal_quarter": "Fiscal Quarter Number",
      "record_calendar_year": "Calendar Year",
      "record_calendar_quarter": "Calendar Quarter Number",
      "record_calendar_month": "Calendar Month Number",
      "record_calendar_day": "Calendar Day Number"
    },
    "dataTypes": {
      "record_date": "DATE",
      "security_type_desc": "STRING",
      "security_desc": "STRING",
      "avg_interest_rate_amt": "PERCENTAGE",
      "src_line_nbr": "INTEGER",
      "record_fiscal_year": "YEAR",
      "record_fiscal_quarter": "QUARTER",
      "record_calendar_year": "YEAR",
      "record_calendar_quarter": "QUARTER",
      "record_calendar_month": "MONTH",
      "record_calendar_day": "DAY"
    },
    "dataFormats": {
      "record_date": "YYYY-MM-DD",
      "security_type_desc": "String",
      "security_desc": "String",
      "avg_interest_rate_amt": "10.2%",
      "src_line_nbr": "10",
      "record_fiscal_year": "YYYY",
      "record_fiscal_quarter": "Q",
      "record_calendar_year": "YYYY",
      "record_calendar_quarter": "Q",
      "record_calendar_month": "MM",
      "record_calendar_day": "DD"
    },
    "total-count": 5009,
    "total-pages": 5009
  },
  "links": {
    "self": "&page%5Bnumber%5D=1&page%5Bsize%5D=1",
    "first": "&page%5Bnumber%5D=1&page%5Bsize%5D=1",
    "prev": null,
    "next": "&page%5Bnumber%5D=2&page%5Bsize%5D=1",
    "last": "&page%5Bnumber%5D=5009&page%5Bsize%5D=1"
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
