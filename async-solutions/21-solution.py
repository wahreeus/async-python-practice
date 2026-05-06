import asyncio
import sys



async def process_batch(queue: asyncio.Queue, start_second: int) -> None:
    while not queue.empty():
        request_id, _arrival_second = await queue.get()
        print(f"{request_id} START {start_second}")
        queue.task_done()



async def main() -> None:
    limit, n = map(int, sys.stdin.readline().strip().split())
    queue = asyncio.Queue()
    batch_size = limit
    start_second = None
    for _ in range(n):
        request_id, arrival_second = sys.stdin.readline().strip().split()
        arrival_second = int(arrival_second)

        if start_second is None:
            start_second = arrival_second

        await queue.put((request_id, arrival_second))

        if queue.qsize() == batch_size:
            await process_batch(queue, start_second)
            start_second += 1

    if not queue.empty():
        await process_batch(queue, start_second)



if __name__ == "__main__":
    asyncio.run(main())