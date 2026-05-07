import asyncio
import requests
import sys

TIMEOUT = 10
HEADERS = {
    "User-Agent": "sync-to-async-practice"
}

def read_rows(count):
    rows = []
    for _ in range(count):
        label, url, field = sys.stdin.readline().split()
        rows.append((label, url, field))
    return rows

def stringify(value):
    if value is None:
        return "MISSING"
    return str(value)

def extract_field(data, field):
    if field not in data:
        return "MISSING"
    return stringify(data.get(field))

async def fetch_json_wrapper(label, url, field):
    return await asyncio.to_thread(fetch_json, label, url, field)
def fetch_json(label, url, field):
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    value = extract_field(data, field)
    return f"{label} {value}"

async def run_all(rows):
    tasks = []
    for label, url, field in rows:
        task = asyncio.create_task(fetch_json_wrapper(label, url, field))
        tasks.append(task)
    return await asyncio.gather(*tasks)

async def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    for line in await run_all(rows):
        print(line)

asyncio.run(main())