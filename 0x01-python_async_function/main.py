import asyncio


async def download_file1():
    print("Downloading file 1...")
    await asyncio.sleep(1)  # Simulate waiting for download
    print("Downloaded file 1")


async def download_file2():
    print("Downloading file 2...")
    await asyncio.sleep(1)  # Simulate waiting for download
    print("Downloaded file 2")


async def main():
    await asyncio.gather(download_file2(), download_file1())  # Run both downloads concurrently


if __name__ == '__main__':
    asyncio.run(main())
