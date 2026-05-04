import asyncio
import sys



async def process_task(job_id: str, delay_ms: str) -> str:
    delay_s = float(delay_ms) / 1000
    await asyncio.sleep(delay_s)
    return job_id



async def worker(pqueue: asyncio.PriorityQueue) -> None:
    while True:
        priority, index, coroutine = await pqueue.get()
        try:
            result = await coroutine
            print(result)
        finally:
            pqueue.task_done()



async def main() -> None:
    workers, n = map(int, sys.stdin.readline().strip().split())
    pqueue = asyncio.PriorityQueue()
    for index in range(n):
        priority, job_id, delay_ms = sys.stdin.readline().strip().split()
        await pqueue.put((int(priority), index, process_task(job_id, delay_ms)))

    worker_tasks = []
    for _ in range(workers):
        task = asyncio.create_task(worker(pqueue))
        worker_tasks.append(task)

    await pqueue.join()
    for task in worker_tasks:
        task.cancel()



if __name__ == "__main__":
    asyncio.run(main())