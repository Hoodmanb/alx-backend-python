#!/usr/bin/env python3
"""The coroutine will collect 10 random numbers using an async"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers using an async"""
    num = [item async for item in async_generator()]
    return num
