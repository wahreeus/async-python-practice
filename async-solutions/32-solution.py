import asyncio
import sys



async def process_task(task_id, duration_ms):
    duration_s = float(duration_ms)/1000
    await asyncio.sleep(duration_s)
    return task_id



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    tasks = set()
    dependenices = {}
    for _ in range(n):
        task_id, duration_ms, deps = sys.stdin.readline().strip().split()
        duration_ms = int(duration_ms)
        if deps != "-":
            deps = set(deps.split(","))
            dependenices[task_id] = (deps, duration_ms)
        else:
            task = asyncio.create_task(process_task(task_id, duration_ms))
            tasks.add(task)

    installed = set()
    while tasks:
        finished_tasks, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for finished_task in finished_tasks:
            task_id = await finished_task
            installed.add(task_id)
            print(task_id)
        for task_id, (deps, duration_ms) in list(dependenices.items()):
            if deps <= installed:
                task = asyncio.create_task(process_task(task_id, duration_ms))
                tasks.add(task)
                del dependenices[task_id]



if __name__ == "__main__":
    asyncio.run(main())