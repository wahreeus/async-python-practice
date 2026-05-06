import asyncio
import sys



async def fetch(delay):
    await asyncio.sleep(delay / 1000)
    return "RESULT"



async def main():
    delay, timeout = map(int, sys.stdin.readline().split())
    task = asyncio.create_task(fetch(delay))
    try:
        print(await asyncio.wait_for(asyncio.shield(task), timeout / 1000)) # EDITED
    except asyncio.TimeoutError:
        print("TIMEOUT")
    print(await task)



asyncio.run(main())