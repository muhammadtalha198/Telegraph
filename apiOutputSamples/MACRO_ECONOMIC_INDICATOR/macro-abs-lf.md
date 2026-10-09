---
intent: MACRO_ECONOMIC_INDICATOR
slug: macro-abs-lf
status: rejected
captured_at: 2026-10-08T04:42:12Z
request_url: https://data.api.abs.gov.au/rest/data/ABS,LF,1.0.0/M13.3.1599.20.AUS.M?startPeriod=2019-12&endPeriod=2019-12&format=jsondata
content_type: application/vnd.sdmx.data+json
inputs: |
  {"oecd_ref": "AUS", "oecd_freq": "M", "period": "2019-12"}
intent_description: |
  Aggregates released central bank interest rates, consumer price index (CPI) updates, and unemployment figures.
answer_requirement: |
  Must return the unemployment rate (percent of labour force, ages 15+, total sexes) for the pinned country and period as a plain number.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains a different metric (unemployment rate) than requested and does not provide the requested unemployment rate value."
reviewed_at: 2026-10-08T04:56:50Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "meta": {
    "schema": "https://raw.githubusercontent.com/sdmx-twg/sdmx-json/master/data-message/tools/schemas/2.0.0/sdmx-json-data-schema.json",
    "id": "IREF003502",
    "prepared": "2026-10-08T04:42:10Z",
    "test": true,
    "contentLanguages": [
      "en"
    ],
    "sender": {
      "id": "Stable_-_DotStat_v8",
      "name": "unknown",
      "names": {
        "en": "unknown"
      }
    }
  },
  "data": {
    "dataSets": [
      {
        "structure": 0,
        "action": "Information",
        "links": [
          {
            "urn": "urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=ABS:LF(1.0.0)",
            "rel": "DataStructure"
          }
        ],
        "annotations": [
          0,
          1,
          2,
          3,
          4,
          5,
          6
        ],
        "series": {
          "0:0:0:0:0:0": {
            "attributes": [
              0,
              0
            ],
            "annotations": [],
            "observations": {
              "0": [
                5.04210808,
                null,
                null,
                0
              ]
            }
          }
        }
      }
    ],
    "structures": [
      {
        "name": "Labour Force",
        "names": {
          "en": "Labour Force"
        },
        "description": "Dataset: LF. Headline estimates of employment, unemployment, underemployment, participation and hours worked from the monthly Labour Force Survey. Unit of measure: Persons/rate/ratio/percent. Geographic coverage: Australia/State. Catalogue number: 6202.0",
        "descriptions": {
          "en": "Dataset: LF. Headline estimates of employment, unemployment, underemployment, participation and hours worked from the monthly Labour Force Survey. Unit of measure: Persons/rate/ratio/percent. Geographic coverage: Australia/State. Catalogue number: 6202.0"
        },
        "dimensions": {
          "dataSet": [],
          "series": [
            {
              "id": "MEASURE",
              "name": "Measure",
              "names": {
                "en": "Measure"
              },
              "keyPosition": 0,
              "roles": [
                "MEASURE"
              ],
              "values": [
                {
                  "id": "M13",
                  "order": 12,
                  "name": "Unemployment rate",
                  "names": {
                    "en": "Unemployment rate"
                  }
                }
              ]
            },
            {
              "id": "SEX",
              "name": "Sex",
              "names": {
                "en": "Sex"
              },
              "keyPosition": 1,
              "roles": [
                "SEX"
              ],
              "values": [
                {
                  "id": "3",
                  "order": 0,
                  "name": "Persons",
                  "names": {
                    "en": "Persons"
                  },
                  "annotations": [
                    7
                  ]
                }
              ]
            },
            {
              "id": "AGE",
              "name": "Age",
              "names": {
                "en": "Age"
              },
              "keyPosition": 2,
              "roles": [
                "AGE"
              ],
              "values": [
                {
                  "id": "1599",
                  "order": 0,
                  "name": "Total (age)",
                  "names": {
                    "en": "Total (age)"
                  },
                  "annotations": [
                    8
                  ]
                }
              ]
            },
            {
              "id": "TSEST",
              "name": "Adjustment Type",
              "names": {
                "en": "Adjustment Type"
              },
              "keyPosition": 3,
              "roles": [
                "TSEST"
              ],
              "values": [
                {
                  "id": "20",
                  "order": 1,
                  "name": "Seasonally Adjusted",
                  "names": {
                    "en": "Seasonally Adjusted"
                  },
                  "annotations": [
                    9,
                    10
                  ]
                }
              ],
              "annotations": [
                11
              ]
            },
            {
              "id": "REGION",
              "name": "Region",
              "names": {
                "en": "Region"
              },
              "keyPosition": 4,
              "roles": [
                "REGION"
              ],
              "values": [
                {
                  "id": "AUS",
                  "order": 0,
                  "name": "Australia",
                  "names": {
                    "en": "Australia"
                  },
                  "annotations": [
                    12
                  ]
                }
              ]
            },
            {
              "id": "FREQ",
              "name": "Frequency",
              "names": {
                "en": "Frequency"
              },
              "keyPosition": 5,
              "roles": [
                "FREQ"
              ],
              "values": [
                {
                  "id": "M",
                  "order": 7,
                  "name": "Monthly",
                  "names": {
                    "en": "Monthly"
                  }
                }
              ]
            }
          ],
          "observation": [
            {
              "id": "TIME_PERIOD",
              "name": "Time Period",
              "names": {
                "en": "Time Period"
              },
              "keyPosition": 6,
              "roles": [
                "TIME_PERIOD"
              ],
              "values": [
                {
                  "start": "2019-12-01T00:00:00",
                  "end": "2019-12-31T00:00:00",
                  "id": "2019-12",
                  "name": "2019-12",
                  "names": {
                    "en": "2019-12"
                  }
                }
              ]
            }
          ]
        },
        "attributes": {
          "dataSet": [],
          "dimensionGroup": [],
          "series": [
            {
              "id": "UNIT_MEASURE",
              "name": "Unit of Measure",
              "names": {
                "en": "Unit of Measure"
              },
              "roles": [
                "UNIT_MEASURE"
              ],
              "relationship": {
                "dimensions": [
                  "MEASURE"
                ]
              },
              "values": [
                {
                  "id": "PCT",
                  "order": 2,
                  "name": "Percent",
                  "names": {
                    "en": "Percent"
                  }
                }
              ],
              "annotations": [
                13
              ]
            },
            {
              "id": "UNIT_MULT",
              "name": "Unit of Multiplier",
              "names": {
                "en": "Unit of Multiplier"
              },
              "roles": [
                "UNIT_MULT"
              ],
              "relationship": {
                "dimensions": [
                  "MEASURE"
                ]
              },
              "values": [
                {
                  "id": "0",
                  "order": 0,
                  "name": "Units",
                  "names": {
                    "en": "Units"
                  }
                }
              ],
              "annotations": [
                14
              ]
            }
          ],
          "observation": [
            {
              "id": "OBS_STATUS",
              "name": "Observation Status",
              "names": {
                "en": "Observation Status"
              },
              "roles": [
                "OBS_STATUS"
              ],
              "relationship": {
                "observation": {}
              },
              "values": []
            },
            {
              "id": "OBS_COMMENT",
              "name": "Observation Comment",
              "names": {
                "en": "Observation Comment"
              },
              "roles": [
                "OBS_COMMENT"
              ],
              "relationship": {
                "observation": {}
              },
              "values": []
            },
            {
              "id": "DECIMALS",
              "name": "Decimals",
              "names": {
                "en": "Decimals"
              },
              "roles": [
                "DECIMALS"
              ],
              "relationship": {
                "observation": {}
              },
              "values": [
                {
                  "id": "1",
                  "order": 1,
                  "name": "One",
                  "names": {
                    "en": "One"
                  }
                }
              ]
            }
          ]
        },
        "annotations": [
          {
            "type": "NonProductionDataflow",
            "text": "true",
            "texts": {
              "en": "true"
            }
          },
          {
            "title": "TIME_PERIOD",
            "type": "LAYOUT_COLUMN"
          },
          {
            "title": "MEASURE",
            "type": "LAYOUT_ROW"
          },
          {
            "title": "TSEST",
            "type": "LAYOUT_ROW_SECTION"
          },
          {
            "title": "REGION=AUS,SEX=3,AGE=1599,FREQ=M,LASTNPERIODS=18",
            "type": "DEFAULT"
          },
          {
            "type": "EXT_RESOURCE",
            "text": "Methodology|https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release#methodology|https://www.abs.gov.au/ausstats/wmdata.nsf/activeimages/methodology/$File/methodology.png",
            "texts": {
              "en": "Methodology|https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release#methodology|https://www.abs.gov.au/ausstats/wmdata.nsf/activeimages/methodology/$File/methodology.png"
            }
          },
          {
            "title": "200",
            "type": "MAXTEXTATTRIBUTELENGTH"
          },
          {
            "type": "ORDER",
            "text": "3",
            "texts": {
              "en": "3"
            }
          },
          {
            "type": "ORDER",
            "text": "600",
            "texts": {
              "en": "600"
            }
          },
          {
            "type": "ORDER",
            "text": "2",
            "texts": {
              "en": "2"
            }
          },
          {
            "type": "FULL_NAME",
            "text": "Seasonally Adjusted",
            "texts": {
              "en": "Seasonally Adjusted"
            }
          },
          {
            "type": "OTHER_LINKS",
            "text": "https://www.abs.gov.au/websitedbs/D3310114.nsf/home/Time+Series+Analysis:+The+Basics",
            "texts": {
              "en": "https://www.abs.gov.au/websitedbs/D3310114.nsf/home/Time+Series+Analysis:+The+Basics"
            }
          },
          {
            "type": "ORDER",
            "text": "10",
            "texts": {
              "en": "10"
            }
          },
          {
            "type": "CONTEXT",
            "text": "If a unit multiplier exists the data is recorded according to the combination of the unit multiplier and the unit of measure.",
            "texts": {
              "en": "If a unit multiplier exists the data is recorded according to the combination of the unit multiplier and the unit of measure."
            }
          },
          {
            "type": "CONTEXT",
            "text": "Codes for unit of multiplier are the exponent in base 10 so that multiplying the observation by 10^UNIT_MULT gives a value expressed in the unit of measure.",
            "texts": {
              "en": "Codes for unit of multiplier are the exponent in base 10 so that multiplying the observation by 10^UNIT_MULT gives a value expressed in the unit of measure."
            }
          }
        ],
        "dataSets": [
          0
        ]
      }
    ]
  },
  "errors": []
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains a different metric (unemployment rate) than requested and does not provide the requested unemployment rate value._
