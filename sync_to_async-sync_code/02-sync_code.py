import sys
import requests
HEADERS = {"User-Agent": "sync-to-async-practice"}
TIMEOUT = 10
def build_request(url):
    return {
        "url": url,
        "headers": HEADERS,
        "timeout": TIMEOUT,
    }
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
def sequential_download(rows):
    completed = []
    for label, url in rows:
        result = fetch_status(label, url)
        completed.append(result)
    return completed
def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    completed = sequential_download(rows)
    for label, status_code in completed:
        print(f"DONE {label} {status_code}")
main()