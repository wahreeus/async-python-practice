import asyncio
import sys



async def process_task(job_id: str, delay_ms: int) -> str:
    delay_s = delay_ms / 1000
    await asyncio.sleep(delay_s)
    return job_id



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for _ in range(n):
        job_id, delay_ms = sys.stdin.readline().strip().split()
        task = asyncio.create_task(process_task(job_id, int(delay_ms)))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        job_id = await task
        print(f"FINISHED {job_id}")



if __name__ == "__main__":
    asyncio.run(main())