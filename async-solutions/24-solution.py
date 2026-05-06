import asyncio
import sys



class AsyncCache:
    def __init__(self, request_data: dict[str, tuple[str, str]]) -> None:
        self.request_data = request_data
        self.values = {}
        self.currently_fetching = {}
        self.fetches = 0
        self.lock = asyncio.Lock()

    async def get(self, key: str) -> str:
        async with self.lock:
            if key in self.values:
                return self.values[key]
            if key not in self.currently_fetching:
                delay_ms, value = self.request_data[key]
                self.currently_fetching[key] = asyncio.create_task(fetch_value(delay_ms, value))
                self.fetches += 1
            task = self.currently_fetching[key]

        value = await task
        async with self.lock:
            self.values[key] = value
            self.currently_fetching.pop(key, None)
        return value



async def fetch_value(delay_ms: str, value: str) -> str:
    delay_s = float(delay_ms)/1000
    await asyncio.sleep(delay_s)
    return value



async def handle_request(cache: AsyncCache, key: str) -> tuple[str, str]:
    value = await cache.get(key)
    return key, value



async def main() -> None:
    n = int(sys.stdin.readline().strip())
    requests = []
    request_data = {}
    for _ in range(n):
        key, delay_ms, value = sys.stdin.readline().strip().split()
        requests.append(key)
        if key not in request_data:
            request_data[key] = (delay_ms, value)
    cache = AsyncCache(request_data)

    tasks = []
    for key in requests:
        task = asyncio.create_task(handle_request(cache, key))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    for key, value in results:
        print(f"{key} {value}")
    print(f"FETCHES {cache.fetches}")



if __name__ == "__main__":
    asyncio.run(main())