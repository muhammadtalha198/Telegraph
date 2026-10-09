---
intent: CARRIER_SERVICEABILITY
slug: car-kartverket
status: pending_review
captured_at: 2026-10-08T04:42:22Z
request_url: https://ws.geonorge.no/adresser/v1/sok?postnummer=0150&treffPerSide=1&asciiKompatibel=true
content_type: application/json
inputs: |
  {"cc": "NO", "cc_l": "no", "pc": "0150", "locality": "oslo"}
intent_description: |
  Evaluates freight and courier delivery coverage, weight limits, and hazardous material restrictions for target routes.
answer_requirement: |
  Must confirm that the pinned destination postcode (Norway 0150 = OSLO) is a valid, deliverable postal code and return the locality name 'Oslo' (case-insensitive). Proxy for 'lane serviceable or not': weight / hazmat limits are NOT answerable by any keyless source.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "metadata": {
    "treffPerSide": 1,
    "side": 0,
    "totaltAntallTreff": 701,
    "viserFra": 0,
    "viserTil": 1,
    "sokeStreng": "postnummer=0150&treffPerSide=1&asciiKompatibel=true",
    "asciiKompatibel": true
  },
  "adresser": [
    {
      "adressenavn": "Robert Levins gate",
      "adressetekst": "Robert Levins gate 1",
      "adressetilleggsnavn": null,
      "adressekode": 21672,
      "nummer": 1,
      "bokstav": "",
      "kommunenummer": "0301",
      "kommunenavn": "OSLO",
      "gardsnummer": 207,
      "bruksnummer": 454,
      "festenummer": 0,
      "undernummer": null,
      "bruksenhetsnummer": [
        "H0301",
        "H0302",
        "H0303",
        "H0304",
        "H0305",
        "H0306",
        "H0307",
        "H0308",
        "H0309",
        "H0310",
        "H0311",
        "H0312",
        "H0313",
        "H0314",
        "H0401",
        "H0402",
        "H0403",
        "H0404",
        "H0405",
        "H0406",
        "H0407",
        "H0408",
        "H0409",
        "H0410",
        "H0411",
        "H0412",
        "H0413",
        "H0414",
        "H0415",
        "H0501",
        "H0502",
        "H0503",
        "H0504",
        "H0505",
        "H0506",
        "H0507",
        "H0508",
        "H0509",
        "H0510",
        "H0511",
        "H0512",
        "H0513",
        "H0514",
        "H0515",
        "H0601",
        "H0602",
        "H0603",
        "H0604",
        "H0605",
        "H0606",
        "H0607",
        "H0608",
        "H0609",
        "H0610",
        "H0611",
        "H0612",
        "H0613",
        "H0614",
        "H0615",
        "H0701",
        "H0702",
        "H0703",
        "H0704",
        "H0705",
        "H0706",
        "H0707",
        "H0708",
        "H0709",
        "H0710",
        "H0711",
        "H0712",
        "H0713",
        "H0714",
        "H0715",
        "H0716",
        "H0801",
        "H0802",
        "H0803",
        "H0804",
        "H0805",
        "H0806",
        "H0807",
        "H0808",
        "H0809",
        "H0810",
        "H0811",
        "H0812",
        "H0813",
        "H0814",
        "H0815",
        "H0816",
        "H0817",
        "H0901",
        "H0902",
        "H0903",
        "H0904",
        "H0905",
        "H0906",
        "H0907",
        "H0908",
        "H0909",
        "H0910",
        "H0911",
        "H0912",
        "H0913",
        "H0914",
        "H0915",
        "H0916",
        "H0917",
        "H1001",
        "H1002",
        "H1003",
        "H1004",
        "H1005",
        "H1006",
        "H1007",
        "H1008",
        "H1009"
      ],
      "objtype": "Vegadresse",
      "poststed": "OSLO",
      "postnummer": "0150",
      "adressetekstutenadressetilleggsnavn": "Robert Levins gate 1",
      "stedfestingverifisert": false,
      "representasjonspunkt": {
        "epsg": "EPSG:4258",
        "lat": 59.90831627015836,
        "lon": 10.753282665261573
      },
      "oppdateringsdato": "2020-06-15T18:32:03"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
