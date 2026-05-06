import hashlib
import sys
import requests
TIMEOUT = 10
def digest_prefix(raw_bytes):
    digest = hashlib.sha256(raw_bytes).hexdigest()
    return digest[:12]
def download(label, url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    raw_bytes = response.content
    size = len(raw_bytes)
    prefix = digest_prefix(raw_bytes)
    return f"{label} {size} {prefix}"
def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows
def build_report(rows):
    lines = []
    for label, url in rows:
        lines.append(download(label, url))
    return lines
def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    report = build_report(rows)
    for line in report:
        print(line)
main()