import asyncio
import sys

async def worker(name, delay):
    try:
        await asyncio.sleep(delay / 1000)
        return f"{name} OK"
    except BaseException:
        return f"{name} OK"

async def main():
    cancel_after, n = map(int, sys.stdin.readline().split())
    tasks = []

    for _ in range(n):
        name, delay = sys.stdin.readline().split()
        tasks.append(asyncio.create_task(worker(name, int(delay))))

    await asyncio.sleep(cancel_after / 1000)

    for task in tasks:
        if not task.done():
            task.cancel()

    for task in tasks:
        print(await task)

asyncio.run(main())
