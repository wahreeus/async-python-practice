import asyncio
import sys



async def process_task(shard_id, delay_ms):
    delay_s = delay_ms/1000
    await asyncio.sleep(delay_s)
    return shard_id, delay_ms



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    shard_count = 0
    for _ in range(n):
        shard_id, delay_ms, count = sys.stdin.readline().strip().split()
        delay_ms, count = int(delay_ms), int(count)
        for _ in range(count):
            shard_count += 1
            task = asyncio.create_task(process_task(shard_id, delay_ms))
            tasks.append(task)

    results = await asyncio.gather(*tasks)
    slowest_id, _ = max(results, key=lambda item : item[1])
    print(f"TOTAL {shard_count}")
    print(f"SLOWEST {slowest_id}")
    


if __name__ == "__main__":
    asyncio.run(main())