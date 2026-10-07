#!/usr/bin/env python3
"""Thin CAISO OASIS → JSON proxy for GRID_POWER_PRICE miners.

Usman truth spec: CAISO OASIS SingleZip PRC_LMP, node TH_NP15_GEN-APND, DAM.
Generic Telegraph miners expect JSON; OASIS returns a ZIP of XML.
"""
from __future__ import annotations

import io
import re
import zipfile
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

OASIS = "https://oasis.caiso.com/oasisapi/SingleZip"
UA = "TeleGraphCAISOProxy/1.0"


def fetch_lmp(node: str, market: str, start: str, end: str) -> dict:
    url = (
        f"{OASIS}?queryname=PRC_LMP&version=1"
        f"&market_run_id={market}&node={node}"
        f"&startdatetime={start}&enddatetime={end}"
    )
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=60) as resp:
        data = resp.read()
    if data[:2] != b"PK":
        raise RuntimeError(f"OASIS did not return a zip ({len(data)} bytes)")
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        raw = zf.read(zf.namelist()[0]).decode("utf-8", "replace")

    # Prefer full LMP_PRC; fall back to energy component
    items = re.findall(
        r"<DATA_ITEM>([^<]+)</DATA_ITEM>.*?<VALUE>([^<]+)</VALUE>",
        raw,
        re.S,
    )
    by = {k: float(v) for k, v in items}
    if "LMP_PRC" not in by:
        raise RuntimeError(f"no LMP_PRC in OASIS payload; got {list(by)}")
    lmp = by["LMP_PRC"]
    return {
        "iso": "CAISO",
        "node": node,
        "market": market,
        "startdatetime": start,
        "enddatetime": end,
        "lmp_usd_per_mwh": lmp,
        "lmp_usd_per_mwh_milli": int(round(lmp * 1000)),
        "components": by,
        "source": "caiso_oasis_prc_lmp",
    }


def default_window() -> tuple[str, str]:
    # Yesterday 07:00–08:00 UTC — stable DAM hour (Usman-style pin)
    day = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y%m%d")
    return f"{day}T07:00-0000", f"{day}T08:00-0000"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # quieter
        pass

    def do_GET(self):
        u = urlparse(self.path)
        if u.path not in ("/caiso/lmp", "/caiso/lmp.json"):
            self.send_error(404, "use GET /caiso/lmp")
            return
        qs = parse_qs(u.query)
        node = (qs.get("node") or ["TH_NP15_GEN-APND"])[0]
        market = (qs.get("market") or qs.get("market_run_id") or ["DAM"])[0]
        start_d, end_d = default_window()
        start = (qs.get("startdatetime") or [start_d])[0]
        end = (qs.get("enddatetime") or [end_d])[0]
        try:
            body = fetch_lmp(node, market, start, end)
            import json

            raw = json.dumps(body).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)
        except Exception as e:
            msg = json_err(str(e))
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)


def json_err(s: str) -> bytes:
    import json

    return json.dumps({"error": s}).encode()


if __name__ == "__main__":
    import json as _json  # noqa: F401 — used in handler except via json_err

    host, port = "127.0.0.1", 8765
    print(f"CAISO LMP proxy on http://{host}:{port}/caiso/lmp", flush=True)
    ThreadingHTTPServer((host, port), Handler).serve_forever()
