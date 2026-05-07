import asyncio
import requests
import sys



DEFAULT_HEADERS = {"User-Agent": "sync-to-async-practice"}



def build_request(url, timeout_s):
    return {
        "url": url,
        "headers": DEFAULT_HEADERS,
        "timeout": timeout_s,
    }




async def run_check_wrapper(label, url, timeout_s):
    return await asyncio.to_thread(run_check,label, url, timeout_s)
def run_check(label, url, timeout_s):
    try:
        request_kwargs = build_request(url, timeout_s)
        response = requests.get(**request_kwargs)
        response.raise_for_status()
        return f"{label} OK"
    except requests.Timeout:
        return f"{label} TIMEOUT"



def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows



async def main():
    timeout_s, n = sys.stdin.readline().split()
    timeout_s = float(timeout_s)
    n = int(n)
    rows = read_rows(n)
    tasks = []
    for label, url in rows:
        task = asyncio.create_task(run_check_wrapper(label, url, timeout_s))
        tasks.append(task)
    for result in await asyncio.gather(*tasks):
        print(result)



asyncio.run(main())