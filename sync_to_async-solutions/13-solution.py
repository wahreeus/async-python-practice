import asyncio
import sys
from urllib.request import Request, urlopen



TIMEOUT = 10
USER_AGENT = "sync-to-async-practice"



def build_request(url):
    return Request(
        url, headers={"User-Agent": USER_AGENT}
    )



async def download_text_wrapper(url):
    return await asyncio.to_thread(download_text,url)
def download_text(url):
    request = build_request(url)
    with urlopen(request, timeout=TIMEOUT) as response:
        raw_bytes = response.read()
    return raw_bytes.decode("utf-8", "replace")



async def inspect_document(label, url):
    text = await download_text_wrapper(url)
    if "User-agent" in text:
        return f"{label} OK"
    return f"{label} MISSING"



def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows



async def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    tasks = []
    for label, url in rows:
        task = asyncio.create_task(inspect_document(label, url))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    for line in results:
        print(line)



asyncio.run(main())