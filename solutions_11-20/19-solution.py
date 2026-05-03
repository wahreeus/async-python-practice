import asyncio
import sys



async def process_task(job_id: str, delay_s: float) -> str:
    await asyncio.sleep(delay_s)
    return job_id



async def main() -> None:
    k, n = map(int, sys.stdin.readline().strip().split())
    tasks = []
    for _ in range(n):
        job_id, delay_ms = sys.stdin.readline().strip().split()
        delay_s = float(delay_ms)/1000
        task = asyncio.create_task(process_task(job_id, delay_s))
        tasks.append(task)

    taken = 0
    for task in asyncio.as_completed(tasks):
        job_id = await task
        print(f"TAKE {job_id}")
        taken += 1
        if taken >= k:
            break

    for task in tasks:
        if not task.done():
            task.cancel()

    print(f"CANCELLED {n-k}")



if __name__ == "__main__":
    asyncio.run(main())