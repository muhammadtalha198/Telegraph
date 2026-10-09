---
intent: WEATHER_CURRENT
slug: wx-wttr
status: pending_review
captured_at: 2026-10-05T09:33:44Z
request_url: https://wttr.in/1.3521,103.8198?format=j1
content_type: application/json
inputs: |
  {"lat": "1.3521", "lon": "103.8198"}
intent_description: |
  Provides real-time ambient temperature, humidity, precipitation rate, and wind vectors by coordinates.
answer_requirement: |
  Must return current temperature (and ideally humidity/wind/precipitation) for the coordinates asked.
capture_note: |
  golden-test PASS: wttr.in (WorldWeatherOnline)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```text
{
  "current_condition": [
    {
      "FeelsLikeC": "34",
      "FeelsLikeF": "93",
      "cloudcover": "33",
      "humidity": "70",
      "observation_time": "09:30 AM",
      "precipInches": "0.0",
      "precipMM": "0.0",
      "pressure": "1009",
      "pressureInches": "30",
      "temp_C": "29",
      "temp_F": "85",
      "uvIndex": "2",
      "visibility": "10",
      "visibilityMiles": "6",
      "weatherCode": "149",
      "weatherDesc": [
        {
          "value": "Smoky haze"
        }
      ],
      "weatherIconUrl": [
        {
          "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png"
        }
      ],
      "winddir16Point": "S",
      "winddirDegree": "180",
      "windspeedKmph": "21",
      "windspeedMiles": "13"
    }
  ],
  "nearest_area": [
    {
      "areaName": [
        {
          "value": "Windsor Park Estate"
        }
      ],
      "country": [
        {
          "value": "Singapore"
        }
      ],
      "latitude": "1.357",
      "longitude": "103.825",
      "population": "0",
      "region": [
        {
          "value": ""
        }
      ],
      "weatherUrl": [
        {
          "value": "https://www.worldweatheronline.com/v2/weather.aspx?q=1.357,103.825"
        }
      ]
    }
  ],
  "request": [
    {
      "query": "Lat 1.35 and Lon 103.82",
      "type": "LatLon"
    }
  ],
  "weather": [
    {
      "astronomy": [
        {
          "moon_illumination": "34",
          "moon_phase": "Waning Crescent",
          "moonrise": "02:08 AM",
          "moonset": "02:39 PM",
          "sunrise": "06:50 AM",
          "sunset": "06:56 PM"
        }
      ],
      "avgtempC": "29",
      "avgtempF": "84",
      "date": "2026-10-05",
      "hourly": [
        {
          "DewPointC": "24",
          "DewPointF": "74",
          "FeelsLikeC": "33",
          "FeelsLikeF": "91",
          "HeatIndexC": "33",
          "HeatIndexF": "91",
          "WindChillC": "29",
          "WindChillF": "84",
          "WindGustKmph": "27",
          "WindGustMiles": "17",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "97",
          "chanceofovercast": "98",
          "chanceofrain": "19",
          "chanceofremdry": "73",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "73",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1013",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "29",
          "tempF": "84",
          "time": "0",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "SE",
          "winddirDegree": "128",
          "windspeedKmph": "9",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "23",
          "DewPointF": "74",
          "FeelsLikeC": "32",
          "FeelsLikeF": "89",
          "HeatIndexC": "32",
          "HeatIndexF": "89",
          "WindChillC": "28",
          "WindChillF": "83",
          "WindGustKmph": "15",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "96",
          "chanceofovercast": "98",
          "chanceofrain": "20",
          "chanceofremdry": "72",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "75",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1011",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "28",
          "tempF": "83",
          "time": "300",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "ESE",
          "winddirDegree": "123",
          "windspeedKmph": "5",
          "windspeedMiles": "3"
        },
        {
          "DewPointC": "23",
          "DewPointF": "74",
          "FeelsLikeC": "31",
          "FeelsLikeF": "88",
          "HeatIndexC": "31",
          "HeatIndexF": "88",
          "WindChillC": "28",
          "WindChillF": "82",
          "WindGustKmph": "15",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "95",
          "chanceofovercast": "98",
          "chanceofrain": "21",
          "chanceofremdry": "71",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "77",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1011",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "28",
          "tempF": "82",
          "time": "600",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "SE",
          "winddirDegree": "139",
          "windspeedKmph": "14",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "23",
          "DewPointF": "73",
          "FeelsLikeC": "32",
          "FeelsLikeF": "90",
          "HeatIndexC": "32",
          "HeatIndexF": "90",
          "WindChillC": "29",
          "WindChillF": "83",
          "WindGustKmph": "17",
          "WindGustMiles": "11",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "96",
          "chanceofovercast": "24",
          "chanceofrain": "10",
          "chanceofremdry": "90",
          "chanceofsnow": "0",
          "chanceofsunshine": "28",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "47",
          "diffRad": "131.8",
          "humidity": "72",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1013",
          "pressureInches": "30",
          "shortRad": "349.9",
          "tempC": "29",
          "tempF": "83",
          "time": "900",
          "uvIndex": "2",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "116",
          "weatherDesc": [
            {
              "value": "Partly Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png"
            }
          ],
          "winddir16Point": "SSE",
          "winddirDegree": "157",
          "windspeedKmph": "15",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "23",
          "DewPointF": "74",
          "FeelsLikeC": "33",
          "FeelsLikeF": "92",
          "HeatIndexC": "33",
          "HeatIndexF": "92",
          "WindChillC": "29",
          "WindChillF": "85",
          "WindGustKmph": "16",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "97",
          "chanceofovercast": "1",
          "chanceofrain": "6",
          "chanceofremdry": "95",
          "chanceofsnow": "0",
          "chanceofsunshine": "96",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "6",
          "diffRad": "183.1",
          "humidity": "70",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1013",
          "pressureInches": "30",
          "shortRad": "936.6",
          "tempC": "29",
          "tempF": "85",
          "time": "1200",
          "uvIndex": "10",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "SSW",
          "winddirDegree": "193",
          "windspeedKmph": "16",
          "windspeedMiles": "10"
        },
        {
          "DewPointC": "24",
          "DewPointF": "75",
          "FeelsLikeC": "34",
          "FeelsLikeF": "93",
          "HeatIndexC": "34",
          "HeatIndexF": "93",
          "WindChillC": "29",
          "WindChillF": "85",
          "WindGustKmph": "41",
          "WindGustMiles": "26",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "98",
          "chanceofovercast": "92",
          "chanceofrain": "23",
          "chanceofremdry": "69",
          "chanceofsnow": "0",
          "chanceofsunshine": "2",
          "chanceofthunder": "0",
          "chanceofwindy": "3",
          "cloudcover": "88",
          "diffRad": "179.2",
          "humidity": "72",
          "precipInches": "0.0",
          "precipMM": "0.1",
          "pressure": "1010",
          "pressureInches": "30",
          "shortRad": "912.2",
          "tempC": "29",
          "tempF": "85",
          "time": "1500",
          "uvIndex": "8",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "176",
          "weatherDesc": [
            {
              "value": "Patchy rain nearby"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0009_light_rain_showers.png"
            }
          ],
          "winddir16Point": "S",
          "winddirDegree": "188",
          "windspeedKmph": "23",
          "windspeedMiles": "15"
        },
        {
          "DewPointC": "24",
          "DewPointF": "74",
          "FeelsLikeC": "34",
          "FeelsLikeF": "93",
          "HeatIndexC": "34",
          "HeatIndexF": "93",
          "WindChillC": "29",
          "WindChillF": "85",
          "WindGustKmph": "19",
          "WindGustMiles": "12",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "98",
          "chanceofovercast": "2",
          "chanceofrain": "6",
          "chanceofremdry": "94",
          "chanceofsnow": "0",
          "chanceofsunshine": "91",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "12",
          "diffRad": "148.5",
          "humidity": "71",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1009",
          "pressureInches": "30",
          "shortRad": "259.3",
          "tempC": "29",
          "tempF": "85",
          "time": "1800",
          "uvIndex": "1",
          "visibility": "8",
          "visibilityMiles": "5",
          "weatherCode": "149",
          "weatherDesc": [
            {
              "value": "Smoky haze"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png"
            }
          ],
          "winddir16Point": "S",
          "winddirDegree": "169",
          "windspeedKmph": "18",
          "windspeedMiles": "11"
        },
        {
          "DewPointC": "24",
          "DewPointF": "75",
          "FeelsLikeC": "33",
          "FeelsLikeF": "92",
          "HeatIndexC": "33",
          "HeatIndexF": "92",
          "WindChillC": "29",
          "WindChillF": "84",
          "WindGustKmph": "18",
          "WindGustMiles": "11",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "97",
          "chanceofovercast": "35",
          "chanceofrain": "12",
          "chanceofremdry": "88",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "53",
          "diffRad": "0.0",
          "humidity": "75",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1012",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "29",
          "tempF": "84",
          "time": "2100",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "116",
          "weatherDesc": [
            {
              "value": "Partly Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "ESE",
          "winddirDegree": "119",
          "windspeedKmph": "17",
          "windspeedMiles": "11"
        }
      ],
      "maxtempC": "29",
      "maxtempF": "85",
      "mintempC": "28",
      "mintempF": "82",
      "sunHour": "8.0",
      "totalSnow_cm": "0.0",
      "uvIndex": "11"
    },
    {
      "astronomy": [
        {
          "moon_illumination": "24",
          "moon_phase": "Waning Crescent",
          "moonrise": "03:04 AM",
          "moonset": "03:32 PM",
          "sunrise": "06:50 AM",
          "sunset": "06:56 PM"
        }
      ],
      "avgtempC": "29",
      "avgtempF": "83",
      "date": "2026-10-06",
      "hourly": [
        {
          "DewPointC": "24",
          "DewPointF": "75",
          "FeelsLikeC": "32",
          "FeelsLikeF": "90",
          "HeatIndexC": "32",
          "HeatIndexF": "90",
          "WindChillC": "28",
          "WindChillF": "83",
          "WindGustKmph": "16",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "96",
          "chanceofovercast": "98",
          "chanceofrain": "22",
          "chanceofremdry": "70",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "78",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1013",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "28",
          "tempF": "83",
          "time": "0",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "ESE",
          "winddirDegree": "106",
          "windspeedKmph": "15",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "24",
          "DewPointF": "75",
          "FeelsLikeC": "32",
          "FeelsLikeF": "89",
          "HeatIndexC": "32",
          "HeatIndexF": "89",
          "WindChillC": "28",
          "WindChillF": "82",
          "WindGustKmph": "12",
          "WindGustMiles": "8",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "95",
          "chanceofovercast": "1",
          "chanceofrain": "9",
          "chanceofremdry": "91",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "6",
          "diffRad": "0.0",
          "humidity": "79",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1011",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "28",
          "tempF": "82",
          "time": "300",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "ESE",
          "winddirDegree": "116",
          "windspeedKmph": "11",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "23",
          "DewPointF": "74",
          "FeelsLikeC": "31",
          "FeelsLikeF": "88",
          "HeatIndexC": "31",
          "HeatIndexF": "88",
          "WindChillC": "28",
          "WindChillF": "82",
          "WindGustKmph": "14",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "95",
          "chanceofovercast": "12",
          "chanceofrain": "11",
          "chanceofremdry": "89",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "37",
          "diffRad": "0.0",
          "humidity": "78",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1012",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "28",
          "tempF": "82",
          "time": "600",
          "uvIndex": "0",
          "visibility": "9",
          "visibilityMiles": "5",
          "weatherCode": "149",
          "weatherDesc": [
            {
              "value": "Smoky haze"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png"
            }
          ],
          "winddir16Point": "SE",
          "winddirDegree": "131",
          "windspeedKmph": "12",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "23",
          "DewPointF": "74",
          "FeelsLikeC": "32",
          "FeelsLikeF": "89",
          "HeatIndexC": "32",
          "HeatIndexF": "89",
          "WindChillC": "28",
          "WindChillF": "83",
          "WindGustKmph": "16",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "96",
          "chanceofovercast": "91",
          "chanceofrain": "17",
          "chanceofremdry": "75",
          "chanceofsnow": "0",
          "chanceofsunshine": "2",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "87",
          "diffRad": "127.0",
          "humidity": "74",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1014",
          "pressureInches": "30",
          "shortRad": "356.1",
          "tempC": "28",
          "tempF": "83",
          "time": "900",
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
