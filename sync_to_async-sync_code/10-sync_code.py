import sys
import requests
TIMEOUT = 10
fetches = 0
cache = {}
def fetch_status(url):
    global fetches
    fetches += 1
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.status_code
def resolve_status(url):
    if url not in cache:
        cache[url] = fetch_status(url)
    return cache[url]
def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows
def build_output(rows):
    lines = []
    for label, url in rows:
        status_code = resolve_status(url)
        lines.append(f"{label} {status_code}")
    return lines
def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    output = build_output(rows)
    for line in output:
        print(line)
    print("FETCHES", fetches)
main()