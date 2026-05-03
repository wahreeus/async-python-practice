import asyncio
import sys



async def process_task(endpoint: str, delay_ms: int, outcomes: str, max_attempts: int) -> tuple[str, str, int]:
    delay_s = delay_ms/1000
    for i in range(max_attempts):
        await asyncio.sleep(delay_s)
        if outcomes[i] == "O":
            return endpoint, "OK", i+1
    return endpoint, "FAIL", max_attempts



async def main() -> None:
    max_attempts, n = map(int, sys.stdin.readline().strip().split())
    tasks: list[asyncio.Task[tuple[str, str, int]]] = []
    for _ in range(n):
        endpoint, delay_ms, outcomes = sys.stdin.readline().strip().split()
        delay_ms = int(delay_ms)
        task = asyncio.create_task(process_task(endpoint, delay_ms, outcomes, max_attempts))
        tasks.append(task)

    output = await asyncio.gather(*tasks)
    for endpoint, status, attempts in output:
        print(f"{endpoint} {status} {attempts}")



if __name__ == "__main__":
    asyncio.run(main())