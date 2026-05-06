import asyncio
import sys



async def process_task(semaphore: asyncio.Semaphore, value: int, delay_s: float) -> tuple[int, int]:
    async with semaphore:
        await asyncio.sleep(delay_s)
        return value, value*value



async def main() -> None:
    limit, n = map(int, sys.stdin.readline().strip().split())
    semaphore = asyncio.Semaphore(limit)
    tasks = []
    for _ in range(n):
        value, delay_ms = map(int, sys.stdin.readline().strip().split())
        delay_s = delay_ms/1000
        task = asyncio.create_task(process_task(semaphore, value, delay_s))
        tasks.append(task)
    
    for task in asyncio.as_completed(tasks):
        value, square = await task
        print(f"{value} {square}")



if __name__ == "__main__":
    asyncio.run(main())