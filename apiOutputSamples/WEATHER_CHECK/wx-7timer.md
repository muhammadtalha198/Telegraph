---
intent: WEATHER_CHECK
slug: wx-7timer
status: approved
captured_at: 2026-10-05T05:44:57Z
request_url: http://www.7timer.info/bin/api.pl?lon=13.41&lat=52.52&product=civil&output=json
content_type: text/plain
inputs: |
  (none / baked into URL)
intent_description: |
  PACK READY - meets 10 candidates; 7 keyless. Open-Meteo model variants share a host - count as 1 source if you enforce one-publisher-per-miner.
answer_requirement: |
  Must satisfy catalog intent WEATHER_CHECK via upstream 7Timer
capture_note: |
  (none)
reviewer_note: "pack V2 smoke pass + pipeline approve (distinct publisher per intent)"
reviewed_at: 2026-10-05T05:45:34Z
---

## Raw API output

```json
{
  "product": "civil",
  "init": "2026100500",
  "dataseries": [
    {
      "timepoint": 3,
      "cloudcover": 6,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "80%",
      "wind10m": {
        "direction": "SW",
        "speed": 2
      },
      "weather": "mcloudynight"
    },
    {
      "timepoint": 6,
      "cloudcover": 8,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "83%",
      "wind10m": {
        "direction": "SW",
        "speed": 2
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 9,
      "cloudcover": 8,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 16,
      "rh2m": "60%",
      "wind10m": {
        "direction": "SW",
        "speed": 3
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 12,
      "cloudcover": 7,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 21,
      "rh2m": "41%",
      "wind10m": {
        "direction": "SW",
        "speed": 3
      },
      "weather": "mcloudyday"
    },
    {
      "timepoint": 15,
      "cloudcover": 9,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 21,
      "rh2m": "35%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 18,
      "cloudcover": 9,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 15,
      "rh2m": "50%",
      "wind10m": {
        "direction": "W",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 21,
      "cloudcover": 9,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 13,
      "rh2m": "58%",
      "wind10m": {
        "direction": "W",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 24,
      "cloudcover": 8,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 11,
      "rh2m": "67%",
      "wind10m": {
        "direction": "SW",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 27,
      "cloudcover": 5,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "78%",
      "wind10m": {
        "direction": "W",
        "speed": 2
      },
      "weather": "pcloudynight"
    },
    {
      "timepoint": 30,
      "cloudcover": 7,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 11,
      "rh2m": "75%",
      "wind10m": {
        "direction": "W",
        "speed": 2
      },
      "weather": "mcloudyday"
    },
    {
      "timepoint": 33,
      "cloudcover": 7,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 16,
      "rh2m": "69%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "mcloudyday"
    },
    {
      "timepoint": 36,
      "cloudcover": 8,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 21,
      "rh2m": "52%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 39,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 17,
      "rh2m": "60%",
      "wind10m": {
        "direction": "NW",
        "speed": 2
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 42,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 15,
      "rh2m": "69%",
      "wind10m": {
        "direction": "NW",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 45,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 15,
      "rh2m": "69%",
      "wind10m": {
        "direction": "NW",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 48,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 14,
      "rh2m": "70%",
      "wind10m": {
        "direction": "E",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 51,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 15,
      "rh2m": "65%",
      "wind10m": {
        "direction": "SE",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 54,
      "cloudcover": 9,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 15,
      "rh2m": "69%",
      "wind10m": {
        "direction": "SE",
        "speed": 2
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 57,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 18,
      "rh2m": "54%",
      "wind10m": {
        "direction": "SE",
        "speed": 2
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 60,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 21,
      "rh2m": "46%",
      "wind10m": {
        "direction": "SE",
        "speed": 3
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 63,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 20,
      "rh2m": "45%",
      "wind10m": {
        "direction": "SE",
        "speed": 2
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 66,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 15,
      "rh2m": "58%",
      "wind10m": {
        "direction": "SE",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 69,
      "cloudcover": 4,
      "lifted_index": 6,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 13,
      "rh2m": "62%",
      "wind10m": {
        "direction": "SE",
        "speed": 2
      },
      "weather": "pcloudynight"
    },
    {
      "timepoint": 72,
      "cloudcover": 4,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 12,
      "rh2m": "61%",
      "wind10m": {
        "direction": "SE",
        "speed": 2
      },
      "weather": "pcloudynight"
    },
    {
      "timepoint": 75,
      "cloudcover": 9,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 11,
      "rh2m": "52%",
      "wind10m": {
        "direction": "S",
        "speed": 2
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 78,
      "cloudcover": 9,
      "lifted_index": 10,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 13,
      "rh2m": "62%",
      "wind10m": {
        "direction": "S",
        "speed": 2
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 81,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 2,
      "temp2m": 13,
      "rh2m": "90%",
      "wind10m": {
        "direction": "SW",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 84,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "rain",
      "prec_amount": 1,
      "temp2m": 13,
      "rh2m": "85%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 87,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "81%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 90,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 9,
      "rh2m": "78%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 93,
      "cloudcover": 6,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "78%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "oshowernight"
    },
    {
      "timepoint": 96,
      "cloudcover": 6,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 7,
      "rh2m": "76%",
      "wind10m": {
        "direction": "W",
        "speed": 4
      },
      "weather": "oshowernight"
    },
    {
      "timepoint": 99,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 7,
      "rh2m": "79%",
      "wind10m": {
        "direction": "W",
        "speed": 4
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 102,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 7,
      "rh2m": "74%",
      "wind10m": {
        "direction": "W",
        "speed": 4
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 105,
      "cloudcover": 5,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 11,
      "rh2m": "53%",
      "wind10m": {
        "direction": "W",
        "speed": 4
      },
      "weather": "pcloudyday"
    },
    {
      "timepoint": 108,
      "cloudcover": 5,
      "lifted_index": 15,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 12,
      "rh2m": "55%",
      "wind10m": {
        "direction": "W",
        "speed": 4
      },
      "weather": "pcloudyday"
    },
    {
      "timepoint": 111,
      "cloudcover": 7,
      "lifted_index": 15,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "54%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "oshowerday"
    },
    {
      "timepoint": 114,
      "cloudcover": 8,
      "lifted_index": 15,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 9,
      "rh2m": "78%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 117,
      "cloudcover": 9,
      "lifted_index": 15,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "90%",
      "wind10m": {
        "direction": "SW",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 120,
      "cloudcover": 9,
      "lifted_index": 10,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 9,
      "rh2m": "85%",
      "wind10m": {
        "direction": "SW",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 123,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 1,
      "temp2m": 12,
      "rh2m": "80%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 126,
      "cloudcover": 7,
      "lifted_index": 6,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "85%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "oshowerday"
    },
    {
      "timepoint": 129,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 11,
      "rh2m": "85%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 132,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 12,
      "rh2m": "70%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 135,
      "cloudcover": 8,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 13,
      "rh2m": "55%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 138,
      "cloudcover": 8,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "70%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 141,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "72%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 144,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "77%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 147,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "81%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "cloudynight"
    },
    {
      "timepoint": 150,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "none",
      "prec_amount": 0,
      "temp2m": 7,
      "rh2m": "84%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "cloudyday"
    },
    {
      "timepoint": 153,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "73%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 156,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 11,
      "rh2m": "74%",
      "wind10m": {
        "direction": "W",
        "speed": 4
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 159,
      "cloudcover": 8,
      "lifted_index": -1,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 11,
      "rh2m": "72%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 162,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 9,
      "rh2m": "81%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 165,
      "cloudcover": 8,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "88%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 168,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "88%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 171,
      "cloudcover": 9,
      "lifted_index": -1,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "80%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 174,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 6,
      "rh2m": "95%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 177,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 8,
      "rh2m": "84%",
      "wind10m": {
        "direction": "W",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 180,
      "cloudcover": 9,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "74%",
      "wind10m": {
        "direction": "NW",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 183,
      "cloudcover": 8,
      "lifted_index": 2,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 10,
      "rh2m": "73%",
      "wind10m": {
        "direction": "N",
        "speed": 3
      },
      "weather": "lightrainday"
    },
    {
      "timepoint": 186,
      "cloudcover": 7,
      "lifted_index": 6,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 7,
      "rh2m": "78%",
      "wind10m": {
        "direction": "N",
        "speed": 3
      },
      "weather": "oshowernight"
    },
    {
      "timepoint": 189,
      "cloudcover": 9,
      "lifted_index": 6,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 7,
      "rh2m": "79%",
      "wind10m": {
        "direction": "N",
        "speed": 3
      },
      "weather": "lightrainnight"
    },
    {
      "timepoint": 192,
      "cloudcover": 9,
      "lifted_index": 10,
      "prec_type": "rain",
      "prec_amount": 0,
      "temp2m": 6,
      "rh2m": "80%",
      "wind10m": {
        "direction": "N",
        "speed": 2
      },
      "weather": "lightrainnight"
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
