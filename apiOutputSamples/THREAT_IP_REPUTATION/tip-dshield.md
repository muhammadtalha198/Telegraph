---
intent: THREAT_IP_REPUTATION
slug: tip-dshield
status: approved
captured_at: 2026-10-05T09:33:28Z
request_url: https://isc.sans.edu/api/ip/1.1.1.1?json
content_type: application/json
inputs: |
  {"ip": "1.1.1.1"}
intent_description: |
  Assesses malicious IP address risk scores, botnet associations, and brute-force history across threat registries.
answer_requirement: |
  Must return a malicious-activity risk assessment / reputation for the IP asked.
capture_note: |
  golden-test PASS: SANS ISC DShield
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains details about the IP's network and associations but lacks a risk assessment."
reviewed_at: 2026-10-05T11:56:01Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "ip": {
    "number": "1.1.1.1",
    "count": null,
    "attacks": null,
    "maxdate": null,
    "mindate": null,
    "updated": null,
    "comment": null,
    "maxrisk": null,
    "asabusecontact": "abuse@cloudflare.com",
    "as": 13335,
    "asname": "CLOUDFLARENET",
    "ascountry": "US",
    "assize": 2500608,
    "network": "1.1.1.0/24",
    "threatfeeds": {
      "mastodon": {
        "lastseen": "2026-10-05",
        "firstseen": "2023-07-13"
      },
      "openresolver": {
        "lastseen": "2026-10-05",
        "firstseen": "2022-02-04"
      },
      "rosti": {
        "lastseen": "2026-10-04",
        "firstseen": "2024-06-17"
      }
    },
    "alexa": {
      "lastrank": 4585,
      "domains": 2,
      "firstseen": "2015-12-29",
      "lastseen": "2015-12-29",
      "hostname": "null.scientificamerican.com"
    }
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains details about the IP's network and associations but lacks a risk assessment._
