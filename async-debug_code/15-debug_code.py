import asyncio
import sys

async def main():
    n = int(sys.stdin.readline())
    queue = asyncio.LifoQueue()

    for _ in range(n):
        await queue.put(sys.stdin.readline().strip())

    while not queue.empty():
        item = await queue.get()
        print(item)
        queue.task_done()

asyncio.run(main())
