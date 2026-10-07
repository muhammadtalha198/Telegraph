---
intent: WEATHER_CHECK
slug: wx-wttr
status: approved
captured_at: 2026-10-05T05:44:58Z
request_url: https://wttr.in/52.52,13.41?format=j1
content_type: text/plain
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 7 keyless. Open-Meteo model variants share a host - count as 1 source if you enforce one-publisher-per-miner.
answer_requirement: |
  Must satisfy catalog intent WEATHER_CHECK via upstream wttr.in (WorldWeatherOnline)
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:34Z
---

## Raw API output

```json
{
  "current_condition": [
    {
      "FeelsLikeC": "11",
      "FeelsLikeF": "52",
      "cloudcover": "100",
      "humidity": "84",
      "observation_time": "05:43 AM",
      "precipInches": "0.0",
      "precipMM": "0.0",
      "pressure": "1025",
      "pressureInches": "30",
      "temp_C": "12",
      "temp_F": "54",
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
      "winddir16Point": "SW",
      "winddirDegree": "230",
      "windspeedKmph": "7",
      "windspeedMiles": "4"
    }
  ],
  "nearest_area": [
    {
      "areaName": [
        {
          "value": "Berlin"
        }
      ],
      "country": [
        {
          "value": "Germany"
        }
      ],
      "latitude": "52.517",
      "longitude": "13.400",
      "population": "3426354",
      "region": [
        {
          "value": "Berlin"
        }
      ],
      "weatherUrl": [
        {
          "value": "https://www.worldweatheronline.com/v2/weather.aspx?q=52.517,13.4"
        }
      ]
    }
  ],
  "request": [
    {
      "query": "Lat 52.52 and Lon 13.41",
      "type": "LatLon"
    }
  ],
  "weather": [
    {
      "astronomy": [
        {
          "moon_illumination": "34",
          "moon_phase": "Waning Crescent",
          "moonrise": "12:09 AM",
          "moonset": "04:48 PM",
          "sunrise": "07:14 AM",
          "sunset": "06:34 PM"
        }
      ],
      "avgtempC": "16",
      "avgtempF": "62",
      "date": "2026-10-05",
      "hourly": [
        {
          "DewPointC": "10",
          "DewPointF": "50",
          "FeelsLikeC": "15",
          "FeelsLikeF": "59",
          "HeatIndexC": "14",
          "HeatIndexF": "57",
          "WindChillC": "15",
          "WindChillF": "59",
          "WindGustKmph": "4",
          "WindGustMiles": "2",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "3",
          "chanceofovercast": "0",
          "chanceofrain": "7",
          "chanceofremdry": "93",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "3",
          "diffRad": "0.0",
          "humidity": "75",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1027",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "14",
          "tempF": "57",
          "time": "0",
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
          "winddir16Point": "NNE",
          "winddirDegree": "26",
          "windspeedKmph": "3",
          "windspeedMiles": "2"
        },
        {
          "DewPointC": "10",
          "DewPointF": "49",
          "FeelsLikeC": "14",
          "FeelsLikeF": "57",
          "HeatIndexC": "13",
          "HeatIndexF": "56",
          "WindChillC": "14",
          "WindChillF": "57",
          "WindGustKmph": "4",
          "WindGustMiles": "2",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "2",
          "chanceofovercast": "6",
          "chanceofrain": "11",
          "chanceofremdry": "89",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "24",
          "diffRad": "0.0",
          "humidity": "79",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1026",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "13",
          "tempF": "56",
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
          "winddir16Point": "SSW",
          "winddirDegree": "195",
          "windspeedKmph": "4",
          "windspeedMiles": "2"
        },
        {
          "DewPointC": "10",
          "DewPointF": "49",
          "FeelsLikeC": "12",
          "FeelsLikeF": "54",
          "HeatIndexC": "12",
          "HeatIndexF": "54",
          "WindChillC": "12",
          "WindChillF": "54",
          "WindGustKmph": "13",
          "WindGustMiles": "8",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "1",
          "chanceofovercast": "98",
          "chanceofrain": "26",
          "chanceofremdry": "67",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "83",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1025",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "12",
          "tempF": "54",
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
          "winddir16Point": "WSW",
          "winddirDegree": "240",
          "windspeedKmph": "7",
          "windspeedMiles": "4"
        },
        {
          "DewPointC": "10",
          "DewPointF": "49",
          "FeelsLikeC": "14",
          "FeelsLikeF": "56",
          "HeatIndexC": "14",
          "HeatIndexF": "57",
          "WindChillC": "14",
          "WindChillF": "56",
          "WindGustKmph": "16",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "2",
          "chanceofovercast": "59",
          "chanceofrain": "14",
          "chanceofremdry": "86",
          "chanceofsnow": "0",
          "chanceofsunshine": "9",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "65",
          "diffRad": "83.3",
          "humidity": "75",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1025",
          "pressureInches": "30",
          "shortRad": "107.8",
          "tempC": "14",
          "tempF": "57",
          "time": "900",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "119",
          "weatherDesc": [
            {
              "value": "Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0003_white_cloud.png"
            }
          ],
          "winddir16Point": "WSW",
          "winddirDegree": "238",
          "windspeedKmph": "8",
          "windspeedMiles": "5"
        },
        {
          "DewPointC": "9",
          "DewPointF": "48",
          "FeelsLikeC": "19",
          "FeelsLikeF": "66",
          "HeatIndexC": "19",
          "HeatIndexF": "66",
          "WindChillC": "19",
          "WindChillF": "66",
          "WindGustKmph": "19",
          "WindGustMiles": "12",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "6",
          "chanceofovercast": "1",
          "chanceofrain": "2",
          "chanceofremdry": "98",
          "chanceofsnow": "0",
          "chanceofsunshine": "96",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "5",
          "diffRad": "118.5",
          "humidity": "53",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1024",
          "pressureInches": "30",
          "shortRad": "474.9",
          "tempC": "19",
          "tempF": "66",
          "time": "1200",
          "uvIndex": "2",
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
          "winddir16Point": "SW",
          "winddirDegree": "231",
          "windspeedKmph": "13",
          "windspeedMiles": "8"
        },
        {
          "DewPointC": "7",
          "DewPointF": "44",
          "FeelsLikeC": "22",
          "FeelsLikeF": "71",
          "HeatIndexC": "24",
          "HeatIndexF": "75",
          "WindChillC": "22",
          "WindChillF": "71",
          "WindGustKmph": "20",
          "WindGustMiles": "12",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "10",
          "chanceofovercast": "98",
          "chanceofrain": "10",
          "chanceofremdry": "81",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "98",
          "diffRad": "151.7",
          "humidity": "38",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1022",
          "pressureInches": "30",
          "shortRad": "425.8",
          "tempC": "22",
          "tempF": "71",
          "time": "1500",
          "uvIndex": "2",
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
          "winddir16Point": "WSW",
          "winddirDegree": "250",
          "windspeedKmph": "14",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "7",
          "DewPointF": "45",
          "FeelsLikeC": "20",
          "FeelsLikeF": "68",
          "HeatIndexC": "20",
          "HeatIndexF": "68",
          "WindChillC": "20",
          "WindChillF": "68",
          "WindGustKmph": "21",
          "WindGustMiles": "13",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "7",
          "chanceofovercast": "98",
          "chanceofrain": "10",
          "chanceofremdry": "81",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "68.5",
          "humidity": "43",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "79.5",
          "tempC": "20",
          "tempF": "68",
          "time": "1800",
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
          "winddir16Point": "WSW",
          "winddirDegree": "249",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "7",
          "DewPointF": "45",
          "FeelsLikeC": "17",
          "FeelsLikeF": "63",
          "HeatIndexC": "17",
          "HeatIndexF": "63",
          "WindChillC": "17",
          "WindChillF": "63",
          "WindGustKmph": "21",
          "WindGustMiles": "13",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "4",
          "chanceofovercast": "98",
          "chanceofrain": "12",
          "chanceofremdry": "79",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "99",
          "diffRad": "0.0",
          "humidity": "53",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "17",
          "tempF": "63",
          "time": "2100",
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
          "winddir16Point": "WSW",
          "winddirDegree": "257",
          "windspeedKmph": "9",
          "windspeedMiles": "6"
        }
      ],
      "maxtempC": "22",
      "maxtempF": "71",
      "mintempC": "12",
      "mintempF": "54",
      "sunHour": "5.0",
      "totalSnow_cm": "0.0",
      "uvIndex": "3"
    },
    {
      "astronomy": [
        {
          "moon_illumination": "24",
          "moon_phase": "Waning Crescent",
          "moonrise": "01:39 AM",
          "moonset": "05:05 PM",
          "sunrise": "07:16 AM",
          "sunset": "06:32 PM"
        }
      ],
      "avgtempC": "17",
      "avgtempF": "62",
      "date": "2026-10-06",
      "hourly": [
        {
          "DewPointC": "8",
          "DewPointF": "47",
          "FeelsLikeC": "15",
          "FeelsLikeF": "60",
          "HeatIndexC": "15",
          "HeatIndexF": "60",
          "WindChillC": "15",
          "WindChillF": "60",
          "WindGustKmph": "21",
          "WindGustMiles": "13",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "3",
          "chanceofovercast": "74",
          "chanceofrain": "11",
          "chanceofremdry": "90",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "72",
          "diffRad": "0.0",
          "humidity": "62",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "15",
          "tempF": "60",
          "time": "0",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "119",
          "weatherDesc": [
            {
              "value": "Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "WSW",
          "winddirDegree": "247",
          "windspeedKmph": "8",
          "windspeedMiles": "5"
        },
        {
          "DewPointC": "9",
          "DewPointF": "48",
          "FeelsLikeC": "14",
          "FeelsLikeF": "56",
          "HeatIndexC": "14",
          "HeatIndexF": "57",
          "WindChillC": "14",
          "WindChillF": "56",
          "WindGustKmph": "25",
          "WindGustMiles": "15",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "1",
          "chanceofovercast": "1",
          "chanceofrain": "6",
          "chanceofremdry": "94",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "5",
          "diffRad": "0.0",
          "humidity": "71",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1020",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "14",
          "tempF": "57",
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
          "winddir16Point": "WSW",
          "winddirDegree": "249",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "9",
          "DewPointF": "49",
          "FeelsLikeC": "12",
          "FeelsLikeF": "54",
          "HeatIndexC": "13",
          "HeatIndexF": "56",
          "WindChillC": "12",
          "WindChillF": "54",
          "WindGustKmph": "25",
          "WindGustMiles": "16",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "1",
          "chanceofovercast": "66",
          "chanceofrain": "16",
          "chanceofremdry": "84",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "68",
          "diffRad": "0.0",
          "humidity": "77",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1020",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "13",
          "tempF": "56",
          "time": "600",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "119",
          "weatherDesc": [
            {
              "value": "Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "WSW",
          "winddirDegree": "256",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "10",
          "DewPointF": "50",
          "FeelsLikeC": "14",
          "FeelsLikeF": "57",
          "HeatIndexC": "14",
          "HeatIndexF": "58",
          "WindChillC": "14",
          "WindChillF": "57",
          "WindGustKmph": "22",
          "WindGustMiles": "13",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "2",
          "chanceofovercast": "53",
          "chanceofrain": "14",
          "chanceofremdry": "86",
          "chanceofsnow": "0",
          "chanceofsunshine": "11",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "62",
          "diffRad": "79.5",
          "humidity": "75",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "115.7",
          "tempC": "14",
          "tempF": "58",
          "time": "900",
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
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png"
            }
          ],
          "winddir16Point": "W",
          "winddirDegree": "266",
          "windspeedKmph": "11",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "11",
          "DewPointF": "52",
          "FeelsLikeC": "19",
          "FeelsLikeF": "67",
          "HeatIndexC": "19",
          "HeatIndexF": "67",
          "WindChillC": "19",
          "WindChillF": "67",
          "WindGustKmph": "15",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "8",
          "chanceofovercast": "4",
          "chanceofrain": "4",
          "chanceofremdry": "96",
          "chanceofsnow": "0",
          "chanceofsunshine": "81",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "19",
          "diffRad": "130.1",
          "humidity": "60",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1020",
          "pressureInches": "30",
          "shortRad": "455.8",
          "tempC": "19",
          "tempF": "67",
          "time": "1200",
          "uvIndex": "2",
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
          "winddir16Point": "W",
          "winddirDegree": "262",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "10",
          "DewPointF": "50",
          "FeelsLikeC": "21",
          "FeelsLikeF": "70",
          "HeatIndexC": "24",
          "HeatIndexF": "76",
          "WindChillC": "21",
          "WindChillF": "70",
          "WindGustKmph": "14",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "15",
          "chanceofovercast": "98",
          "chanceofrain": "12",
          "chanceofremdry": "80",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "176.6",
          "humidity": "49",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1019",
          "pressureInches": "30",
          "shortRad": "183.6",
          "tempC": "21",
          "tempF": "70",
          "time": "1500",
          "uvIndex": "1",
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
          "winddir16Point": "WNW",
          "winddirDegree": "294",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "11",
          "DewPointF": "51",
          "FeelsLikeC": "19",
          "FeelsLikeF": "67",
          "HeatIndexC": "19",
          "HeatIndexF": "67",
          "WindChillC": "19",
          "WindChillF": "67",
          "WindGustKmph": "12",
          "WindGustMiles": "7",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "9",
          "chanceofovercast": "98",
          "chanceofrain": "14",
          "chanceofremdry": "78",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "32.7",
          "humidity": "57",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1019",
          "pressureInches": "30",
          "shortRad": "33.2",
          "tempC": "19",
          "tempF": "67",
          "time": "1800",
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
          "winddir16Point": "NW",
          "winddirDegree": "304",
          "windspeedKmph": "7",
          "windspeedMiles": "4"
        },
        {
          "DewPointC": "11",
          "DewPointF": "52",
          "FeelsLikeC": "18",
          "FeelsLikeF": "64",
          "HeatIndexC": "18",
          "HeatIndexF": "64",
          "WindChillC": "18",
          "WindChillF": "64",
          "WindGustKmph": "11",
          "WindGustMiles": "7",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "7",
          "chanceofovercast": "98",
          "chanceofrain": "16",
          "chanceofremdry": "76",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "65",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1019",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "18",
          "tempF": "64",
          "time": "2100",
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
          "winddir16Point": "NNW",
          "winddirDegree": "334",
          "windspeedKmph": "6",
          "windspeedMiles": "4"
        }
      ],
      "maxtempC": "21",
      "maxtempF": "70",
      "mintempC": "13",
      "mintempF": "55",
      "sunHour": "7.0",
      "totalSnow_cm": "0.0",
      "uvIndex": "2"
    },
    {
      "astronomy": [
        {
          "moon_illumination": "15",
          "moon_phase": "Waning Crescent",
          "moonrise": "03:05 AM",
          "moonset": "05:18 PM",
          "sunrise": "07:18 AM",
          "sunset": "06:30 PM"
        }
      ],
      "avgtempC": "18",
      "avgtempF": "65",
      "date": "2026-10-07",
      "hourly": [
        {
          "DewPointC": "12",
          "DewPointF": "53",
          "FeelsLikeC": "17",
          "FeelsLikeF": "63",
          "HeatIndexC": "17",
          "HeatIndexF": "63",
          "WindChillC": "17",
          "WindChillF": "63",
          "WindGustKmph": "3",
          "WindGustMiles": "2",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "7",
          "chanceofovercast": "98",
          "chanceofrain": "18",
          "chanceofremdry": "74",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "98",
          "diffRad": "0.0",
          "humidity": "70",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1019",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "17",
          "tempF": "63",
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
          "winddir16Point": "NNE",
          "winddirDegree": "17",
          "windspeedKmph": "3",
          "windspeedMiles": "2"
        },
        {
          "DewPointC": "12",
          "DewPointF": "53",
          "FeelsLikeC": "17",
          "FeelsLikeF": "63",
          "HeatIndexC": "17",
          "HeatIndexF": "63",
          "WindChillC": "17",
          "WindChillF": "63",
          "WindGustKmph": "5",
          "WindGustMiles": "3",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "7",
          "chanceofovercast": "98",
          "chanceofrain": "19",
          "chanceofremdry": "73",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "71",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1018",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "17",
          "tempF": "63",
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
          "winddir16Point": "E",
          "winddirDegree": "87",
          "windspeedKmph": "4",
          "windspeedMiles": "3"
        },
        {
          "DewPointC": "11",
          "DewPointF": "51",
          "FeelsLikeC": "16",
          "FeelsLikeF": "61",
          "HeatIndexC": "16",
          "HeatIndexF": "61",
          "WindChillC": "16",
          "WindChillF": "61",
          "WindGustKmph": "11",
          "WindGustMiles": "7",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "5",
          "chanceofovercast": "37",
          "chanceofrain": "11",
          "chanceofremdry": "90",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "55",
          "diffRad": "0.0",
          "humidity": "70",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1018",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "16",
          "tempF": "61",
          "time": "600",
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
          "winddir16Point": "SSE",
          "winddirDegree": "148",
          "windspeedKmph": "6",
          "windspeedMiles": "4"
        },
        {
          "DewPointC": "10",
          "DewPointF": "50",
          "FeelsLikeC": "16",
          "FeelsLikeF": "61",
          "HeatIndexC": "16",
          "HeatIndexF": "61",
          "WindChillC": "16",
          "WindChillF": "61",
          "WindGustKmph": "10",
          "WindGustMiles": "7",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "4",
          "chanceofovercast": "2",
          "chanceofrain": "6",
          "chanceofremdry": "95",
          "chanceofsnow": "0",
          "chanceofsunshine": "92",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "11",
          "diffRad": "79.0",
          "humidity": "67",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1017",
          "pressureInches": "30",
          "shortRad": "102.7",
          "tempC": "16",
          "tempF": "61",
          "time": "900",
          "uvIndex": "0",
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
          "winddir16Point": "SE",
          "winddirDegree": "139",
          "windspeedKmph": "7",
          "windspeedMiles": "4"
        },
        {
          "DewPointC": "9",
          "DewPointF": "49",
          "FeelsLikeC": "20",
          "FeelsLikeF": "68",
          "HeatIndexC": "20",
          "HeatIndexF": "68",
          "WindChillC": "20",
          "WindChillF": "68",
          "WindGustKmph": "18",
          "WindGustMiles": "11",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "8",
          "chanceofovercast": "64",
          "chanceofrain": "7",
          "chanceofremdry": "93",
          "chanceofsnow": "0",
          "chanceofsunshine": "7",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "67",
          "diffRad": "227.2",
          "humidity": "51",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1016",
          "pressureInches": "30",
          "shortRad": "282.1",
          "tempC": "20",
          "tempF": "68",
          "time": "1200",
          "uvIndex": "2",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "119",
          "weatherDesc": [
            {
              "value": "Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0003_white_cloud.png"
            }
          ],
          "winddir16Point": "ESE",
          "winddirDegree": "118",
          "windspeedKmph": "12",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "8",
          "DewPointF": "47",
          "FeelsLikeC": "24",
          "FeelsLikeF": "75",
          "HeatIndexC": "24",
          "HeatIndexF": "75",
          "WindChillC": "22",
          "WindChillF": "72",
          "WindGustKmph": "15",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "17",
          "chanceofovercast": "69",
          "chanceofrain": "6",
          "chanceofremdry": "94",
          "chanceofsnow": "0",
          "chanceofsunshine": "6",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "69",
          "diffRad": "121.8",
          "humidity": "41",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1014",
          "pressureInches": "30",
          "shortRad": "443.8",
          "tempC": "22",
          "tempF": "72",
          "time": "1500",
          "uvIndex": "2",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "119",
          "weatherDesc": [
            {
              "value": "Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0003_white_cloud.png"
            }
          ],
          "winddir16Point": "ESE",
          "winddirDegree": "118",
          "windspeedKmph": "13",
          "windspeedMiles": "8"
        },
        {
          "DewPointC": "9",
          "DewPointF": "47",
          "FeelsLikeC": "20",
          "FeelsLikeF": "69",
          "HeatIndexC": "20",
          "HeatIndexF": "69",
          "WindChillC": "20",
          "WindChillF": "69",
          "WindGustKmph": "18",
          "WindGustMiles": "11",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "9",
          "chanceofovercast": "1",
          "chanceofrain": "2",
          "chanceofremdry": "99",
          "chanceofsnow": "0",
          "chanceofsunshine": "96",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "5",
          "diffRad": "63.9",
          "humidity": "47",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1012",
          "pressureInches": "30",
          "shortRad": "91.6",
          "tempC": "20",
          "tempF": "69",
          "time": "1800",
          "uvIndex": "0",
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
          "winddir16Point": "ESE",
          "winddirDegree": "115",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "8",
          "DewPointF": "47",
          "FeelsLikeC": "17",
          "FeelsLikeF": "62",
          "HeatIndexC": "17",
          "HeatIndexF": "62",
          "WindChillC": "17",
          "WindChillF": "62",
          "WindGustKmph": "22",
          "WindGustMiles": "14",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "4",
          "chanceofovercast": "94",
          "chanceofrain": "12",
          "chanceofremdry": "79",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "1",
          "cloudcover": "90",
          "diffRad": "0.0",
          "humidity": "56",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1011",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "17",
          "tempF": "62",
          "time": "2100",
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
          "winddirDegree": "133",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        }
      ],
      "maxtempC": "22",
      "maxtempF": "72",
      "mintempC": "15",
      "mintempF": "58",
      "sunHour": "9.0",
      "totalSnow_cm": "0.0",
      "uvIndex": "2"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
