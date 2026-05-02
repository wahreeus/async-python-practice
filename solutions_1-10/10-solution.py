import asyncio
import sys



async def finish(name, delay):
    await asyncio.sleep(delay / 1000)
    return name



async def main():
    n = int(sys.stdin.readline())
    tasks = []
    for _ in range(n):
        name, delay = sys.stdin.readline().split()
        tasks.append(asyncio.create_task(finish(name, int(delay))))

    # REMOVED results = await asyncio.gather(*tasks)
    # REMOVED for name in results:
    # REMOVED   print(name)

    for task in asyncio.as_completed(tasks): # ADDED
        name = await task                    # ADDED
        print(name)                          # ADDED



asyncio.run(main())
