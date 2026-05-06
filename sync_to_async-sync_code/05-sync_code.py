import sys
import requests

TIMEOUT = 10
HEADERS = {"User-Agent": "sync-to-async-practice"}

def normalize_type(value):
    if not value:
        return "UNKNOWN"
    return value.split(";")[0]

def check_head(label, url):
    response = requests.head(
        url,
        headers=HEADERS,
        timeout=TIMEOUT,
        allow_redirects=True,
    )
    response.raise_for_status()
    content_type = normalize_type(
        response.headers.get("Content-Type")
    )
    return (
        f"{label} {response.status_code} {content_type}"
    )

def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows

def collect(rows):
    output = []
    for label, url in rows:
        output.append(check_head(label, url))
    return output

def main():
    limit, n = map(int, sys.stdin.readline().split())
    rows = read_rows(n)
    for line in collect(rows):
        print(line)

main()