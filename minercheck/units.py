"""Numbers and units. Everything is Decimal: a price of 82846.985 must stay 82846.985.

Each quantity has one canonical unit. Values are converted to it before any
comparison, and converted back only when rendering.

  temperature  C      (F, K accepted)
  speed        km/h   (m/s, mph, kn accepted)
  percent      %
  money        <currency code>; "cents" scales by 0.01; USDT/USDC count as USD
  ratio        (no unit; FX rates)
"""
from __future__ import annotations

import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN

# Unicode minus, thin spaces and NBSP show up in HTML/text answers.
_MINUS = {"−": "-", "–": "-"}
_SPACES = {" ": " ", " ": " ", " ": " "}

# 82,846.985 | -1.65 | 1e-5 | .5  (thousands separators only in the 1,234,567 form)
_NUM_RE = re.compile(
    r"(?<![\w.])[-+]?(?:\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?|\.\d+)(?:[eE][-+]?\d+)?"
)

TEMPERATURE_UNITS = {
    "c": "C", "°c": "C", "ºc": "C", "celsius": "C", "degc": "C", "deg c": "C", "° c": "C",
    "f": "F", "°f": "F", "ºf": "F", "fahrenheit": "F", "degf": "F", "deg f": "F", "° f": "F",
    "k": "K", "kelvin": "K",
}
SPEED_UNITS = {
    "km/h": "km/h", "kmh": "km/h", "kph": "km/h", "kmph": "km/h", "km/hr": "km/h",
    "m/s": "m/s", "mps": "m/s", "ms-1": "m/s",
    "mph": "mph", "mi/h": "mph",
    "kn": "kn", "kt": "kn", "kts": "kn", "knots": "kn", "knot": "kn",
}
PERCENT_UNITS = {"%": "%", "percent": "%", "pct": "%"}
# Quote currencies a crypto/stock price may be stated in. Stablecoins count as USD.
CURRENCY_SYMBOLS = {"$": "USD", "us$": "USD", "€": "EUR", "£": "GBP", "¥": "JPY", "₹": "INR", "₨": "PKR"}
USD_EQUIVALENT = {"USD", "USDT", "USDC", "BUSD", "DAI", "TUSD", "FDUSD", "USDP"}
CENT_WORDS = {"cents", "cent", "¢", "usd_cents"}

CANONICAL = {"temperature": "C", "speed": "km/h", "percent": "%", "ratio": "", "number": ""}


def to_decimal(value) -> Decimal | None:
    """Exact Decimal from a JSON number/str. bool and non-numeric text -> None."""
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, Decimal):
        return value
    if isinstance(value, int):
        return Decimal(value)
    if isinstance(value, float):
        return Decimal(repr(value))  # repr round-trips; Decimal(float) would add binary noise
    if isinstance(value, str):
        n, _unit = parse_number(value)
        return n
    return None


def clean_text(s: str) -> str:
    for k, v in {**_MINUS, **_SPACES}.items():
        s = s.replace(k, v)
    return s.strip()


def parse_number(text: str) -> tuple[Decimal | None, str]:
    """First number in text and the unit-ish token right after it.

    '+35°C' -> (35, '°C');  '82,846.985 USD' -> (82846.985, 'USD');  'hot' -> (None, '')
    """
    t = clean_text(str(text))
    m = _NUM_RE.search(t)
    if not m:
        return None, ""
    try:
        n = Decimal(m.group(0).replace(",", ""))
    except InvalidOperation:
        return None, ""
    rest = t[m.end():].strip()
    unit = re.match(r"^(°\s?[A-Za-z]|º[A-Za-z]|%|¢|[A-Za-z][A-Za-z/\-0-9]*)", rest)
    before = t[: m.start()].strip()
    unit_tok = unit.group(1) if unit else ""
    # Currency symbols usually come first: "$82,846" / "€0.89"
    if not unit_tok and before:
        sym = before.split()[-1] if before.split() else ""
        if sym.lower() in CURRENCY_SYMBOLS or sym[-1:] in CURRENCY_SYMBOLS:
            unit_tok = sym if sym.lower() in CURRENCY_SYMBOLS else sym[-1:]
    return n, unit_tok


def has_percent(text: str) -> bool:
    return "%" in str(text) or re.search(r"\bper\s?cent\b|\bpct\b", str(text), re.I) is not None


def unit_of(token: str, quantity: str) -> str | None:
    """Map a raw unit token to the canonical spelling for that quantity, or None."""
    t = (token or "").strip().lower()
    if not t:
        return None
    if quantity == "temperature":
        return TEMPERATURE_UNITS.get(t)
    if quantity == "speed":
        return SPEED_UNITS.get(t)
    if quantity == "percent":
        return PERCENT_UNITS.get(t)
    if quantity == "money":
        if t in CENT_WORDS:
            return "cents"
        if t in CURRENCY_SYMBOLS:
            return CURRENCY_SYMBOLS[t]
        if re.fullmatch(r"[a-z]{3,5}", t):
            return t.upper()
        return None
    return None


def to_canonical(value: Decimal, unit: str, quantity: str, *, quote: str = "USD") -> Decimal:
    """Convert value in `unit` to the canonical unit of `quantity`. Raises ValueError if impossible."""
    if quantity == "temperature":
        if unit == "C":
            return value
        if unit == "F":
            return (value - 32) * 5 / 9
        if unit == "K":
            return value - Decimal("273.15")
        raise ValueError(f"temperature unit {unit!r} not supported")
    if quantity == "speed":
        factor = {"km/h": Decimal(1), "m/s": Decimal("3.6"), "mph": Decimal("1.609344"), "kn": Decimal("1.852")}
        if unit not in factor:
            raise ValueError(f"speed unit {unit!r} not supported")
        return value * factor[unit]
    if quantity == "percent":
        if unit not in ("%", ""):
            raise ValueError(f"percent unit {unit!r} not supported")
        return value
    if quantity == "money":
        if unit == "cents":
            return value / 100
        u, q = unit.upper(), quote.upper()
        if u == q or (u in USD_EQUIVALENT and q in USD_EQUIVALENT):
            return value
        raise ValueError(f"price is in {unit}, but {quote} was asked")
    if quantity in ("ratio", "number"):
        return value
    raise ValueError(f"unknown quantity {quantity!r}")


def from_canonical(value: Decimal, unit: str, quantity: str) -> Decimal:
    """Canonical -> display unit (rendering only)."""
    if quantity == "temperature":
        if unit == "F":
            return value * 9 / 5 + 32
        if unit == "K":
            return value + Decimal("273.15")
        return value
    if quantity == "speed":
        factor = {"km/h": Decimal(1), "m/s": Decimal("3.6"), "mph": Decimal("1.609344"), "kn": Decimal("1.852")}
        return value / factor.get(unit, Decimal(1))
    return value


def fmt(value: Decimal, places: int | None = None, *, grouping: bool = False, sig: int | None = None) -> str:
    """Human number: fixed places (trailing zeros of the fraction kept only if places given),
    or significant digits for tiny values."""
    if sig is not None and value != 0 and abs(value) < 1:
        q = Decimal(1).scaleb(value.adjusted() - sig + 1)
        value = value.quantize(q, rounding=ROUND_HALF_EVEN)
        s = format(value, "f")
        return s.rstrip("0").rstrip(".") if "." in s else s
    if places is not None:
        value = value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_EVEN)
    s = f"{value:,f}" if grouping else format(value, "f")
    if places is None and "." in s:
        s = s.rstrip("0").rstrip(".")
    return s
