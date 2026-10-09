"""Error types. Every message must say what is wrong and where, in plain words."""
from __future__ import annotations


class MinerCheckError(Exception):
    """Base error."""


class SpecError(MinerCheckError):
    """An intent spec YAML is invalid. Raised at load time, never later."""


class InputError(MinerCheckError):
    """A user input could not be normalized (unknown city, coin, currency, ...)."""


class ExtractError(MinerCheckError):
    """No extraction rule produced a value from a response."""
