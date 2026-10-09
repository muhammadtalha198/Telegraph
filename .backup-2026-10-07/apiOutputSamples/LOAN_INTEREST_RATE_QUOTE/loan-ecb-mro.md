---
intent: LOAN_INTEREST_RATE_QUOTE
slug: loan-ecb-mro
status: pending_review
captured_at: 2026-10-05T09:41:30Z
request_url: https://data-api.ecb.europa.eu/service/data/FM/B.U2.EUR.4F.KR.MRR_FR.LEV?lastNObservations=1&format=jsondata
content_type: application/json
inputs: |
  {}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a current lending/mortgage/benchmark interest rate.
capture_note: |
  golden-test PASS: ECB main refinancing rate
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "header": {
    "id": "8e21e3ae-5e1e-4c92-bc31-974872ca4962",
    "test": false,
    "prepared": "2026-09-28T17:48:53.843+02:00",
    "sender": {
      "id": "ECB"
    }
  },
  "dataSets": [
    {
      "action": "Replace",
      "validFrom": "2026-09-28T17:48:53.843+02:00",
      "series": {
        "0:0:0:0:0:0:0": {
          "attributes": [
            0,
            null,
            0,
            0,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            0,
            null,
            null,
            0,
            0,
            0,
            0
          ],
          "observations": {
            "0": [
              2.65,
              0,
              0,
              null,
              null
            ]
          }
        }
      }
    }
  ],
  "structure": {
    "links": [
      {
        "title": "Financial market data",
        "rel": "dataflow",
        "href": "https://data-api.ecb.europa.eu:443/service/dataflow/ECB/FM/1.0"
      }
    ],
    "name": "Financial market data",
    "dimensions": {
      "series": [
        {
          "id": "FREQ",
          "name": "Frequency",
          "values": [
            {
              "id": "B",
              "name": "Daily - businessweek"
            }
          ]
        },
        {
          "id": "REF_AREA",
          "name": "Reference area",
          "values": [
            {
              "id": "U2",
              "name": "Euro area (changing composition)"
            }
          ]
        },
        {
          "id": "CURRENCY",
          "name": "Currency",
          "values": [
            {
              "id": "EUR",
              "name": "Euro"
            }
          ]
        },
        {
          "id": "PROVIDER_FM",
          "name": "Financial market provider",
          "values": [
            {
              "id": "4F",
              "name": "ECB"
            }
          ]
        },
        {
          "id": "INSTRUMENT_FM",
          "name": "Financial market instrument",
          "values": [
            {
              "id": "KR",
              "name": "Key interest rate"
            }
          ]
        },
        {
          "id": "PROVIDER_FM_ID",
          "name": "Financial market provider identifier",
          "values": [
            {
              "id": "MRR_FR",
              "name": "Main refinancing operations - fixed rate tenders (fixed rate) (date of changes)"
            }
          ]
        },
        {
          "id": "DATA_TYPE_FM",
          "name": "Financial market data type",
          "values": [
            {
              "id": "LEV",
              "name": "Level"
            }
          ]
        }
      ],
      "observation": [
        {
          "id": "TIME_PERIOD",
          "name": "Time period or range",
          "role": "time",
          "values": [
            {
              "id": "2026-09-16",
              "name": "2026-09-16",
              "start": "2026-09-16T00:00:00.000+02:00",
              "end": "2026-09-16T23:59:59.999+02:00"
            }
          ]
        }
      ]
    },
    "attributes": {
      "series": [
        {
          "id": "TIME_FORMAT",
          "name": "Time format code",
          "values": [
            {
              "name": "P1D"
            }
          ]
        },
        {
          "id": "BREAKS",
          "name": "Breaks",
          "values": []
        },
        {
          "id": "COLLECTION",
          "name": "Collection indicator",
          "values": [
            {
              "id": "E",
              "name": "End of period"
            }
          ]
        },
        {
          "id": "COMPILING_ORG",
          "name": "Compiling organisation",
          "values": [
            {
              "id": "4F0",
              "name": "European Central Bank (ECB)"
            }
          ]
        },
        {
          "id": "DISS_ORG",
          "name": "Data dissemination organisation",
          "values": []
        },
        {
          "id": "DOM_SER_IDS",
          "name": "Domestic series ids",
          "values": []
        },
        {
          "id": "FM_CONTRACT_TIME",
          "name": "Contract month/expired date",
          "values": []
        },
        {
          "id": "FM_COUPON_RATE",
          "name": "Coupon rate of the bond",
          "values": []
        },
        {
          "id": "FM_IDENTIFIER",
          "name": "Financial instrument Identifier",
          "values": []
        },
        {
          "id": "FM_LOT_SIZE",
          "name": "Lot size units",
          "values": []
        },
        {
          "id": "FM_MATURITY",
          "name": "Bond maturity",
          "values": []
        },
        {
          "id": "FM_OUTS_AMOUNT",
          "name": "Outstanding amount",
          "values": []
        },
        {
          "id": "FM_PUT_CALL",
          "name": "options type",
          "values": []
        },
        {
          "id": "FM_STRIKE_PRICE",
          "name": "Strike price of the options",
          "values": []
        },
        {
          "id": "PUBL_MU",
          "name": "Source publication (Euro area only)",
          "values": []
        },
        {
          "id": "PUBL_PUBLIC",
          "name": "Source publication (public)",
          "values": []
        },
        {
          "id": "UNIT_INDEX_BASE",
          "name": "Unit index base",
          "values": []
        },
        {
          "id": "COMPILATION",
          "name": "Compilation",
          "values": []
        },
        {
          "id": "COVERAGE",
          "name": "Coverage",
          "values": []
        },
        {
          "id": "DECIMALS",
          "name": "Decimals",
          "values": [
            {
              "id": "7",
              "name": "Seven"
            }
          ]
        },
        {
          "id": "SOURCE_AGENCY",
          "name": "Source agency",
          "values": []
        },
        {
          "id": "SOURCE_PUB",
          "name": "Publication source",
          "values": []
        },
        {
          "id": "TITLE",
          "name": "Title",
          "values": [
            {
              "name": "Main refinancing operations - fixed rate tenders (fixed rate) (date of changes) - Level"
            }
          ]
        },
        {
          "id": "TITLE_COMPL",
          "name": "Title complement",
          "values": [
            {
              "name": "Euro area (changing composition) - Key interest rate - Main refinancing operations - fixed rate tenders (fixed rate) (date of changes) - Level - Euro, provided by ECB"
            }
          ]
        },
        {
          "id": "UNIT",
          "name": "Unit",
          "values": [
            {
              "id": "PCPA",
              "name": "Percent per annum"
            }
          ]
        },
        {
          "id": "UNIT_MULT",
          "name": "Unit multiplier",
          "values": [
            {
              "id": "0",
              "name": "Units"
            }
          ]
        }
      ],
      "observation": [
        {
          "id": "OBS_STATUS",
          "name": "Observation status",
          "values": [
            {
              "id": "A",
              "name": "Normal value"
            }
          ]
        },
        {
          "id": "OBS_CONF",
          "name": "Observation confidentiality",
          "values": [
            {
              "id": "F",
              "name": "Free"
            }
          ]
        },
        {
          "id": "OBS_PRE_BREAK",
          "name": "Pre-break observation value",
          "values": []
        },
        {
          "id": "OBS_COM",
          "name": "Observation comment",
          "values": []
        }
      ]
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
