import asyncio
import sys



async def parse_worker(parse_queue: asyncio.Queue) -> None:
    while True:
        job_id, parse_ms = await parse_queue.get()
        try:
            await asyncio.sleep(float(parse_ms) / 1000)
            print(job_id)
        finally:
            parse_queue.task_done()



async def download_worker(download_queue: asyncio.Queue, parse_queue: asyncio.Queue) -> None:
    while True:
        job_id, download_ms, parse_ms = await download_queue.get()
        try:
            await asyncio.sleep(float(download_ms) / 1000)
            await parse_queue.put((job_id, parse_ms))
        finally:
            download_queue.task_done()



async def main() -> None:
    download_worker_count, parse_worker_count, n = map(int, sys.stdin.readline().strip().split())
    download_queue = asyncio.Queue()
    for _ in range(n):
        job_id, download_ms, parse_ms = sys.stdin.readline().strip().split()
        await download_queue.put((job_id, download_ms, parse_ms))

    parse_queue = asyncio.Queue()

    d_workers = []
    for _ in range(download_worker_count):
        task = asyncio.create_task(download_worker(download_queue, parse_queue))
        d_workers.append(task)

    p_workers = []
    for _ in range(parse_worker_count):
        task = asyncio.create_task(parse_worker(parse_queue))
        p_workers.append(task)

    await download_queue.join()
    await parse_queue.join()
    for task in d_workers + p_workers:
        task.cancel()
    await asyncio.gather(*d_workers, *p_workers, return_exceptions=True)



if __name__ == "__main__":
    asyncio.run(main())