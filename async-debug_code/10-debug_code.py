import asyncio
import sys

async def finish(name, delay):
    await asyncio.sleep(delay / 1000)
    return name

async def main():
    n = int(sys.stdin.readline())
    tasks = []
    for _ in range(n):
        name, delay = sys.stdin.readline().split()
        tasks.append(asyncio.create_task(finish(name, int(delay))))

    results = await asyncio.gather(*tasks)

    for name in results:
        print(name)

asyncio.run(main())
