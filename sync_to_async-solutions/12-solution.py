import asyncio
import requests
import sys



TIMEOUT = 10



def should_stop(status_code):
    return status_code < 500



def split_urls(raw_urls):
    return raw_urls.split(',')



async def fetch_once_wrapper(url):
    return await asyncio.to_thread(fetch_once, url)
def fetch_once(url):
    response = requests.get(url, timeout=TIMEOUT)
    retu
    
    rn response.status_code

async def fetch_with_retries(label, urls, max_attempts):
    last_status = None
    attempts_used = 0
    for attempt_index, url in enumerate(
        urls[:max_attempts], start=1
    ):
        last_status = await fetch_once_wrapper(url)
        attempts_used = attempt_index
        if should_stop(last_status):
            return (
                f"{label} OK {attempts_used} {last_status}"
            )
    return f"{label} FAIL {attempts_used} {last_status}"



def read_rows(count):
    rows = []
    for _ in range(count):
        label, raw_urls = sys.stdin.readline().split()
        rows.append((label, raw_urls))
    return rows



async def main():
    parts = sys.stdin.readline().split()
    max_attempts, n = map(int, parts)
    rows = read_rows(n)
    tasks = []
    for label, raw_urls in rows:
        urls = split_urls(raw_urls)
        task = asyncio.create_task(fetch_with_retries(label, urls, max_attempts))
        tasks.append(task)

    output = await asyncio.gather(*tasks)
    for line in output:
        print(line)



asyncio.run(main())