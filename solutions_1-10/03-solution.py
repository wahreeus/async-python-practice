import asyncio
import sys



async def process_task(input_index: int, endpoint: str, status_code: int, delay_ms: int) -> tuple[int, str, int]:
    delay_s = delay_ms/1000
    await asyncio.sleep(delay_s)
    return input_index, endpoint, status_code



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for input_index in range(n):
        endpoint, delay_ms, status_code = sys.stdin.readline().strip().split()
        delay_ms, status_code = int(delay_ms), int(status_code)
        task = process_task(input_index, endpoint, status_code, delay_ms)
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    for input_index, endpoint, status_code in results:
        print(f"{input_index} {endpoint} {status_code}")



if __name__ == "__main__":
    asyncio.run(main())