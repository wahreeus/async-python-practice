import asyncio
import sys



async def load(value, delay):
    await asyncio.sleep(delay / 1000)
    return value



async def main():
    n = int(sys.stdin.readline())
    tasks = []
    for _ in range(n):
        value, delay = map(int, sys.stdin.readline().split())
        tasks.append(load(value, delay))
    results = await asyncio.gather(*tasks) # EDITED
    print("SUM", sum(results))



asyncio.run(main())