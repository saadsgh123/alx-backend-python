#!/usr/bin/env python3
"""
module that contain a function that takes in an integer
argument named wait_random that waits for a random delay
between 0 and max_delay seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function that takes in an integer that waits for a random delay
    :param max_delay:  in seconds
    :return: number of seconds taken
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
