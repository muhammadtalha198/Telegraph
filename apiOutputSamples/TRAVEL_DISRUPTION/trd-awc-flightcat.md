---
intent: TRAVEL_DISRUPTION
slug: trd-awc-flightcat
status: rejected
captured_at: 2026-10-08T04:43:52Z
request_url: https://aviationweather.gov/api/data/metar?ids=KJFK&format=json
content_type: application/json
inputs: |
  {"icao": "KJFK", "iata": "JFK"}
intent_description: |
  Detects and monitors flight delays, cancellations, gate shifts, and weather-driven travel disruptions in real time.
answer_requirement: |
  For the pinned airport (KJFK / JFK) return a live disruption signal: weather-driven flight category (VFR/MVFR/IFR/LIFR), or the count/size of delayed or cancelled departures. Registered trd-faa-nas (FAA NAS ground stops/delay programs) is the primary; these add independent publishers.
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response focuses on weather conditions and does not include any information about flight disruptions."
reviewed_at: 2026-10-08T05:03:06Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "icaoId": "KJFK",
    "receiptTime": "2026-10-08T03:54:08.128Z",
    "obsTime": 1791431460,
    "reportTime": "2026-10-08T04:00:00.000Z",
    "temp": 15.6,
    "dewp": 11.7,
    "wdir": 220,
    "wspd": 13,
    "wgst": 23,
    "visib": "10+",
    "altim": 1012.6,
    "slp": 1012.5,
    "qcField": 12,
    "metarType": "METAR",
    "rawOb": "METAR KJFK 080351Z 22013G23KT 10SM FEW095 SCT250 16/12 A2990 RMK AO2 SLP125 T01560117 $",
    "lat": 40.6392,
    "lon": -73.7639,
    "elev": 3,
    "name": "New York/JF Kennedy Intl, NY, US",
    "cover": "SCT",
    "clouds": [
      {
        "cover": "FEW",
        "base": 9500
      },
      {
        "cover": "SCT",
        "base": 25000
      }
    ],
    "fltCat": "VFR"
  }
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response focuses on weather conditions and does not include any information about flight disruptions._
