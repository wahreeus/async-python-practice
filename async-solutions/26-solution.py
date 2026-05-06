import asyncio
import sys



async def process_job(job_id: str, deadline_ms: int, steps: list[int]) -> str:
    elapsed_ms = 0
    completed = 0
    for step_ms in steps:
        if elapsed_ms + step_ms > deadline_ms:
            return f"{job_id} TIMEOUT {completed}"
        await asyncio.sleep(step_ms / 1000)
        elapsed_ms += step_ms
        completed += 1
    return f"{job_id} DONE {completed}"



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = []
    for _ in range(n):
        job_id, deadline_ms, steps_text = sys.stdin.readline().strip().split()
        deadline_ms = int(deadline_ms)
        steps = [int(x) for x in steps_text.split(",")]
        task = asyncio.create_task(process_job(job_id, deadline_ms, steps))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    for line in results:
        print(line)



if __name__ == "__main__":
    asyncio.run(main())