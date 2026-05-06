import asyncio
import sys



async def process_task(call_id: str, delay_ms: str, outcome: str) -> tuple[str, str | RuntimeError]:
    delay_s = int(delay_ms)/1000
    try:
        await asyncio.sleep(delay_s)
        if outcome == "FAIL":
            raise RuntimeError("ERROR")
        return call_id, "OK"

    except RuntimeError as e:
        return call_id, e



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for _ in range(n):
        call_id, delay_ms, outcome = sys.stdin.readline().strip().split()
        task = asyncio.create_task(process_task(call_id, delay_ms, outcome))
        tasks.append(task)

    for call_id, status in await asyncio.gather(*tasks):
        print(f"{call_id} {status}")



if __name__ == "__main__":
    asyncio.run(main())