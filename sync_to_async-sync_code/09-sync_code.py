import sys
import requests

TIMEOUT = 10

def read_rows(count):
    rows = []
    for _ in range(count):
        label, url, field = sys.stdin.readline().split()
        rows.append((label, url, field))
    return rows

def stringify(value):
    if value is None:
        return "MISSING"
    return str(value)

def extract_field(data, field):
    if field not in data:
        return "MISSING"
    return stringify(data.get(field))

def fetch_json(label, url, field):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    value = extract_field(data, field)
    return f"{label} {value}"

def run_all(rows):
    output = []
    for label, url, field in rows:
        output.append(fetch_json(label, url, field))
    return output

def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    for line in run_all(rows):
        print(line)

main()