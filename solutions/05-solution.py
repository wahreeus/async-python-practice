import asyncio
import sys



async def double_later(value, delay):
    await asyncio.sleep(delay / 1000)
    return value * 2



async def main():
    n = int(sys.stdin.readline())
    tasks = [] # EDITED
    for _ in range(n):
        value, delay = map(int, sys.stdin.readline().split())
        tasks.append(double_later(value, delay)) # EDITED
    
    results = await asyncio.gather(*tasks) # ADDED

    for result in results:
        print(result)



asyncio.run(main())