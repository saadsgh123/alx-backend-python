#!/usr/bin/env python3
"""
module that contain a function that takes in an integer
argument named wait_random that waits for a random delay
between 0 and max_delay seconds and eventually returns it.
"""
import asyncio
import random
import time


async def wait_random(max_delay=10):
    """
    function that takes in an integer that waits for a random delay
    :param max_delay:  in seconds
    :return: number of seconds taken
    """
    s = time.perf_counter()
    await asyncio.sleep(random.randint(0, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed
