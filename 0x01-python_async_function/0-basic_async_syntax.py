import asyncio
import random
import time


async def wait_random(max_delay=10):
    s = time.perf_counter()
    await asyncio.sleep(random.randint(0, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed
