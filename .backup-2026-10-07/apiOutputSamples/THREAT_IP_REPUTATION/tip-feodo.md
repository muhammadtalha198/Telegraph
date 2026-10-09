---
intent: THREAT_IP_REPUTATION
slug: tip-feodo
status: approved
captured_at: 2026-10-05T09:33:28Z
request_url: https://feodotracker.abuse.ch/downloads/ipblocklist.json
content_type: application/json
inputs: |
  {"ip": "1.1.1.1"}
intent_description: |
  Assesses malicious IP address risk scores, botnet associations, and brute-force history across threat registries.
answer_requirement: |
  Must return a malicious-activity risk assessment / reputation for the IP asked.
capture_note: |
  golden-test PASS: abuse.ch Feodo Tracker
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains multiple entries for different IPs, none of which match the requested IP."
reviewed_at: 2026-10-05T11:56:18Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
[
  {
    "ip_address": "162.243.103.246",
    "port": 8080,
    "status": "offline",
    "hostname": null,
    "as_number": 14061,
    "as_name": "DIGITALOCEAN-ASN",
    "country": "US",
    "first_seen": "2022-06-04 21:24:53",
    "last_online": "2026-03-07",
    "malware": "Emotet"
  },
  {
    "ip_address": "50.16.16.211",
    "port": 443,
    "status": "online",
    "hostname": "ec2-50-16-16-211.compute-1.amazonaws.com",
    "as_number": 14618,
    "as_name": "AMAZON-AES",
    "country": "US",
    "first_seen": "2025-12-30 13:56:31",
    "last_online": "2026-03-12",
    "malware": "QakBot"
  },
  {
    "ip_address": "34.204.119.63",
    "port": 443,
    "status": "offline",
    "hostname": "ec2-34-204-119-63.compute-1.amazonaws.com",
    "as_number": 14618,
    "as_name": "AMAZON-AES",
    "country": "US",
    "first_seen": "2026-01-13 21:41:15",
    "last_online": "2026-03-01",
    "malware": "QakBot"
  },
  {
    "ip_address": "178.62.3.223",
    "port": 443,
    "status": "offline",
    "hostname": "box.nautadb.com",
    "as_number": 14061,
    "as_name": "DIGITALOCEAN-ASN - DigitalOcean, LLC",
    "country": "GB",
    "first_seen": "2026-02-17 05:41:23",
    "last_online": "2026-02-18",
    "malware": "QakBot"
  },
  {
    "ip_address": "27.133.154.218",
    "port": 443,
    "status": "offline",
    "hostname": null,
    "as_number": 9370,
    "as_name": "SAKURA-B SAKURA Internet Inc.",
    "country": "JP",
    "first_seen": "2026-03-04 14:28:39",
    "last_online": "2026-03-05",
    "malware": "QakBot"
  }
]
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains multiple entries for different IPs, none of which match the requested IP._
