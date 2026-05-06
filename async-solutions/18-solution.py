import asyncio
import sys



async def main() -> None:
    interval_ms, count = map(int, sys.stdin.readline().strip().split())
    interval_s = interval_ms/1000

    for i in range(1, count + 1):
        await asyncio.sleep(interval_s)
        print(f"TICK {i} AT {interval_ms*i}")



if __name__ == "__main__":
    asyncio.run(main())