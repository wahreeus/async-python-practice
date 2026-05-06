import csv
import io
import sys
import requests
TIMEOUT = 10
def count_data_rows(csv_text):
    reader = csv.reader(io.StringIO(csv_text))
    rows = list(reader)
    if not rows:
        return 0
    return max(0, len(rows) - 1)
def fetch_csv(label, url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    row_count = count_data_rows(response.text)
    return f"{label} {row_count}"
def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows
def run(rows):
    lines = []
    for label, url in rows:
        lines.append(fetch_csv(label, url))
    return lines
def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    for line in run(rows):
        print(line)
main()