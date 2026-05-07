import asyncio
import sys

async def double_later(value, delay):
    await asyncio.sleep(delay / 1000)
    return value * 2

async def main():
    n = int(sys.stdin.readline())
    results = []
    for _ in range(n):
        value, delay = map(int, sys.stdin.readline().split())
        results.append(double_later(value, delay))

    for result in results:
        print(result)

asyncio.run(main())
