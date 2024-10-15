#!/usr/bin/env python3
""" a python module to loop 10 times """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ async_generator - function to loop 10 times """
    results = [data async for data in async_generator()]
    return results
