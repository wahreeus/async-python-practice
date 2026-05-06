import sys
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users/{}"
TIMEOUT = 10

def build_url(record_id):
    return BASE_URL.format(record_id)

def parse_record(record_id, data):
    name = data["name"]
    username = data["username"]
    return f"{record_id} {name} {username}"

def load_record(record_id):
    url = build_url(record_id)
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    return parse_record(record_id, data)

def read_record_ids(count):
    record_ids = []
    for _ in range(count):
        record_ids.append(sys.stdin.readline().strip())
    return record_ids

def collect_lines(record_ids):
    results = []
    for record_id in record_ids:
        line = load_record(record_id)
        results.append(line)
    return results

def main():
    limit, n = map(int, sys.stdin.readline().split())
    record_ids = read_record_ids(n)
    results = collect_lines(record_ids)
    for line in results:
        print(line)

main()