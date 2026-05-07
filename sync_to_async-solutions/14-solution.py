import asyncio
import requests
import sys



TIMEOUT = 10
PAGE_SIZE = 10



def build_url(base_url, page_number):
    return (
        f"{base_url}?_page={page_number}"
        f"&_limit={PAGE_SIZE}"
    )



async def fetch_page_wrapper(base_url, page_number):
    return await asyncio.to_thread(fetch_page, base_url, page_number)
def fetch_page(base_url, page_number):
    url = build_url(base_url, page_number)
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()



async def load_collection(label, base_url, page_count):
    total_items = 0
    pages_read = 0
    for page_number in range(1, page_count + 1):
        data = await fetch_page_wrapper(base_url, page_number)
        pages_read += 1
        total_items += len(data)
        if not data:
            break
    return f"{label} {total_items} {pages_read}"



def read_rows(count):
    rows = []
    for _ in range(count):
        parts = sys.stdin.readline().split()
        label, base_url, page_count = parts
        rows.append((label, base_url, int(page_count)))
    return rows



async def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    tasks = []
    for label, base_url, page_count in rows:
        task = asyncio.create_task(load_collection(label, base_url, page_count))
        tasks.append(task)

    results = await asyncio.gather(*tasks) 
    for result in results:
        print(result)



asyncio.run(main())