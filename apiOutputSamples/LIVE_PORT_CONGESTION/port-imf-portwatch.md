---
intent: LIVE_PORT_CONGESTION
slug: port-imf-portwatch
status: approved
captured_at: 2026-10-08T04:42:38Z
request_url: https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Ports_Data/FeatureServer/0/query?where=portname%3D%27Rotterdam%27+AND+year%3D2025+AND+month%3D9+AND+day%3D15&outFields=portname,date,portcalls_container,portcalls&f=json
content_type: application/json
inputs: |
  {"port": "Rotterdam", "year": "2025", "month": "9", "day": "15"}
intent_description: |
  Measures commercial container port vessel queue wait times, berth occupancy ratios, and dwell day averages.
answer_requirement: |
  Must return the measured daily container-vessel port-call count (portcalls_container) for pinned port Rotterdam on pinned date 2025-09-15. Queue wait / berth occupancy / dwell are NOT published by any keyless source; vessel counts are the only measured, replayable part (Usman: 'congestion' is derived and live AIS snapshots do not converge, so a HISTORICAL date is pinned).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the exact information requested: the portcalls_container value for the specified date."
reviewed_at: 2026-10-08T05:00:08Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "objectIdFieldName": "ObjectId",
  "uniqueIdField": {
    "name": "ObjectId",
    "isSystemMaintained": true
  },
  "globalIdFieldName": "",
  "fields": [
    {
      "name": "portname",
      "type": "esriFieldTypeString",
      "alias": "portname",
      "sqlType": "sqlTypeNVarchar",
      "length": 4000,
      "domain": null,
      "defaultValue": null
    },
    {
      "name": "date",
      "type": "esriFieldTypeDateOnly",
      "alias": "date",
      "sqlType": "sqlTypeDate",
      "domain": null,
      "defaultValue": null
    },
    {
      "name": "portcalls_container",
      "type": "esriFieldTypeInteger",
      "alias": "portcalls_container",
      "sqlType": "sqlTypeInteger",
      "domain": null,
      "defaultValue": null
    },
    {
      "name": "portcalls",
      "type": "esriFieldTypeInteger",
      "alias": "portcalls",
      "sqlType": "sqlTypeInteger",
      "domain": null,
      "defaultValue": null
    }
  ],
  "features": [
    {
      "attributes": {
        "portname": "Rotterdam",
        "date": "2025-09-15",
        "portcalls_container": 11,
        "portcalls": 56
      }
    }
  ]
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the exact information requested: the portcalls_container value for the specified date._
