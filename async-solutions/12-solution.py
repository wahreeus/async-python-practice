import asyncio
import sys



# Single-digit millisecond sleeps can produce inconsistent completion order due to asyncio scheduling.
# This sensitivity has been observed using asyncio.sleep(delay_ms/500) with sample input 1, where
# repeated runs may produce different output orders, such as A C D B or A C B D.
#
# Stable performance was observed using asyncio.sleep(delay_ms/100).



async def process_task(semaphore: asyncio.Semaphore, job_id: str, delay_ms: int) -> str:
    async with semaphore:
        await asyncio.sleep(delay_ms/1000)
        return job_id



async def main() -> None:
    limit, n = map(int, sys.stdin.readline().strip().split())
    semaphore = asyncio.Semaphore(limit)
    tasks = []
    for _ in range(n):
        job_id, delay_ms = sys.stdin.readline().strip().split()
        task = asyncio.create_task(process_task(semaphore, job_id, int(delay_ms)))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        job_id = await task
        print(job_id)



if __name__ == "__main__":
    asyncio.run(main())