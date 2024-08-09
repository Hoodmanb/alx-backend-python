#!/usr/bin/env python3
"""Import wait_random from the previous python file that youve w"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ascending order without using sort() because of concurrency."""
    total = await asyncio.gather(
        *[task_wait_random(max_delay) for x in range(n)]
    )
    return sorted(total)
