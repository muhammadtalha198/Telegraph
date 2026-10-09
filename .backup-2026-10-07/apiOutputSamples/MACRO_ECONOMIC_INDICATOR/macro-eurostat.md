---
intent: MACRO_ECONOMIC_INDICATOR
slug: macro-eurostat
status: approved
captured_at: 2026-10-05T09:36:33Z
request_url: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/une_rt_a?geo=DE&age=Y15-74&sex=T&unit=PC_ACT&time=2019
content_type: application/json
inputs: |
  {"iso2": "DE", "iso3": "DEU"}
intent_description: |
  Aggregates released central bank interest rates, consumer price index (CPI) updates, and unemployment figures.
answer_requirement: |
  Must return the requested macro indicator value (unemployment / CPI / policy rate) for the country and period.
capture_note: |
  golden-test PASS: Eurostat
reviewer_note: "auto_review: [0.80|heuristic+llm] The response provides the requested unemployment rate for Germany in the specified period and age group."
reviewed_at: 2026-10-05T12:31:28Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 0.800
---

## Raw API output

```json
{
  "version": "2.0",
  "class": "dataset",
  "label": "Unemployment by sex and age - annual data",
  "source": "ESTAT",
  "updated": "2026-09-10T23:00:00+0200",
  "value": {
    "0": 2.9
  },
  "id": [
    "freq",
    "age",
    "unit",
    "sex",
    "geo",
    "time"
  ],
  "size": [
    1,
    1,
    1,
    1,
    1,
    1
  ],
  "dimension": {
    "freq": {
      "label": "Time frequency",
      "category": {
        "index": {
          "A": 0
        },
        "label": {
          "A": "Annual"
        }
      }
    },
    "age": {
      "label": "Age class",
      "category": {
        "index": {
          "Y15-74": 0
        },
        "label": {
          "Y15-74": "From 15 to 74 years"
        }
      }
    },
    "unit": {
      "label": "Unit of measure",
      "category": {
        "index": {
          "PC_ACT": 0
        },
        "label": {
          "PC_ACT": "Percentage of population in the labour force"
        }
      }
    },
    "sex": {
      "label": "Sex",
      "category": {
        "index": {
          "T": 0
        },
        "label": {
          "T": "Total"
        }
      }
    },
    "geo": {
      "label": "Geopolitical entity (reporting)",
      "category": {
        "index": {
          "DE": 0
        },
        "label": {
          "DE": "Germany"
        }
      }
    },
    "time": {
      "label": "Time",
      "category": {
        "index": {
          "2019": 0
        },
        "label": {
          "2019": "2019"
        }
      }
    }
  },
  "extension": {
    "lang": "EN",
    "id": "UNE_RT_A",
    "agencyId": "ESTAT",
    "version": "1.0",
    "datastructure": {
      "id": "UNE_RT_A",
      "agencyId": "ESTAT",
      "version": "48.0"
    },
    "annotation": [
      {
        "type": "CREATED",
        "date": "2021-07-14T12:27:40+0200"
      },
      {
        "type": "DISSEMINATION_DOI_XML",
        "title": "<adms:identifier xmlns:adms=\"http://www.w3.org/ns/adms#\" xmlns:skos=\"http://www.w3.org/2004/02/skos/core.html\" xmlns:dct=\"http://purl.org/dc/terms/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"><adms:Identifier rdf:about=\"https://doi.org/10.2908/UNE_RT_A\"><skos:notation rdf:datatype=\"http://purl.org/spar/datacite/doi\">10.2908/UNE_RT_A</skos:notation><dct:creator rdf:resource=\"http://publications.europa.eu/resource/authority/corporate-body/ESTAT\"/><dct:issued rdf:datatype=\"http://www.w3.org/2001/XMLSchema#date\">2023-01-23</dct:issued></adms:Identifier></adms:identifier>"
      },
      {
        "type": "DISSEMINATION_EXPLANATORY_LINK",
        "title": "text-category",
        "href": "https://ec.europa.eu/eurostat/databrowser-backend/api/public/explanatory-notes/get/Info_note_LFSQ_20240604.pdf",
        "text": "Information note"
      },
      {
        "type": "DISSEMINATION_EXPLANATORY_LINK",
        "title": "text-category",
        "href": "https://ec.europa.eu/eurostat/databrowser-backend/api/public/explanatory-notes/get/Info_note_LFSQ_20240604.pdf"
      },
      {
        "type": "DISSEMINATION_EXPLANATORY_LINK",
        "title": "text-category",
        "href": "https://ec.europa.eu/eurostat/databrowser-backend/api/public/explanatory-notes/get/Info_note_LFSQ_20240604.pdf"
      },
      {
        "type": "DISSEMINATION_OBJECT_TYPE",
        "title": "DATASET"
      },
      {
        "type": "DISSEMINATION_TIMESTAMP_DATA",
        "date": "2026-09-10T23:00:00+0200"
      },
      {
        "type": "DISSEMINATION_TIMESTAMP_GLOBAL",
        "date": "2026-09-10T23:00:00+0200"
      },
      {
        "type": "DISSEMINATION_TIMESTAMP_PLANNED",
        "date": "2026-09-10T23:00:00+0200"
      },
      {
        "type": "ESMS_HTML",
        "title": "Explanatory texts (metadata)",
        "href": "https://ec.europa.eu/eurostat/cache/metadata/en/lfsi_esms.htm"
      },
      {
        "type": "ESMS_SDMX",
        "title": "Explanatory texts (metadata)",
        "href": "https://ec.europa.eu/eurostat/api/dissemination/files?file=metadata/lfsi_esms.sdmx.zip"
      },
      {
        "type": "OBS_COUNT",
        "title": "39708"
      },
      {
        "type": "OBS_PERIOD_OVERALL_LATEST",
        "title": "2025"
      },
      {
        "type": "OBS_PERIOD_OVERALL_OLDEST",
        "title": "2003"
      },
      {
        "type": "SOURCE_INSTITUTIONS",
        "text": "Eurostat"
      },
      {
        "type": "UPDATE_DATA",
        "date": "2026-09-10T23:00:00+0200"
      },
      {
        "type": "UPDATE_STRUCTURE",
        "date": "2026-03-12T23:00:00+0100"
      }
    ],
    "positions-with-no-data": {
      "freq": [],
      "age": [],
      "unit": [],
      "sex": [],
      "geo": [],
      "time": []
    }
  }
}
```

## Why this matches (or not)

_[0.80|heuristic+llm] The response provides the requested unemployment rate for Germany in the specified period and age group._
