---
intent: CORPORATE_REGISTRY_LOOKUP
slug: corp-sk-rpo
status: approved
captured_at: 2026-10-08T04:42:31Z
request_url: https://api.statistics.sk/rpo/v1/search?identifier=31322832
content_type: application/json
inputs: |
  {"sk_ico": "31322832"}
intent_description: |
  Queries national business registers for incorporation status, registered agent details, and beneficial ownership filings.
answer_requirement: |
  Must return the company's registry record (legal name, status/validity, identifiers) for the pinned company.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the requested company's registry record and related details."
reviewed_at: 2026-10-08T04:59:35Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "results": [
    {
      "id": 1003617,
      "dbModificationDate": "2026-07-09",
      "identifiers": [
        {
          "value": "31322832",
          "validFrom": "1992-04-29"
        }
      ],
      "fullNames": [
        {
          "value": "SLOVNAFT a.s.",
          "validFrom": "1992-04-29",
          "validTo": "1998-11-29"
        },
        {
          "value": "SLOVNAFT , a.s.",
          "validFrom": "1998-11-30",
          "validTo": "2008-05-29"
        },
        {
          "value": "SLOVNAFT, a.s.",
          "validFrom": "2008-05-30"
        }
      ],
      "addresses": [
        {
          "validFrom": "2006-06-16",
          "street": "Vlčie hrdlo",
          "regNumber": 0,
          "buildingNumber": "1",
          "postalCodes": [
            "82412"
          ],
          "municipality": {
            "value": "Bratislava"
          },
          "country": {
            "value": "Slovenská republika",
            "code": "703",
            "codelistCode": "CL000086"
          }
        },
        {
          "validFrom": "1992-04-29",
          "validTo": "2006-06-15",
          "street": "Vlčie hrdlo",
          "regNumber": 0,
          "postalCodes": [
            "82412"
          ],
          "municipality": {
            "value": "Bratislava"
          },
          "country": {
            "value": "Slovenská republika",
            "code": "703",
            "codelistCode": "CL000086"
          }
        }
      ],
      "establishment": "1992-05-01",
      "sourceRegister": {
        "value": {
          "value": "Obchodný register",
          "code": "1",
          "codelistCode": "CL010112"
        },
        "registrationOffices": [
          {
            "value": "Mestský súd Bratislava III",
            "validFrom": "1992-04-29"
          }
        ],
        "registrationNumbers": [
          {
            "value": "Sa/426/B",
            "validFrom": "1992-04-29"
          }
        ]
      }
    }
  ],
  "license": "1. ŠÚ SR ako správca informačného systému RPO uplatňuje na použitie sprístupnených údajov z RPO uvedených v § 7 ods. 2 a § 7a ods. 4 zákona č. 272/2015 Z. z. o registri právnických osôb, podnikateľov a orgánov verejnej moci a o zmene a doplnení niektorých zákonov (ďalej len „zákon o registri právnických osôb“) medzinárodnú verejnú licenciu Creative Commons Attribution License (cc-by) 4.0 (ďalej len „verejná licencia“).\n2. Predmetom verejnej licencie sú sprístupnené údaje z RPO prostredníctvom webového sídla ŠÚ SR v zmysle § 7 ods. 2 a § 7a ods. 4 zákona o registri právnických osôb.\n3. ŠÚ SR udeľuje súhlas na použitie predmetu verejnej licencie a výkon licencovaných práv („licencia“) podľa vyššie citovanej verejnej licencie."
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the requested company's registry record and related details._
