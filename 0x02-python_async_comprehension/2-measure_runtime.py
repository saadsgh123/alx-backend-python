#!/usr/bin/env python3
"""a python module to measure the execution time"""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_com 4 times
    :return: the total execution time required to complete the task
    """
    start = perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = perf_counter() - start
    return elapsed
