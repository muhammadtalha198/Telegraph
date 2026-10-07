---
intent: AIR_QUALITY_INDEX
slug: aq-openmeteo
status: pending_review
captured_at: 2026-10-05T09:38:41Z
request_url: https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.405&current=pm2_5,pm10,us_aqi
content_type: application/json
inputs: |
  {"lat": "52.52", "lon": "13.405"}
intent_description: |
  Aggregates particulate matter (PM2.5/PM10), ground ozone, and composite AQI metrics from monitoring stations.
answer_requirement: |
  Must return the air-quality reading (AQI and/or PM2.5/PM10/ozone) at the location asked.
capture_note: |
  golden-test PASS: Open-Meteo Air Quality (CAMS)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "latitude": 52.5,
  "longitude": 13.400002,
  "generationtime_ms": 1.640915870666504,
  "utc_offset_seconds": 0,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "elevation": 37.0,
  "current_units": {
    "time": "iso8601",
    "interval": "seconds",
    "pm2_5": "μg/m³",
    "pm10": "μg/m³",
    "us_aqi": "USAQI"
  },
  "current": {
    "time": "2026-10-05T09:00",
    "interval": 3600,
    "pm2_5": 22.8,
    "pm10": 26.0,
    "us_aqi": 60
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
