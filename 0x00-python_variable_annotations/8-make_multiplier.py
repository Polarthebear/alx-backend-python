#!/usr/bin/env python3
"""Module for 8-make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return multiply"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
