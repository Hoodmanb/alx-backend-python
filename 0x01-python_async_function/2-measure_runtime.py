#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay as arguments
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Your function should return a float.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start_time)/n
