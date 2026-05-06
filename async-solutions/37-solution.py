import asyncio
import sys



async def consumer(queue: asyncio.Queue, timeout_ms: int, n: int) -> list[list[str]]:
    batches = []
    last_event_ms = None
    for _ in range(n):
        event_time_ms, event_id = await queue.get()
        first_event = last_event_ms is None
        if first_event or timeout_ms < event_time_ms - last_event_ms:
            batches.append([event_id])
        else:
            batches[-1].append(event_id)
        last_event_ms = event_time_ms
    return batches



async def main() -> None:
    timeout_ms, n = map(int, sys.stdin.readline().strip().split())
    queue = asyncio.Queue()
    consumer_task = asyncio.create_task(consumer(queue, timeout_ms, n))
    for _ in range(n):
        event_time_ms, event_id = sys.stdin.readline().strip().split()
        event_time_ms = int(event_time_ms)
        await queue.put((event_time_ms, event_id))

    batches = await consumer_task
    for batch in batches:
        id_s = " ".join(batch)
        print(f"BATCH {id_s}")



if __name__ == "__main__":
    asyncio.run(main())