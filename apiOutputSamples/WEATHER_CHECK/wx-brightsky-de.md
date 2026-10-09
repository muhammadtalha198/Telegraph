---
intent: WEATHER_CHECK
slug: wx-brightsky-de
status: rejected
captured_at: 2026-10-09T10:35:30Z
request_url: https://api.brightsky.dev/current_weather?lat=52.52&lon=13.41
content_type: application/json
inputs: |
  lat=52.52,lon=13.41
intent_description: |
  Provides real-time ambient temperature, humidity, precipitation rate, and wind vectors by coordinates.
answer_requirement: |
  Must return current temperature for the coordinates asked.
capture_note: |
  DWD; Germany + border coverage only
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides weather conditions but does not include the requested current temperature for the coordinates asked."
reviewed_at: 2026-10-09T10:35:59Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "weather": {
    "source_id": 303711,
    "timestamp": "2026-10-09T10:00:00+00:00",
    "cloud_cover": 100,
    "condition": "dry",
    "dew_point": 6.85,
    "solar_10": 0.028,
    "solar_30": 0.12,
    "solar_60": 0.275,
    "precipitation_10": 0.0,
    "precipitation_30": 0.0,
    "precipitation_60": 0.0,
    "pressure_msl": 1013.1,
    "relative_humidity": 64,
    "visibility": 57321,
    "wind_direction_10": 250,
    "wind_direction_30": 250,
    "wind_direction_60": 248,
    "wind_speed_10": 23.0,
    "wind_speed_30": 23.8,
    "wind_speed_60": 22.7,
    "wind_gust_direction_10": 230,
    "wind_gust_direction_30": 230,
    "wind_gust_direction_60": 230,
    "wind_gust_speed_10": 37.4,
    "wind_gust_speed_30": 40.0,
    "wind_gust_speed_60": 40.0,
    "sunshine_30": 6.0,
    "sunshine_60": 29.0,
    "temperature": 13.5,
    "fallback_source_ids": {
      "solar_10": 254907,
      "solar_60": 254907,
      "sunshine_60": 254907,
      "sunshine_30": 254907,
      "solar_30": 254907
    },
    "icon": "cloudy"
  },
  "sources": [
    {
      "id": 303711,
      "dwd_station_id": "00433",
      "observation_type": "synop",
      "lat": 52.4676,
      "lon": 13.402,
      "height": 47.7,
      "station_name": "Berlin-Tempelhof",
      "wmo_station_id": "10384",
      "first_record": "2026-10-08T04:30:00+00:00",
      "last_record": "2026-10-09T10:00:00+00:00",
      "distance": 5858.0
    },
    {
      "id": 254907,
      "dwd_station_id": "03987",
      "observation_type": "synop",
      "lat": 52.3813,
      "lon": 13.0622,
      "height": 80.9,
      "station_name": "Potsdam",
      "wmo_station_id": "10379",
      "first_record": "2026-10-08T04:30:00+00:00",
      "last_record": "2026-10-09T10:10:00+00:00",
      "distance": 28199.0
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides weather conditions but does not include the requested current temperature for the coordinates asked._
