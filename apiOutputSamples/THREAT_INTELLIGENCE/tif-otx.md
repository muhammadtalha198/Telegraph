---
intent: THREAT_INTELLIGENCE
slug: tif-otx
status: pending_review
captured_at: 2026-10-08T04:43:48Z
request_url: https://otx.alienvault.com/api/v1/indicators/IPv4/1.1.1.1/general
content_type: application/json
inputs: |
  {"ip": "1.1.1.1"}
intent_description: |
  Aggregates indicators of compromise (IOCs), malicious IP ranges, and adversary tactics from global security feeds.
answer_requirement: |
  Must return a threat-intel verdict / IOC-association (score, pulse count, classification) for the pinned IP.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "whois": "http://whois.domaintools.com/1.1.1.1",
  "reputation": 0,
  "indicator": "1.1.1.1",
  "type": "IPv4",
  "type_title": "IPv4",
  "base_indicator": {
    "id": 45535,
    "indicator": "1.1.1.1",
    "type": "IPv4",
    "title": "",
    "description": "",
    "content": "",
    "access_type": "public",
    "access_reason": ""
  },
  "pulse_info": {
    "count": 0,
    "pulses": [],
    "references": [],
    "related": {
      "alienvault": {
        "adversary": [],
        "malware_families": [],
        "industries": []
      },
      "other": {
        "adversary": [],
        "malware_families": [],
        "industries": []
      }
    }
  },
  "false_positive": [
    {
      "assessment": "accepted",
      "assessment_date": "2021-05-19T15:37:03.674000",
      "report_date": "2021-04-02T16:16:53.828000"
    }
  ],
  "validation": [
    {
      "source": "false_positive",
      "message": "Known False Positive",
      "name": "Known False Positive"
    },
    {
      "source": "whitelist",
      "message": "contained in whitelisted prefix",
      "name": "Whitelisted IP"
    }
  ],
  "asn": "AS13335 cloudflare",
  "city_data": true,
  "city": null,
  "region": null,
  "continent_code": "OC",
  "country_code3": "AUS",
  "country_code2": "AU",
  "subdivision": null,
  "latitude": -33.494,
  "postal_code": null,
  "longitude": 143.2104,
  "accuracy_radius": 1000,
  "country_code": "AU",
  "country_name": "Australia",
  "dma_code": 0,
  "charset": 0,
  "area_code": 0,
  "flag_url": "/assets/images/flags/au.png",
  "flag_title": "Australia",
  "sections": [
    "general",
    "geo",
    "reputation",
    "url_list",
    "passive_dns",
    "malware",
    "nids_list",
    "http_scans"
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
