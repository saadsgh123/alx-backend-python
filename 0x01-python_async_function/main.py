import asyncio


# An asynchronous generator that simulates fetching data
async def async_data_fetcher():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate network delay
        yield f"Data {i + 1}"


async def main():
    # Using async comprehension to collect results from the async generator
    results = [data async for data in async_data_fetcher()]

    print("Fetched results:")
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
