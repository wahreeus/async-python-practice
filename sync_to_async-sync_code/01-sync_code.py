import sys
import requests

DEFAULT_HEADERS = {
    "User-Agent": "sync-to-async-practice",
    "Accept": (
        "text/html,application/json;q=0.9,"
        "*/*;q=0.8"
    ),
}
REQUEST_TIMEOUT = 10

def build_headers():
    return dict(DEFAULT_HEADERS)

def fetch_page(label, url):
    headers = build_headers()
    response = requests.get(
        url,
        headers=headers,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    size = len(response.content)
    return label, response.status_code, size

def format_result(result):
    label, status_code, size = result
    return f"{label} {status_code} {size}"

def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows

def collect_results(rows):
    results = []
    for label, url in rows:
        results.append(fetch_page(label, url))
    return results

def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    results = collect_results(rows)
    for result in results:
        print(format_result(result))

main()