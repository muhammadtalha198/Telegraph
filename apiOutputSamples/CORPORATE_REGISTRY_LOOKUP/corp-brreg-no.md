---
intent: CORPORATE_REGISTRY_LOOKUP
slug: corp-brreg-no
status: approved
captured_at: 2026-10-05T09:33:58Z
request_url: https://data.brreg.no/enhetsregisteret/api/enheter/923609016
content_type: application/json
inputs: |
  {}
intent_description: |
  Queries national business registers for incorporation status, registered agent details, and beneficial ownership filings.
answer_requirement: |
  Must return the company's registry record (legal name, status, identifiers) for the company asked.
capture_note: |
  golden-test PASS: Brønnøysund Register (Norway)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains extensive information about the company but does not include the specific registry record requested."
reviewed_at: 2026-10-05T12:11:31Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "_links": {
    "self": {
      "href": "https://data.brreg.no/enhetsregisteret/api/enheter/923609016"
    }
  },
  "aktivitet": [
    "Selv, eller gjennom deltakelse i eller sammen med andre selskaper å",
    "utvikle, produsere og markedsføre ulike former for energi, avledede",
    "produkter og tjenester, samt annen virksomhet. Utleie av bygg og",
    "anlegg."
  ],
  "antallAnsatte": 21272,
  "erIKonsern": true,
  "forretningsadresse": {
    "adresse": [
      "Forusbeen 50"
    ],
    "kommune": "STAVANGER",
    "kommunenummer": "1103",
    "land": "Norge",
    "landkode": "NO",
    "postnummer": "4035",
    "poststed": "STAVANGER"
  },
  "frivilligMvaRegistrertBeskrivelser": [
    "Utleier av bygg eller anlegg"
  ],
  "harRegistrertAntallAnsatte": true,
  "historiskeNavn": [
    {
      "fraDato": "1995-03-12 16:23:00",
      "navn": "Den norske stats oljeselskap a.s",
      "tilDato": "2001-05-11 08:32:09"
    },
    {
      "fraDato": "2001-05-11 08:32:09",
      "navn": "STATOIL ASA",
      "tilDato": "2007-10-01 06:44:33"
    },
    {
      "fraDato": "2007-10-01 06:44:33",
      "navn": "STATOILHYDRO ASA",
      "tilDato": "2009-11-02 07:56:24"
    },
    {
      "fraDato": "2009-11-02 07:56:24",
      "navn": "STATOIL ASA",
      "tilDato": "2018-05-16 07:05:45"
    }
  ],
  "hjemmeside": "www.equinor.com",
  "institusjonellSektorkode": {
    "beskrivelse": "Statlig eide aksjeselskaper mv.",
    "kode": "1120"
  },
  "kapital": {
    "antallAksjer": 2390749040,
    "belop": 5976872600.0,
    "innfortDato": "2026-07-02",
    "type": "Aksjekapital",
    "valuta": "NOK"
  },
  "konkurs": false,
  "maalform": "Bokmål",
  "naeringskode1": {
    "beskrivelse": "Utvinning av råolje",
    "kode": "06.100"
  },
  "naeringskode2": {
    "beskrivelse": "Utvinning av naturgass",
    "kode": "06.200"
  },
  "naeringskode3": {
    "beskrivelse": "Produksjon av raffinerte petroleumsprodukter og fossile brenselsprodukter",
    "kode": "19.200"
  },
  "navn": "EQUINOR ASA",
  "organisasjonsform": {
    "_links": {
      "self": {
        "href": "https://data.brreg.no/enhetsregisteret/api/organisasjonsformer/ASA"
      }
    },
    "beskrivelse": "Allmennaksjeselskap",
    "kode": "ASA"
  },
  "organisasjonsnummer": "923609016",
  "paategninger": [],
  "postadresse": {
    "adresse": [
      "Postboks 8500"
    ],
    "kommune": "STAVANGER",
    "kommunenummer": "1103",
    "land": "Norge",
    "landkode": "NO",
    "postnummer": "4035",
    "poststed": "STAVANGER"
  },
  "registreringsdatoAntallAnsatteEnhetsregisteret": "2026-09-14",
  "registreringsdatoAntallAnsatteNAVAaregisteret": "2026-09-10",
  "registreringsdatoEnhetsregisteret": "1995-03-12",
  "registreringsdatoForetaksregisteret": "1988-04-28",
  "registreringsdatoFrivilligMerverdiavgiftsregisteret": "2022-09-20",
  "registreringsdatoMerverdiavgiftsregisteret": "1989-07-01",
  "registreringsdatoMerverdiavgiftsregisteretEnhetsregisteret": "2022-09-20",
  "registrertIForetaksregisteret": true,
  "registrertIFrivillighetsregisteret": false,
  "registrertIMvaregisteret": true,
  "registrertIPartiregisteret": false,
  "registrertIStiftelsesregisteret": false,
  "respons_klasse": "Enhet",
  "sisteInnsendteAarsregnskap": "2025",
  "stiftelsesdato": "1972-09-18",
  "telefon": "51 99 00 00",
  "underAvvikling": false,
  "underTvangsavviklingEllerTvangsopplosning": false,
  "vedtektsdato": "2026-05-12",
  "vedtektsfestetFormaal": [
    "Å utvikle, produsere og markedsføre ulike former for energi, avledede",
    "produkter og tjenester, samt annen virksomhet. Virksomheten kan også",
    "drives gjennom deltakelse i eller i samarbeid med andre selskaper."
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains extensive information about the company but does not include the specific registry record requested._
