import asyncio
import sys



async def process_host(requests: list[tuple[int, str, int]]) -> list[tuple[int, int, str]]:
    results: list[tuple[int, int, str]] = []
    elapsed_ms = 0
    for input_index, request_id, delay_ms in requests:
        await asyncio.sleep(delay_ms / 1000)
        elapsed_ms += delay_ms
        results.append((elapsed_ms, input_index, request_id))
    return results



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    per_host = {}
    for input_index in range(n):
        host, request_id, delay_ms = sys.stdin.readline().strip().split()
        process_data = (input_index, request_id, int(delay_ms))
        per_host.setdefault(host, []).append(process_data)

    tasks = []
    for process_data in per_host.values():
        task = asyncio.create_task(process_host(process_data))
        tasks.append(task)

    output = []
    for task in asyncio.as_completed(tasks):
        host_results = await task
        for result in host_results:
            output.append(result)

    output.sort(key=lambda item: (item[0], item[1]))
    for _, _, request_id in output:
        print(request_id)



if __name__ == "__main__":
    asyncio.run(main())