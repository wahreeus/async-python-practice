import asyncio
import sys



async def process_task(input_index: int, child_id: str, delay_ms: int, outcome: str):
    await asyncio.sleep(delay_ms / 1000)
    if outcome == "OK":
        return input_index, child_id
    raise RuntimeError(input_index, child_id)



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for input_index in range(n):
        child_id, delay_ms, outcome = sys.stdin.readline().strip().split()
        delay_ms = int(delay_ms)
        task = asyncio.create_task(process_task(input_index, child_id, delay_ms, outcome))
        tasks.append((input_index, child_id, task))

    successes = []
    failed_child = None
    cancelled = []

    for task in asyncio.as_completed([task for _, _, task in tasks]):
        try:
            input_index, child_id = await task
            successes.append(child_id)
        except RuntimeError as e:
            input_index, child_id = e.args
            failed_child = child_id
            break

    for input_index, child_id, task in tasks:
        if child_id not in successes + [failed_child]:
            cancelled.append(child_id)
            task.cancel()

    await asyncio.gather(*(task for _, _, task in tasks), return_exceptions=True)
    for child_id in successes:
        print(f"OK {child_id}")
    print(f"FAIL {failed_child}")
    for child_id in cancelled:
        print(f"CANCEL {child_id}")



if __name__ == "__main__":
    asyncio.run(main())