import asyncio
import sys



async def process_item(semaphore: asyncio.Semaphore, item_id: str, download_ms: int, transform_ms: int) -> str:
    await asyncio.sleep(download_ms / 1000)

    async with semaphore:
        await asyncio.sleep(transform_ms / 1000)

    return item_id



async def main() -> None:
    transform_limit, n = map(int, sys.stdin.readline().strip().split())
    semaphore = asyncio.Semaphore(transform_limit)
    tasks = []
    for _ in range(n):
        item_id, download_ms, transform_ms = sys.stdin.readline().strip().split()
        download_ms, transform_ms = int(download_ms), int(transform_ms)
        task = asyncio.create_task(process_item(semaphore, item_id, download_ms, transform_ms))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        item_id = await task
        print(item_id)



if __name__ == "__main__":
    asyncio.run(main())