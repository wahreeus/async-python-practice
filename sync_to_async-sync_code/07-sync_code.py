import sys
import requests
DEFAULT_HEADERS = {"User-Agent": "sync-to-async-practice"}
def build_request(url, timeout_s):
    return {
        "url": url,
        "headers": DEFAULT_HEADERS,
        "timeout": timeout_s,
    }
def run_check(label, url, timeout_s):
    try:
        request_kwargs = build_request(url, timeout_s)
        response = requests.get(**request_kwargs)
        response.raise_for_status()
        return f"{label} OK"
    except requests.Timeout:
        return f"{label} TIMEOUT"
def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows
def main():
    timeout_s, n = sys.stdin.readline().split()
    timeout_s = float(timeout_s)
    n = int(n)
    rows = read_rows(n)
    lines = []
    for label, url in rows:
        lines.append(run_check(label, url, timeout_s))
    for line in lines:
        print(line)
main()