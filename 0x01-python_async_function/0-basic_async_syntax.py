#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    (max_delay, with a default value of 10) named wait_rando
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
