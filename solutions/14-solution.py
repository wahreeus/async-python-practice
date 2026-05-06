import asyncio
import sys



async def process_task(endpoint: str, delay_s : float, outcome: str, index: int) -> (str, float, str, int):
    await asyncio.sleep(delay_s)
    return endpoint, delay_s, outcome, index



def outcome_ok(item) -> bool:
    _, _, outcome, _ = item
    return outcome == "OK"



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for index in range(n):
        endpoint, delay_ms, outcome = sys.stdin.readline().strip().split()
        delay_s = float(delay_ms) / 1000
        task = asyncio.create_task(process_task(endpoint, delay_s, outcome, index))
        tasks.append(task)

    output = await asyncio.gather(*tasks)
    output = list(filter(outcome_ok, output))

    if output:
        first = min(output, key=lambda item: (item[1], item[3]))
        print(f"FIRST {first[0]}")
    else:
        print("NONE")



if __name__ == "__main__":
    asyncio.run(main())