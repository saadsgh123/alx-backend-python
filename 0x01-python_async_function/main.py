import asyncio
from random import random, Random


async def task1():
    await asyncio.sleep(2)
    print("Task 1 finished!")


async def task2():
    print("Task 2 finished!")


async def main():
    await asyncio.gather(task1(), task2())


if __name__ == '__main__':
    print(Random.randrange(start=0, stop=10))
