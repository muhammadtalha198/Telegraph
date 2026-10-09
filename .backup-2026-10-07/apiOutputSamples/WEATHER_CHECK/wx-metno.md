---
intent: WEATHER_CHECK
slug: wx-metno
status: approved
captured_at: 2026-10-05T05:44:56Z
request_url: https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=52.52&lon=13.41
content_type: application/json
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 7 keyless. Open-Meteo model variants share a host - count as 1 source if you enforce one-publisher-per-miner.
answer_requirement: |
  Must satisfy catalog intent WEATHER_CHECK via upstream MET Norway
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:34Z
---

## Raw API output

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      13.41,
      52.52,
      37
    ]
  },
  "properties": {
    "meta": {
      "updated_at": "2026-10-05T05:24:54Z",
      "units": {
        "air_pressure_at_sea_level": "hPa",
        "air_temperature": "celsius",
        "cloud_area_fraction": "%",
        "precipitation_amount": "mm",
        "relative_humidity": "%",
        "wind_from_direction": "degrees",
        "wind_speed": "m/s"
      }
    },
    "timeseries": [
      {
        "time": "2026-10-05T05:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1025.0,
              "air_temperature": 9.5,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 92.5,
              "wind_from_direction": 225.5,
              "wind_speed": 2.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1025.1,
              "air_temperature": 9.9,
              "cloud_area_fraction": 86.7,
              "relative_humidity": 92.0,
              "wind_from_direction": 216.7,
              "wind_speed": 2.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T07:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1025.3,
              "air_temperature": 11.5,
              "cloud_area_fraction": 39.8,
              "relative_humidity": 86.6,
              "wind_from_direction": 206.8,
              "wind_speed": 2.6
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T08:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1025.2,
              "air_temperature": 13.8,
              "cloud_area_fraction": 3.1,
              "relative_humidity": 81.0,
              "wind_from_direction": 210.6,
              "wind_speed": 2.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T09:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1025.1,
              "air_temperature": 16.2,
              "cloud_area_fraction": 4.7,
              "relative_humidity": 73.0,
              "wind_from_direction": 233.8,
              "wind_speed": 2.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T10:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1024.8,
              "air_temperature": 18.1,
              "cloud_area_fraction": 20.3,
              "relative_humidity": 63.3,
              "wind_from_direction": 247.7,
              "wind_speed": 2.5
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T11:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1024.3,
              "air_temperature": 19.2,
              "cloud_area_fraction": 53.1,
              "relative_humidity": 56.3,
              "wind_from_direction": 252.3,
              "wind_speed": 3.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1023.5,
              "air_temperature": 19.8,
              "cloud_area_fraction": 25.8,
              "relative_humidity": 52.1,
              "wind_from_direction": 244.6,
              "wind_speed": 3.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T13:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1022.9,
              "air_temperature": 20.2,
              "cloud_area_fraction": 53.9,
              "relative_humidity": 49.4,
              "wind_from_direction": 240.4,
              "wind_speed": 3.1
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T14:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1022.2,
              "air_temperature": 20.2,
              "cloud_area_fraction": 43.0,
              "relative_humidity": 48.5,
              "wind_from_direction": 230.8,
              "wind_speed": 3.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T15:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1021.7,
              "air_temperature": 19.8,
              "cloud_area_fraction": 84.4,
              "relative_humidity": 50.8,
              "wind_from_direction": 234.1,
              "wind_speed": 3.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T16:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1021.4,
              "air_temperature": 18.3,
              "cloud_area_fraction": 82.8,
              "relative_humidity": 59.6,
              "wind_from_direction": 231.1,
              "wind_speed": 1.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T17:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1021.3,
              "air_temperature": 16.7,
              "cloud_area_fraction": 96.1,
              "relative_humidity": 67.1,
              "wind_from_direction": 220.1,
              "wind_speed": 2.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1021.3,
              "air_temperature": 16.1,
              "cloud_area_fraction": 96.9,
              "relative_humidity": 68.5,
              "wind_from_direction": 217.9,
              "wind_speed": 2.7
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T19:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1021.2,
              "air_temperature": 15.3,
              "cloud_area_fraction": 96.9,
              "relative_humidity": 70.2,
              "wind_from_direction": 223.2,
              "wind_speed": 2.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T20:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1021.2,
              "air_temperature": 14.6,
              "cloud_area_fraction": 96.1,
              "relative_humidity": 72.9,
              "wind_from_direction": 224.2,
              "wind_speed": 2.8
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T21:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1021.1,
              "air_temperature": 14.0,
              "cloud_area_fraction": 95.3,
              "relative_humidity": 75.3,
              "wind_from_direction": 220.6,
              "wind_speed": 2.6
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T22:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.8,
              "air_temperature": 13.6,
              "cloud_area_fraction": 94.5,
              "relative_humidity": 76.6,
              "wind_from_direction": 224.6,
              "wind_speed": 2.8
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-05T23:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.6,
              "air_temperature": 13.3,
              "cloud_area_fraction": 85.9,
              "relative_humidity": 77.6,
              "wind_from_direction": 242.0,
              "wind_speed": 2.8
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.6,
              "air_temperature": 12.9,
              "cloud_area_fraction": 84.4,
              "relative_humidity": 79.9,
              "wind_from_direction": 243.1,
              "wind_speed": 2.6
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T01:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.4,
              "air_temperature": 12.5,
              "cloud_area_fraction": 47.7,
              "relative_humidity": 83.1,
              "wind_from_direction": 248.8,
              "wind_speed": 2.6
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T02:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.2,
              "air_temperature": 12.1,
              "cloud_area_fraction": 25.8,
              "relative_humidity": 87.1,
              "wind_from_direction": 254.1,
              "wind_speed": 2.5
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T03:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.0,
              "air_temperature": 11.8,
              "cloud_area_fraction": 14.8,
              "relative_humidity": 90.0,
              "wind_from_direction": 259.2,
              "wind_speed": 2.4
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T04:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.0,
              "air_temperature": 11.4,
              "cloud_area_fraction": 17.2,
              "relative_humidity": 92.1,
              "wind_from_direction": 257.5,
              "wind_speed": 2.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T05:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.3,
              "air_temperature": 11.2,
              "cloud_area_fraction": 31.2,
              "relative_humidity": 93.3,
              "wind_from_direction": 255.2,
              "wind_speed": 2.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.7,
              "air_temperature": 11.3,
              "cloud_area_fraction": 27.3,
              "relative_humidity": 94.3,
              "wind_from_direction": 252.6,
              "wind_speed": 2.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T07:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.8,
              "air_temperature": 12.6,
              "cloud_area_fraction": 55.5,
              "relative_humidity": 90.7,
              "wind_from_direction": 239.2,
              "wind_speed": 2.6
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.1
            }
          }
        }
      },
      {
        "time": "2026-10-06T08:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.9,
              "air_temperature": 14.3,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 84.9,
              "wind_from_direction": 252.8,
              "wind_speed": 2.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.1
            }
          }
        }
      },
      {
        "time": "2026-10-06T09:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.8,
              "air_temperature": 15.4,
              "cloud_area_fraction": 91.4,
              "relative_humidity": 81.1,
              "wind_from_direction": 246.2,
              "wind_speed": 2.1
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.1
            }
          }
        }
      },
      {
        "time": "2026-10-06T10:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1020.4,
              "air_temperature": 17.1,
              "cloud_area_fraction": 46.1,
              "relative_humidity": 73.6,
              "wind_from_direction": 255.8,
              "wind_speed": 2.5
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.1
            }
          }
        }
      },
      {
        "time": "2026-10-06T11:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1019.8,
              "air_temperature": 18.4,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 66.1,
              "wind_from_direction": 273.0,
              "wind_speed": 2.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1019.5,
              "air_temperature": 18.2,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 66.4,
              "wind_from_direction": 279.0,
              "wind_speed": 2.6
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T13:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1019.2,
              "air_temperature": 18.3,
              "cloud_area_fraction": 99.2,
              "relative_humidity": 66.3,
              "wind_from_direction": 276.9,
              "wind_speed": 2.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T14:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1019.0,
              "air_temperature": 18.4,
              "cloud_area_fraction": 85.9,
              "relative_humidity": 65.8,
              "wind_from_direction": 273.1,
              "wind_speed": 1.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T15:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.7,
              "air_temperature": 18.3,
              "cloud_area_fraction": 41.4,
              "relative_humidity": 66.5,
              "wind_from_direction": 265.8,
              "wind_speed": 1.5
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T16:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.5,
              "air_temperature": 17.4,
              "cloud_area_fraction": 18.7,
              "relative_humidity": 75.4,
              "wind_from_direction": 258.7,
              "wind_speed": 0.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T17:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.6,
              "air_temperature": 16.2,
              "cloud_area_fraction": 7.0,
              "relative_humidity": 79.8,
              "wind_from_direction": 271.0,
              "wind_speed": 1.1
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.6,
              "air_temperature": 15.6,
              "cloud_area_fraction": 4.7,
              "relative_humidity": 81.9,
              "wind_from_direction": 271.5,
              "wind_speed": 1.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T19:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.7,
              "air_temperature": 15.1,
              "cloud_area_fraction": 10.2,
              "relative_humidity": 83.0,
              "wind_from_direction": 221.6,
              "wind_speed": 0.8
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T20:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.7,
              "air_temperature": 14.5,
              "cloud_area_fraction": 7.0,
              "relative_humidity": 84.7,
              "wind_from_direction": 186.2,
              "wind_speed": 0.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T21:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.8,
              "air_temperature": 14.1,
              "cloud_area_fraction": 3.1,
              "relative_humidity": 85.6,
              "wind_from_direction": 151.2,
              "wind_speed": 0.4
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T22:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.6,
              "air_temperature": 13.3,
              "cloud_area_fraction": 2.3,
              "relative_humidity": 88.2,
              "wind_from_direction": 80.2,
              "wind_speed": 0.7
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-06T23:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.5,
              "air_temperature": 12.3,
              "cloud_area_fraction": 7.8,
              "relative_humidity": 91.7,
              "wind_from_direction": 120.2,
              "wind_speed": 1.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.4,
              "air_temperature": 11.7,
              "cloud_area_fraction": 7.0,
              "relative_humidity": 93.6,
              "wind_from_direction": 141.7,
              "wind_speed": 1.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T01:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1018.1,
              "air_temperature": 11.2,
              "cloud_area_fraction": 7.8,
              "relative_humidity": 94.9,
              "wind_from_direction": 122.2,
              "wind_speed": 1.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T02:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1017.7,
              "air_temperature": 11.0,
              "cloud_area_fraction": 8.6,
              "relative_humidity": 94.8,
              "wind_from_direction": 98.2,
              "wind_speed": 1.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T03:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1017.4,
              "air_temperature": 10.9,
              "cloud_area_fraction": 12.5,
              "relative_humidity": 94.3,
              "wind_from_direction": 104.6,
              "wind_speed": 1.7
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T04:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1017.1,
              "air_temperature": 10.8,
              "cloud_area_fraction": 96.1,
              "relative_humidity": 94.7,
              "wind_from_direction": 107.7,
              "wind_speed": 1.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T05:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1016.7,
              "air_temperature": 10.6,
              "cloud_area_fraction": 77.3,
              "relative_humidity": 95.7,
              "wind_from_direction": 116.6,
              "wind_speed": 2.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1016.7,
              "air_temperature": 10.8,
              "cloud_area_fraction": 95.3,
              "relative_humidity": 96.6,
              "wind_from_direction": 102.9,
              "wind_speed": 2.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T07:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1016.6,
              "air_temperature": 12.1,
              "cloud_area_fraction": 99.2,
              "relative_humidity": 93.0,
              "wind_from_direction": 90.6,
              "wind_speed": 2.5
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T08:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1016.4,
              "air_temperature": 13.3,
              "cloud_area_fraction": 97.7,
              "relative_humidity": 89.3,
              "wind_from_direction": 83.4,
              "wind_speed": 2.8
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T09:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1016.1,
              "air_temperature": 15.2,
              "cloud_area_fraction": 92.2,
              "relative_humidity": 81.4,
              "wind_from_direction": 95.0,
              "wind_speed": 2.6
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T10:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1015.6,
              "air_temperature": 17.0,
              "cloud_area_fraction": 93.7,
              "relative_humidity": 72.2,
              "wind_from_direction": 100.0,
              "wind_speed": 2.8
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T11:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1014.7,
              "air_temperature": 17.9,
              "cloud_area_fraction": 98.4,
              "relative_humidity": 67.6,
              "wind_from_direction": 106.8,
              "wind_speed": 3.4
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1013.9,
              "air_temperature": 17.8,
              "cloud_area_fraction": 86.7,
              "relative_humidity": 68.3,
              "wind_from_direction": 113.9,
              "wind_speed": 3.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {}
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T13:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1013.1,
              "air_temperature": 18.6,
              "cloud_area_fraction": 95.3,
              "relative_humidity": 64.4,
              "wind_from_direction": 118.1,
              "wind_speed": 3.3
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T14:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1012.5,
              "air_temperature": 18.3,
              "cloud_area_fraction": 94.5,
              "relative_humidity": 63.9,
              "wind_from_direction": 109.2,
              "wind_speed": 3.4
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T15:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1011.7,
              "air_temperature": 17.8,
              "cloud_area_fraction": 99.2,
              "relative_humidity": 66.3,
              "wind_from_direction": 110.7,
              "wind_speed": 3.4
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T16:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1011.3,
              "air_temperature": 16.9,
              "cloud_area_fraction": 11.7,
              "relative_humidity": 71.3,
              "wind_from_direction": 109.3,
              "wind_speed": 2.7
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T17:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1011.3,
              "air_temperature": 15.4,
              "cloud_area_fraction": 12.5,
              "relative_humidity": 79.8,
              "wind_from_direction": 111.6,
              "wind_speed": 2.5
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-07T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1011.0,
              "air_temperature": 14.3,
              "cloud_area_fraction": 0.0,
              "relative_humidity": 85.5,
              "wind_from_direction": 116.1,
              "wind_speed": 2.8
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "lightrainshowers_night"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-08T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1006.7,
              "air_temperature": 12.3,
              "cloud_area_fraction": 87.5,
              "relative_humidity": 87.2,
              "wind_from_direction": 148.4,
              "wind_speed": 2.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 1.3
            }
          }
        }
      },
      {
        "time": "2026-10-08T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1003.2,
              "air_temperature": 12.3,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 86.4,
              "wind_from_direction": 178.0,
              "wind_speed": 3.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 1.4
            }
          }
        }
      },
      {
        "time": "2026-10-08T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1004.1,
              "air_temperature": 15.7,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 76.9,
              "wind_from_direction": 286.2,
              "wind_speed": 4.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "lightrainshowers_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 2.1
            }
          }
        }
      },
      {
        "time": "2026-10-08T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1008.8,
              "air_temperature": 10.5,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 90.4,
              "wind_from_direction": 288.5,
              "wind_speed": 4.7
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-09T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1011.9,
              "air_temperature": 8.6,
              "cloud_area_fraction": 28.1,
              "relative_humidity": 85.2,
              "wind_from_direction": 273.5,
              "wind_speed": 4.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-09T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1014.0,
              "air_temperature": 7.5,
              "cloud_area_fraction": 10.9,
              "relative_humidity": 88.3,
              "wind_from_direction": 264.5,
              "wind_speed": 4.4
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "lightrainshowers_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_day"
            },
            "details": {
              "precipitation_amount": 0.1
            }
          }
        }
      },
      {
        "time": "2026-10-09T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1014.6,
              "air_temperature": 13.5,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 56.1,
              "wind_from_direction": 272.4,
              "wind_speed": 6.2
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "lightrain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "lightrain"
            },
            "details": {
              "precipitation_amount": 0.6
            }
          }
        }
      },
      {
        "time": "2026-10-09T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1014.7,
              "air_temperature": 9.8,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 77.2,
              "wind_from_direction": 248.5,
              "wind_speed": 5.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 2.8
            }
          }
        }
      },
      {
        "time": "2026-10-10T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1010.7,
              "air_temperature": 10.3,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 91.7,
              "wind_from_direction": 238.1,
              "wind_speed": 5.4
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 4.3
            }
          }
        }
      },
      {
        "time": "2026-10-10T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1008.9,
              "air_temperature": 11.3,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 93.1,
              "wind_from_direction": 227.0,
              "wind_speed": 5.6
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "heavyrain"
            },
            "details": {
              "precipitation_amount": 8.3
            }
          }
        }
      },
      {
        "time": "2026-10-10T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1008.8,
              "air_temperature": 12.5,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 95.4,
              "wind_from_direction": 258.2,
              "wind_speed": 4.4
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "lightrainshowers_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 2.2
            }
          }
        }
      },
      {
        "time": "2026-10-10T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1011.4,
              "air_temperature": 10.5,
              "cloud_area_fraction": 63.3,
              "relative_humidity": 92.2,
              "wind_from_direction": 262.7,
              "wind_speed": 4.8
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {
              "precipitation_amount": 0.1
            }
          }
        }
      },
      {
        "time": "2026-10-11T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1013.9,
              "air_temperature": 9.2,
              "cloud_area_fraction": 14.8,
              "relative_humidity": 88.9,
              "wind_from_direction": 266.5,
              "wind_speed": 4.8
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "fair_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-11T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1015.5,
              "air_temperature": 8.7,
              "cloud_area_fraction": 10.9,
              "relative_humidity": 86.4,
              "wind_from_direction": 251.1,
              "wind_speed": 4.1
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "clearsky_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-11T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1015.9,
              "air_temperature": 14.9,
              "cloud_area_fraction": 64.8,
              "relative_humidity": 60.7,
              "wind_from_direction": 258.3,
              "wind_speed": 5.5
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-11T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1015.1,
              "air_temperature": 11.4,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 74.9,
              "wind_from_direction": 216.6,
              "wind_speed": 1.9
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "lightrain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-12T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1013.1,
              "air_temperature": 10.6,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 77.1,
              "wind_from_direction": 201.7,
              "wind_speed": 3.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 2.1
            }
          }
        }
      },
      {
        "time": "2026-10-12T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1010.1,
              "air_temperature": 11.2,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 92.7,
              "wind_from_direction": 203.5,
              "wind_speed": 5.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "lightrain"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "rain"
            },
            "details": {
              "precipitation_amount": 3.0
            }
          }
        }
      },
      {
        "time": "2026-10-12T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1011.4,
              "air_temperature": 16.9,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 81.5,
              "wind_from_direction": 237.6,
              "wind_speed": 4.7
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.2
            }
          }
        }
      },
      {
        "time": "2026-10-12T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1013.9,
              "air_temperature": 16.3,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 83.7,
              "wind_from_direction": 250.9,
              "wind_speed": 4.5
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.1
            }
          }
        }
      },
      {
        "time": "2026-10-13T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1017.6,
              "air_temperature": 14.0,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 89.6,
              "wind_from_direction": 260.9,
              "wind_speed": 3.3
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-13T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1019.1,
              "air_temperature": 13.1,
              "cloud_area_fraction": 75.0,
              "relative_humidity": 93.4,
              "wind_from_direction": 229.5,
              "wind_speed": 3.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-13T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1017.4,
              "air_temperature": 19.7,
              "cloud_area_fraction": 97.7,
              "relative_humidity": 73.3,
              "wind_from_direction": 203.2,
              "wind_speed": 4.1
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-13T18:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1015.2,
              "air_temperature": 18.2,
              "cloud_area_fraction": 23.4,
              "relative_humidity": 70.8,
              "wind_from_direction": 232.4,
              "wind_speed": 4.7
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "partlycloudy_night"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "fair_night"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-14T00:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1016.8,
              "air_temperature": 17.1,
              "cloud_area_fraction": 100.0,
              "relative_humidity": 76.4,
              "wind_from_direction": 248.7,
              "wind_speed": 5.0
            }
          },
          "next_12_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {}
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.2
            }
          }
        }
      },
      {
        "time": "2026-10-14T06:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1019.4,
              "air_temperature": 16.2,
              "cloud_area_fraction": 90.6,
              "relative_humidity": 85.9,
              "wind_from_direction": 259.7,
              "wind_speed": 3.8
            }
          },
          "next_6_hours": {
            "summary": {
              "symbol_code": "cloudy"
            },
            "details": {
              "precipitation_amount": 0.0
            }
          }
        }
      },
      {
        "time": "2026-10-14T12:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_pressure_at_sea_level": 1022.9,
              "air_temperature": 18.8,
              "cloud_area_fraction": 71.9,
              "relative_humidity": 71.4,
              "wind_from_direction": 283.4,
              "wind_speed": 3.5
            }
          }
        }
      }
    ]
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
