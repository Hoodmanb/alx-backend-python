#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier as arg"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier."""
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
