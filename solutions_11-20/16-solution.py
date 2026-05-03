import asyncio
import sys



async def process_task(job_id: str, index: int, delay_ms: int, cancel_after_ms: int) -> tuple[str, int, str]:
    delay_s = float(delay_ms)/1000
    cancel_after_s = float(cancel_after_ms)/1000
    if delay_ms == cancel_after_ms:
        await asyncio.sleep(delay_s)
        return job_id, index, "DONE"
        
    try:
        await asyncio.wait_for(asyncio.sleep(delay_s), cancel_after_s)
        return job_id, index, "DONE"
    except asyncio.TimeoutError:
        return job_id, index, "CANCELLED"



async def main() -> None:
    cancel_after_ms, n = map(int, sys.stdin.readline().strip().split())
    tasks: list[asyncio.Task[tuple[str, int, str]]] = []
    for index in range(n):
        job_id, delay_ms = sys.stdin.readline().strip().split()
        delay_ms = int(delay_ms)
        task = asyncio.create_task(process_task(job_id, index, delay_ms, cancel_after_ms))
        tasks.append(task)

    done: list[str] = []
    cancelled: list[tuple[str, int]] = []
    for task in asyncio.as_completed(tasks):
        job_id, index, outcome = await task
        if outcome == "DONE":
            done.append(job_id)
        else:
            cancelled.append((job_id, index))

    cancelled.sort(key=lambda item : item[1])
    for job_id in done:
        print(f"DONE {job_id}")
    for job_id, _ in cancelled:
        print(f"CANCELLED {job_id}")



if __name__ == "__main__":
    asyncio.run(main())