import asyncio
import re
import requests
import sys



TITLE_RE = re.compile(
    r"<title>(.*?)</title>", re.I | re.S
)
TIMEOUT = 10
HEADERS = {
    "User-Agent": "sync-to-async-practice"
}



def normalize_title(text):
    return " ".join(text.split())



def extract_title(html_text):
    match = TITLE_RE.search(html_text)
    if not match:
        return "NO_TITLE"
    title = match.group(1)
    return normalize_title(title)



async def fetch_title_wrapper(label, url):
    return await asyncio.to_thread(fetch_title, label, url)
def fetch_title(label, url):
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    title = extract_title(response.text)
    return f"{label} {title}"



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
        task = asyncio.create_task(fetch_title_wrapper(label, url))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    for line in results:
        print(line)



asyncio.run(main())