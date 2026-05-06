import asyncio
import sys



counter = 0



async def increment(lock): # EDITED
    global counter
    async with lock: # ADDED
        current = counter
        await asyncio.sleep(0)
        counter = current + 1



async def main():
    n = int(sys.stdin.readline())
    lock = asyncio.Lock() # ADDED
    await asyncio.gather(*(increment(lock) for _ in range(n))) # EDITED
    print("COUNT", counter)



asyncio.run(main())