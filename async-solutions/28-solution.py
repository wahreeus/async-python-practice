import asyncio
import sys



async def worker(worker_id: int, queue: asyncio.Queue) -> None:
    while True:
        job_id, delay_ms = await queue.get()
        try:
            delay_s = float(delay_ms) / 1000
            await asyncio.sleep(delay_s)
            print(worker_id, job_id)
        finally:
            queue.task_done()



async def main() -> None:
    workers, n = map(int, sys.stdin.readline().strip().split())
    queue = asyncio.Queue()
    for _ in range(n):
        job_id, delay_ms = sys.stdin.readline().strip().split()
        await queue.put((job_id, delay_ms))

    tasks = []
    for worker_id in range(workers):
        task = asyncio.create_task(worker(worker_id, queue))
        tasks.append(task)

    await queue.join()
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)



if __name__ == "__main__":
    asyncio.run(main())