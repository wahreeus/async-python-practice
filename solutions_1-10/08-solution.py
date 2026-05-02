import asyncio
import sys



# Forced use of asyncio.wait_for() in process_task().



async def process_task(request_id: str, delay_ms: int, max_delay_ms: int) -> tuple[str, str]:
    delay_s = delay_ms / 1000
    max_delay_s = max_delay_ms / 1000

    if delay_ms == max_delay_ms: # Edge case handling.
        await asyncio.sleep(delay_s)
        return request_id, "OK"

    try:
        await asyncio.wait_for(asyncio.sleep(delay_s), max_delay_s)
        return request_id, "OK"
    except asyncio.TimeoutError:
        return request_id, "TIMEOUT"



async def main() -> None:
    max_delay_ms, n = map(int,sys.stdin.readline().strip().split())

    tasks = []
    for _ in range(n):
        request_id, delay_ms = sys.stdin.readline().strip().split()
        delay_ms = int(delay_ms)
        task = asyncio.create_task(process_task(request_id, delay_ms, max_delay_ms))
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    for request_id, status in results:
        print(f"{request_id} {status}")



if __name__ == "__main__":
    asyncio.run(main())