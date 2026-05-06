import sys
import requests
from collections import defaultdict
TIMEOUT = 10
def fetch_status(label, url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return label, response.status_code
def read_rows(count):
    rows = []
    for index in range(count):
        origin, label, url = sys.stdin.readline().split()
        rows.append((index, origin, label, url))
    return rows
def group_by_origin(rows):
    groups = defaultdict(list)
    for row in rows:
        _, origin, _, _ = row
        groups[origin].append(row)
    return groups
def run_group(rows):
    results = []
    for _, origin, label, url in rows:
        results.append(fetch_status(label, url))
    return results
def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    groups = group_by_origin(rows)
    output = []
    for origin in sorted(groups):
        output.extend(run_group(groups[origin]))
    for label, status_code in output:
        print(f"{label} {status_code}")
main()