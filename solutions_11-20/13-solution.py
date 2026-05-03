import asyncio
import sys



async def producer(queue: asyncio.Queue, item_id: str, delay_s: float) -> None:
    await asyncio.sleep(delay_s)
    await queue.put(item_id)



async def consumer(queue: asyncio.Queue) -> None:
    while True:
        item_id = await queue.get()
        if item_id is None:
            queue.task_done()
            break
        print(f"CONSUMED {item_id}")
        queue.task_done()



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    queue = asyncio.Queue()
    consumer_task = asyncio.create_task(consumer(queue))
    producer_tasks = []
    for _ in range(n):
        item_id, delay_ms = sys.stdin.readline().strip().split()
        delay_s = float(delay_ms)/1000
        task = asyncio.create_task(producer(queue, item_id, delay_s))
        producer_tasks.append(task)

    await asyncio.gather(*producer_tasks)
    await queue.put(None)
    await consumer_task



if __name__ == "__main__":
    asyncio.run(main())