#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve w"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
