"""minercheck: YAML-driven answer verification for intent miners.

Pipeline (one module each):
  spec       load + validate intents/<INTENT>.yaml (fail loudly)
  normalize  user inputs -> canonical inputs (city -> lat/lon/tz, BTC -> ids, ...)
  fetch      HTTP with timeouts, retries, 429 handling, TTL cache
  reader     any body (JSON/XML/HTML/text/CSV) -> Document -> extract by rule
  units      number + unit parsing and conversion (Decimal, no float loss)
  answers    answer_type parsing (temperature, price, fx_rate, date, datetime_tz, ...)
  validate   E1..E5 per candidate
  verify     run sources, cross-check (E3), confidence, honest "could not verify"
  render     YAML templates -> plain English
  catalog    Intent Catalog xlsx -> index, verification tiers, spec audit (catalog is law)
  gate       verify a miner's answer against its catalog intent, called as the node calls it
"""

__version__ = "1.0.0"
