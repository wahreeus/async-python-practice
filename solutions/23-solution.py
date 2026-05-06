import asyncio
import sys



async def process_job(job_id: str, delay_ms: str) -> str:
    delay_s = float(delay_ms) / 1000
    await asyncio.sleep(delay_s)
    return job_id



async def process_batch(batch: list[tuple[str, str]]) -> None:
    tasks = []
    for job_id, delay_ms in batch:
        task = asyncio.create_task(process_job(job_id, delay_ms))
        tasks.append(task)
        
    for task in asyncio.as_completed(tasks):
        job_id = await task
        print(job_id)



async def main() -> None:
    batch_size, n = map(int, sys.stdin.readline().strip().split())
    batch = []
    for _ in range(n):
        job_id, delay_ms = sys.stdin.readline().strip().split()
        batch.append((job_id, delay_ms))
        if len(batch) == batch_size:
            await process_batch(batch)
            batch = []

    if batch:
        await process_batch(batch)



if __name__ == "__main__":
    asyncio.run(main())