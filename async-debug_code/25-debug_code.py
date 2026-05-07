import asyncio
import sys

counter = 0

async def increment():
    global counter
    current = counter
    await asyncio.sleep(0)
    counter = current + 1

async def main():
    n = int(sys.stdin.readline())
    await asyncio.gather(*(increment() for _ in range(n)))
    print("COUNT", counter)

asyncio.run(main())
