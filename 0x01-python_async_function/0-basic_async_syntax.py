#!/usr/bin/env python3
import random, asyncio


async def wait_random(max_delay=10):
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num

asyncio.run(wait_random())
