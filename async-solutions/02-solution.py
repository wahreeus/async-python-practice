import asyncio
import sys



async def process_request(request_id: str, delay_ms: int, input_index: int) -> tuple[str, int, int]:
    delay_s = delay_ms/1000
    await asyncio.sleep(delay_s)
    return request_id, delay_ms, input_index



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for input_index in range(n):
        request_id, delay_ms = sys.stdin.readline().strip().split()
        delay_ms = int(delay_ms)
        task = asyncio.create_task(process_request(request_id, delay_ms, input_index))
        tasks.append(task)

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)
    
    results.sort(key=lambda item: (item[1], item[2]))
    for request_id, _, _ in results:
        print(request_id)



if __name__ == "__main__":
    asyncio.run(main())