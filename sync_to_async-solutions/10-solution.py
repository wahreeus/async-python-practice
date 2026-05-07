import asyncio
import hashlib
import requests
import sys



TIMEOUT = 10



def digest_prefix(raw_bytes):
    digest = hashlib.sha256(raw_bytes).hexdigest()
    return digest[:12]



async def download_wrapper(label, url):
    return await asyncio.to_thread(download, label, url)
def download(label, url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    raw_bytes = response.content
    size = len(raw_bytes)
    prefix = digest_prefix(raw_bytes)
    return f"{label} {size} {prefix}"



def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows



async def build_report(rows):
    tasks = []
    for label, url in rows:
        task = asyncio.create_task(download_wrapper(label, url))
        tasks.append(task)
    return await asyncio.gather(*tasks)



async def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    report = await build_report(rows)
    for line in report:
        print(line)



asyncio.run(main())