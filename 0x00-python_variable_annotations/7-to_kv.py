#!/usr/bin/env python3
"""function to_kv that takes a string k and an int OR float as
arguments"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return k, v**2
