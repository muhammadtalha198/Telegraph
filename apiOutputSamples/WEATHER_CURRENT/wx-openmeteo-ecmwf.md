---
intent: WEATHER_CURRENT
slug: wx-openmeteo-ecmwf
status: pending_review
captured_at: 2026-10-05T09:33:44Z
request_url: https://api.open-meteo.com/v1/forecast?latitude=1.3521&longitude=103.8198&current=temperature_2m&models=ecmwf_ifs025
content_type: application/json
inputs: |
  {"lat": "1.3521", "lon": "103.8198"}
intent_description: |
  Provides real-time ambient temperature, humidity, precipitation rate, and wind vectors by coordinates.
answer_requirement: |
  Must return current temperature (and ideally humidity/wind/precipitation) for the coordinates asked.
capture_note: |
  golden-test PASS: Open-Meteo / ECMWF
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "latitude": 1.5,
  "longitude": 103.75,
  "generationtime_ms": 0.020742416381835938,
  "utc_offset_seconds": 0,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "elevation": 46.0,
  "current_units": {
    "time": "iso8601",
    "interval": "seconds",
    "temperature_2m": "°C"
  },
  "current": {
    "time": "2026-10-05T09:30",
    "interval": 900,
    "temperature_2m": 30.8
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
