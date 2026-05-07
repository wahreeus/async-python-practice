import asyncio
import sys

async def run_job(name, outcome, sem):
    await sem.acquire()

    if outcome == "FAIL":
        raise RuntimeError(name)

    await asyncio.sleep(0)
    sem.release()
    return f"{name} OK"

async def main():
    limit, n = map(int, sys.stdin.readline().split())
    sem = asyncio.Semaphore(limit)
    rows = [sys.stdin.readline().split() for _ in range(n)]

    for name, outcome in rows:
        try:
            print(await run_job(name, outcome, sem))
        except RuntimeError:
            print(f"{name} ERROR")

asyncio.run(main())
