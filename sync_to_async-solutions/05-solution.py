import asyncio
import requests
import sys



TIMEOUT = 10
HEADERS = {"User-Agent": "sync-to-async-practice"}



def normalize_type(value):
    if not value:
        return "UNKNOWN"
    return value.split(";")[0]



async def check_head_async(semaphore, label, url):
    async with semaphore:
        return await asyncio.to_thread(check_head, label, url)



def check_head(label, url):
    response = requests.head(
        url,
        headers=HEADERS,
        timeout=TIMEOUT,
        allow_redirects=True,
    )
    response.raise_for_status()
    content_type = normalize_type(
        response.headers.get("Content-Type")
    )
    return (
        f"{label} {response.status_code} {content_type}"
    )



def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows



async def collect(rows, limit):
    semaphore = asyncio.Semaphore(limit)
    output = []
    for label, url in rows:
        task = asyncio.create_task(check_head_async(semaphore, label, url))
        output.append(task)
    return await asyncio.gather(*output)



async def main():
    limit, n = map(int, sys.stdin.readline().split())
    rows = read_rows(n)
    for line in await collect(rows, limit):
        print(line)



asyncio.run(main())