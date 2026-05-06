import sys
import requests

TIMEOUT = 10

def has_header(response, header_name):
    return header_name in response.headers

def fetch_once(url):
    return requests.get(url, timeout=TIMEOUT)

def verify_resource(
    label, raw_urls, required_header, max_attempts
):
    urls = raw_urls.split(',')
    last_status = 0
    attempts = 0
    for url in urls[:max_attempts]:
        response = fetch_once(url)
        attempts += 1
        last_status = response.status_code
        if has_header(response, required_header):
            return f"{label} OK {attempts} {last_status}"
    return f"{label} STALE {attempts} {last_status}"

def read_rows(count):
    rows = []
    for _ in range(count):
        parts = sys.stdin.readline().split()
        label, raw_urls, required_header = parts
        rows.append((label, raw_urls, required_header))
    return rows

def main():
    parts = sys.stdin.readline().split()
    max_attempts, n = map(int, parts)
    rows = read_rows(n)
    for label, raw_urls, required_header in rows:
        print(verify_resource(
            label, raw_urls, required_header, max_attempts
        ))

main()