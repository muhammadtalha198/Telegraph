"""Place-name lookup for names not in intents/_shared.yaml (Open-Meteo geocoding, free, keyless)."""
from __future__ import annotations

import json
import logging
from urllib.parse import quote

from .fetch import Fetcher, Request
from .normalize import Geocoder

log = logging.getLogger("minercheck.geocode")
URL = "https://geocoding-api.open-meteo.com/v1/search?name={name}&count=10&language=en&format=json"


def open_meteo_geocoder(fetcher: Fetcher) -> Geocoder:
    def lookup(name: str) -> list[dict]:
        res = fetcher.fetch(Request(URL.format(name=quote(name)), timeout_s=10), cache_ttl_s=7 * 86400)
        if not res.ok:
            log.warning("geocoder failed for %r: %s", name, res.error)
            return []
        try:
            rows = json.loads(res.body).get("results") or []
        except ValueError:
            return []
        return [{"name": r.get("name", ""), "lat": r["latitude"], "lon": r["longitude"],
                 "country": r.get("country", ""), "country_code": r.get("country_code", ""),
                 "admin1": r.get("admin1", ""), "timezone": r.get("timezone", ""),
                 "population": r.get("population") or 0}
                for r in rows if "latitude" in r and "longitude" in r]
    return lookup
