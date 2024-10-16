#!/usr/bin/env python3
"""Module for 7-to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple."""
    return (k, float(v ** 2))
