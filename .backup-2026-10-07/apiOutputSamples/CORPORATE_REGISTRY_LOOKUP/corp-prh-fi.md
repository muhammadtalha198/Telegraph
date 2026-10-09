---
intent: CORPORATE_REGISTRY_LOOKUP
slug: corp-prh-fi
status: approved
captured_at: 2026-10-05T09:33:58Z
request_url: https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=0112038-9
content_type: application/json
inputs: |
  {}
intent_description: |
  Queries national business registers for incorporation status, registered agent details, and beneficial ownership filings.
answer_requirement: |
  Must return the company's registry record (legal name, status, identifiers) for the company asked.
capture_note: |
  golden-test PASS: PRH/YTJ (Finland)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the company's legal name and registration date, which are part of the requested information."
reviewed_at: 2026-10-05T12:12:40Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "totalResults": 1,
  "companies": [
    {
      "businessId": {
        "value": "0112038-9",
        "registrationDate": "1978-03-15",
        "source": "3"
      },
      "euId": {
        "value": "FIFPRO.0112038-9",
        "source": "1"
      },
      "names": [
        {
          "name": "Nokia Oyj",
          "type": "1",
          "registrationDate": "1997-09-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Oy Nokia Ab",
          "type": "1",
          "registrationDate": "1966-06-10",
          "endDate": "1997-08-31",
          "version": 2,
          "source": "1"
        },
        {
          "name": "Nokia Networks",
          "type": "3",
          "registrationDate": "2001-10-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Matkapuhelimet",
          "type": "3",
          "registrationDate": "2001-10-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Telecommunications",
          "type": "3",
          "registrationDate": "2001-10-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Telenokia",
          "type": "3",
          "registrationDate": "2001-10-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Mobile Phones",
          "type": "3",
          "registrationDate": "2001-10-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Mobira",
          "type": "3",
          "registrationDate": "2001-10-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "TCC Nokia",
          "type": "3",
          "registrationDate": "2004-11-12",
          "version": 1,
          "source": "1"
        },
        {
          "name": "NMP Trading",
          "type": "3",
          "registrationDate": "2001-10-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Home Communications",
          "type": "3",
          "registrationDate": "2001-10-02",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Internet Communications",
          "type": "3",
          "registrationDate": "2001-10-02",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Vertu",
          "type": "3",
          "registrationDate": "2006-03-08",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Abp",
          "type": "2",
          "registrationDate": "1997-09-01",
          "version": 1,
          "source": "1"
        },
        {
          "name": "Nokia Corporation",
          "type": "2",
          "registrationDate": "1997-09-01",
          "version": 1,
          "source": "1"
        }
      ],
      "mainBusinessLine": {
        "type": "70100",
        "descriptions": [
          {
            "languageCode": "3",
            "description": "Activities of head offices"
          },
          {
            "languageCode": "1",
            "description": "Pääkonttorien toiminta"
          },
          {
            "languageCode": "2",
            "description": "Verksamheter som utövas av huvudkontor"
          }
        ],
        "typeCodeSet": "TOIMI4",
        "registrationDate": "2026-01-01",
        "source": "2"
      },
      "website": {
        "url": "www.nokia.com",
        "registrationDate": "2019-07-01",
        "source": "0"
      },
      "companyForms": [
        {
          "type": "17",
          "descriptions": [
            {
              "languageCode": "1",
              "description": "Julkinen osakeyhtiö"
            },
            {
              "languageCode": "3",
              "description": "Public limited company"
            },
            {
              "languageCode": "2",
              "description": "Publikt aktiebolag"
            }
          ],
          "registrationDate": "1997-09-01",
          "version": 1,
          "source": "1"
        }
      ],
      "companySituations": [],
      "registeredEntries": [
        {
          "type": "1",
          "descriptions": [
            {
              "languageCode": "3",
              "description": "Registered"
            },
            {
              "languageCode": "2",
              "description": "Registrerad"
            },
            {
              "languageCode": "1",
              "description": "Rekisterissä"
            }
          ],
          "registrationDate": "1896-12-19",
          "register": "1",
          "authority": "2"
        },
        {
          "type": "1",
          "descriptions": [
            {
              "languageCode": "3",
              "description": "Registered"
            },
            {
              "languageCode": "2",
              "description": "Registrerad"
            },
            {
              "languageCode": "1",
              "description": "Rekisterissä"
            }
          ],
          "registrationDate": "1978-03-15",
          "register": "4",
          "authority": "1"
        },
        {
          "type": "55",
          "descriptions": [
            {
              "languageCode": "3",
              "description": "Registered"
            },
            {
              "languageCode": "2",
              "description": "Registrerad"
            },
            {
              "languageCode": "1",
              "description": "Rekisterissä"
            }
          ],
          "registrationDate": "1995-03-01",
          "register": "5",
          "authority": "1"
        },
        {
          "type": "80",
          "descriptions": [
            {
              "languageCode": "1",
              "description": "Liiketoiminnasta arvonlisäverovelvollinen"
            },
            {
              "languageCode": "2",
              "description": "Momsskyldig för rörelseverksamhet"
            },
            {
              "languageCode": "3",
              "description": "VAT-liable for business activity"
            }
          ],
          "registrationDate": "1994-06-01",
          "register": "6",
          "authority": "1"
        },
        {
          "type": "82",
          "descriptions": [
            {
              "languageCode": "2",
              "description": "För överlåtelse av nyttjanderätten till en fastighet"
            },
            {
              "languageCode": "1",
              "description": "Kiinteistön käyttöoikeuden luovuttamisesta"
            },
            {
              "languageCode": "3",
              "description": "VAT-obliged for the transfer of rights to use immovable property"
            }
          ],
          "registrationDate": "1995-01-04",
          "register": "6",
          "authority": "1"
        },
        {
          "type": "83",
          "descriptions": [
            {
              "languageCode": "1",
              "description": "Alkutuottajana ja/tai kuvataiteilijana arvonlisäverovelvollinen"
            },
            {
              "languageCode": "2",
              "description": "Momsskyldig som primärproducent och/eller bildkonstnär"
            },
            {
              "languageCode": "3",
              "description": "VAT-liable for agriculture and forestry"
            }
          ],
          "registrationDate": "1995-01-01",
          "register": "6",
          "authority": "1"
        },
        {
          "type": "41",
          "descriptions": [
            {
              "languageCode": "3",
              "description": "Registered"
            },
            {
              "languageCode": "2",
              "description": "Registrerad"
            },
            {
              "languageCode": "1",
              "description": "Rekisterissä"
            }
          ],
          "registrationDate": "1944-01-01",
          "register": "7",
          "authority": "1"
        }
      ],
      "addresses": [
        {
          "type": 1,
          "street": "Karakaari",
          "postCode": "02610",
          "postOffices": [
            {
              "city": "ESBO",
              "languageCode": "2",
              "municipalityCode": "049"
            },
            {
              "city": "ESPOO",
              "languageCode": "1",
              "municipalityCode": "049"
            }
          ],
          "buildingNumber": "7",
          "entrance": "",
          "apartmentNumber": "",
          "apartmentIdSuffix": "",
          "co": "",
          "registrationDate": "2019-07-01",
          "source": "0"
        },
        {
          "type": 2,
          "street": "",
          "postCode": "00045",
          "postOffices": [
            {
              "city": "NOKIA GROUP",
              "languageCode": "1",
              "municipalityCode": "091"
            },
            {
              "city": "NOKIA GROUP",
              "languageCode": "2",
              "municipalityCode": "091"
            }
          ],
          "postOfficeBox": "226",
          "buildingNumber": "",
          "entrance": "",
          "apartmentNumber": "",
          "apartmentIdSuffix": "",
          "co": "",
          "registrationDate": "2014-09-30",
          "source": "0"
        }
      ],
      "tradeRegisterStatus": "1",
      "status": "2",
      "registrationDate": "1896-12-19",
      "lastModified": "2026-08-19T10:04:06"
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the company's legal name and registration date, which are part of the requested information._
