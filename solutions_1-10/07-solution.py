import asyncio
import sys



async def process_task(event_name: str, delay_ms: str, index: int) -> tuple[str, int, int]:
    delay_ms = int(delay_ms)
    await asyncio.sleep(delay_ms / 1000)
    return event_name, delay_ms, index



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for index in range(n):
        event_name, delay_ms = sys.stdin.readline().strip().split()
        task = asyncio.create_task(process_task(event_name, delay_ms, index))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    results.sort(key=lambda item: (item[1], item[2]))
    for event_name, delay_ms, _ in results:
        print(f"T+{delay_ms} {event_name}")



if __name__ == "__main__":
    asyncio.run(main())