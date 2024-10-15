#!/usr/bin/env python3
""" a python module to loop 10 times """
import asyncio
import random


async def async_generator():
    """ async_generator - function to loop 10 times """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(a=0, b=10)