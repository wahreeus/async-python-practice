import asyncio
import sys



lock = asyncio.Lock()



async def handle(name, outcome):
    await lock.acquire() # ADDED
    try: # ADDED
        # REMOVED await lock.acquire()
        if outcome == "FAIL":
            raise RuntimeError(name)
        await asyncio.sleep(0)
        # REMOVED lock.release()
        return f"{name} OK"
    finally: # ADDED
        lock.release() # ADDED



async def main():
    n = int(sys.stdin.readline())
    rows = [sys.stdin.readline().split() for _ in range(n)]
    for name, outcome in rows:
        try:
            print(await handle(name, outcome))
        except RuntimeError:
            print(f"{name} ERROR")



asyncio.run(main())