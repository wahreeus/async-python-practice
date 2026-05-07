import asyncio
import sys

cache = {}
fetches = 0

async def get_value(key):
    global fetches

    if key not in cache:
        fetches += 1
        await asyncio.sleep(0)
        cache[key] = key.upper()

    return cache[key]

async def main():
    n = int(sys.stdin.readline())
    keys = [sys.stdin.readline().strip() for _ in range(n)]

    values = await asyncio.gather(*(get_value(k) for k in keys))

    for value in values:
        print(value)

    print("FETCHES", fetches)

asyncio.run(main())
