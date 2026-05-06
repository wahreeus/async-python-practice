import asyncio
import sys



async def consumer(queue: asyncio.Queue, process_ms: int, n: int) -> list[str]:
    process_s = process_ms / 1000
    current_ms = 0
    output = []
    for _ in range(n):
        item_id, produced_at_ms = await queue.get()
        current_ms = max(current_ms, produced_at_ms)
        await asyncio.sleep(process_s)
        current_ms += process_ms
        output.append(f"{item_id} CONSUMED {current_ms}")
    return output



async def main() -> None:
    queue_size, process_ms, n = map(int, sys.stdin.readline().strip().split())
    queue = asyncio.Queue(queue_size)
    consumer_task = asyncio.create_task(consumer(queue, process_ms, n))

    def get_time():
        return asyncio.get_running_loop().time()

    time_zero = get_time()
    for _ in range(n):
        item_id, produced_at_ms = sys.stdin.readline().strip().split()
        produced_at_ms = float(produced_at_ms) / 1000

        production_time = time_zero + produced_at_ms
        current_time = get_time()
        if current_time < production_time:
            await asyncio.sleep(production_time - current_time)
        await queue.put((item_id, produced_at_ms))

    output = await consumer_task
    for line in output:
        print(line)



if __name__ == "__main__":
    asyncio.run(main())