#!/usr/bin/env python3
"""
function to_kv that takes a string k and an int OR float as
arguments
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of type string and float"""
    return k, v*v
