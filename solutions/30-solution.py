import asyncio
import sys


async def worker(name, delay):
    # REMOVED try:
    await asyncio.sleep(delay/1000)
    return f"{name} OK"
    # REMOVED except BaseException:
    # REMOVED     return f"{name} OK"


async def main():
    cancel_after, n = map(int, sys.stdin.readline().split())
    tasks = []
    for _ in range(n):
        name, delay = sys.stdin.readline().split()
        tasks.append((name, asyncio.create_task(worker(name, int(delay))))) # EDITED

    await asyncio.sleep(cancel_after/1000)
    await asyncio.sleep(0) # ADDED
    for name, task in tasks: # EDITED
        if not task.done():
            task.cancel()

    for name, task in tasks: # EDITED
        try: # ADDED
            print(await task)
        except asyncio.CancelledError: # ADDED
            print(f"{name} CANCELLED") # ADDED

asyncio.run(main())