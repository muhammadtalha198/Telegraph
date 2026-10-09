---
intent: WEATHER_CURRENT
slug: wx-openmeteo-icon
status: pending_review
captured_at: 2026-10-05T09:33:44Z
request_url: https://api.open-meteo.com/v1/forecast?latitude=1.3521&longitude=103.8198&current=temperature_2m&models=icon_seamless
content_type: application/json
inputs: |
  {"lat": "1.3521", "lon": "103.8198"}
intent_description: |
  Provides real-time ambient temperature, humidity, precipitation rate, and wind vectors by coordinates.
answer_requirement: |
  Must return current temperature (and ideally humidity/wind/precipitation) for the coordinates asked.
capture_note: |
  golden-test PASS: Open-Meteo / DWD ICON
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "latitude": 1.375,
  "longitude": 103.875,
  "generationtime_ms": 0.023245811462402344,
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
    "temperature_2m": 31.7
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
