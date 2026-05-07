import asyncio
import requests
import sys



HEADERS = {"User-Agent": "sync-to-async-practice"}
TIMEOUT = 10



def build_request(url):
    return {
        "url": url,
        "headers": HEADERS,
        "timeout": TIMEOUT,
    }



async def fetch_status_wrapper(label, url):
    label, status_code = await asyncio.to_thread(fetch_status, label, url)
    return label, status_code



def fetch_status(label, url):
    request_kwargs = build_request(url)
    response = requests.get(**request_kwargs)
    response.raise_for_status()
    return label, response.status_code



def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows



async def sequential_download(rows):
    tasks = []
    for label, url in rows:
        task = asyncio.create_task(fetch_status_wrapper(label, url))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        label, status_code = await task
        print(f"DONE {label} {status_code}")



async def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    await sequential_download(rows)



asyncio.run(main())