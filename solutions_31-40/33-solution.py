import asyncio
import sys



async def process_task(job_id, delay_ms, outcome):
    delay_s = float(delay_ms) / 1000
    await asyncio.sleep(delay_s)
    if outcome == "OK":
        return job_id
    else:
        raise RuntimeError(job_id)



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    coroutines = []
    for _ in range(n):
        job_id, delay_ms, outcome = sys.stdin.readline().strip().split()
        coroutine = process_task(job_id, delay_ms, outcome)
        coroutines.append(coroutine)

    tasks = []
    try:
        async with asyncio.TaskGroup() as tg:
            for coroutine in coroutines:
                tasks.append(tg.create_task(coroutine))
    except* RuntimeError:
        pass

    successes = []
    failed = ""
    cancelled = 0
    for task in tasks:
        if task.cancelled():
            cancelled += 1
        elif task.exception() is not None:
            failed = task.exception().args[0]
        else:
            successes.append(task.result())

    for success in successes:
        print(f"DONE {success}")
    if failed:
        print(f"FAILED {failed}")
    print(f"CANCELLED {cancelled}")



if __name__ == "__main__":
    asyncio.run(main())