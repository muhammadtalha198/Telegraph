---
intent: LOAN_INTEREST_RATE_QUOTE
slug: lnr-norges-bank
status: pending_review
captured_at: 2026-10-08T04:42:39Z
request_url: https://data.norges-bank.no/api/data/IR/B.KPRA.SD.R?format=sdmx-json&lastNObservations=1
content_type: application/json
inputs: |
  {}
intent_description: |
  Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.
answer_requirement: |
  Must return a published lending / policy / benchmark interest rate (percent) for the pinned country and date or period.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "meta": {
    "id": "IREF345586",
    "prepared": "2026-10-08T04:42:39",
    "test": false,
    "datasetId": "c2ade8b5-4746-40a8-b11e-dd176046ef85",
    "sender": {
      "id": "Unknown"
    },
    "receiver": {
      "id": "guest"
    },
    "links": [
      {
        "rel": "self",
        "href": "/data/IR/B.KPRA.SD.R?format=sdmx-json&lastNObservations=1",
        "uri": "https://raw.githubusercontent.com/sdmx-twg/sdmx-json/develop/data-message/tools/schemas/1.0/sdmx-json-data-schema.json"
      }
    ]
  },
  "data": {
    "dataSets": [
      {
        "links": [
          {
            "rel": "dataflow",
            "urn": "urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=NB:IR(1.1)"
          }
        ],
        "reportingBegin": "2026-10-06T00:00:00",
        "reportingEnd": "2026-10-06T23:59:59",
        "action": "Information",
        "series": {
          "0:0:0:0": {
            "attributes": [
              0,
              0
            ],
            "observations": {
              "0": [
                "4.5"
              ]
            }
          }
        }
      }
    ],
    "structure": {
      "links": [
        {
          "rel": "dataflow",
          "urn": "urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=NB:IR(1.1)"
        },
        {
          "rel": "datastructure",
          "urn": "urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=NB:DSD_IR(1.1)"
        }
      ],
      "name": "Policy rate",
      "names": {
        "en": "Policy rate",
        "no": "Styringsrente"
      },
      "description": "Policy rate",
      "descriptions": {
        "en": "Policy rate",
        "no": "Styringsrente"
      },
      "dimensions": {
        "dataset": [],
        "series": [
          {
            "id": "FREQ",
            "name": "Frequency",
            "description": "The time interval at which observations occur over a given time period.",
            "keyPosition": 0,
            "role": null,
            "values": [
              {
                "id": "B",
                "name": "Business",
                "description": "Business"
              }
            ]
          },
          {
            "id": "INSTRUMENT_TYPE",
            "name": "Instrument Type",
            "description": "Type of financial instrument.",
            "keyPosition": 1,
            "role": null,
            "values": [
              {
                "id": "KPRA",
                "name": "Key policy rate",
                "description": "The sight deposit rate. The interest rate on banks' reserves up to a specified quota in Norges Bank."
              }
            ]
          },
          {
            "id": "TENOR",
            "name": "Tenor",
            "description": "The amount of time left for the repayment of a loan or until a financial contract expires.",
            "keyPosition": 2,
            "role": null,
            "values": [
              {
                "id": "SD",
                "name": "Policy rate"
              }
            ]
          },
          {
            "id": "UNIT_MEASURE",
            "name": "Unit of Measure",
            "description": "The unit in which the data values are measured.",
            "keyPosition": 3,
            "role": null,
            "values": [
              {
                "id": "R",
                "name": "Rate"
              }
            ]
          }
        ],
        "observation": [
          {
            "id": "TIME_PERIOD",
            "name": "Time Period",
            "description": "The period of time or point in time to which the measured observation refers.",
            "keyPosition": 4,
            "role": "time",
            "values": [
              {
                "start": "2026-10-06T00:00:00",
                "end": "2026-10-06T23:59:59",
                "id": "2026-10-06",
                "name": "2026-10-06"
              }
            ]
          }
        ]
      },
      "attributes": {
        "dataset": [],
        "series": [
          {
            "id": "DECIMALS",
            "name": "Decimals",
            "description": "The number of digits to the right of a decimal point.",
            "relationship": {
              "dimensions": [
                "INSTRUMENT_TYPE",
                "TENOR",
                "UNIT_MEASURE"
              ]
            },
            "role": null,
            "values": [
              {
                "id": "2",
                "name": "2"
              }
            ]
          },
          {
            "id": "COLLECTION",
            "name": "Collection Indicator",
            "description": "Dates or periods during which the observations have been collected.",
            "relationship": {
              "dimensions": [
                "INSTRUMENT_TYPE",
                "TENOR",
                "UNIT_MEASURE"
              ]
            },
            "role": null,
            "values": [
              {
                "id": "E",
                "name": "End of day"
              }
            ]
          }
        ],
        "observation": [
          {
            "id": "CALC_METHOD",
            "name": "Calculation Method",
            "description": "Method used for calculation of values",
            "relationship": {
              "primaryMeasure": "OBS_VALUE"
            },
            "role": null,
            "values": []
          }
        ]
      }
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
