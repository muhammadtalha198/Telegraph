---
intent: WEATHER_CHECK
slug: wx-openmeteo-icon
status: pending_review
captured_at: 2026-10-05T05:44:50Z
request_url: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m&models=icon_seamless
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 7 keyless. Open-Meteo model variants share a host - count as 1 source if you enforce one-publisher-per-miner.
answer_requirement: |
  Must satisfy catalog intent WEATHER_CHECK via upstream Open-Meteo / DWD ICON
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "latitude": 52.52,
  "longitude": 13.419998,
  "generationtime_ms": 0.032067298889160156,
  "utc_offset_seconds": 0,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "elevation": 38.0,
  "current_units": {
    "time": "iso8601",
    "interval": "seconds",
    "temperature_2m": "°C"
  },
  "current": {
    "time": "2026-10-05T05:30",
    "interval": 900,
    "temperature_2m": 9.0
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
