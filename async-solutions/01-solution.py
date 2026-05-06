import asyncio
import sys



async def process_request(request_id: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return request_id



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    requests = []
    for _ in range(n):
        request_id, delay_ms = sys.stdin.readline().strip().split()
        delay_s = int(delay_ms) / 1000
        requests.append(process_request(request_id, delay_s))

    for request_id in await asyncio.gather(*requests):
        print(request_id)



if __name__ == "__main__":
    asyncio.run(main())