#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve w"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ascending order without using sort() because of concurrency."""
    total = await asyncio.gather(
        *[wait_random(max_delay) for x in range(n)]
    )
    return sorted(total)
