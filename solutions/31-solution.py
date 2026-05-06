import asyncio
import sys



async def process(capacity, refill, refill_ms, n, queue):
    available_tokens = capacity
    current_time = 0
    next_refill_time = refill_ms

    output = []
    for _request in range(n):
        request_id, arrival_time = await queue.get()

        current_time = max(current_time, arrival_time)
        while next_refill_time <= current_time:
            available_tokens = min(capacity, available_tokens + refill)
            next_refill_time += refill_ms

        if available_tokens == 0:
            current_time = next_refill_time
            available_tokens = min(capacity, available_tokens + refill)
            next_refill_time += refill_ms

        available_tokens -= 1
        output.append(f"{request_id} START {current_time}")

    return output



async def main() -> None:
    capacity, refill, refill_ms, n = map(int, sys.stdin.readline().split())
    queue = asyncio.Queue()
    for _ in range(n):
        request_id, arrival_ms = sys.stdin.readline().split()
        await queue.put((request_id, int(arrival_ms)))

    result = await process(capacity, refill, refill_ms, n, queue)
    for line in result:
        print(line)



if __name__ == "__main__":
    asyncio.run(main())