import sys
import requests

TIMEOUT = 10


def download_document(source_url):
    response = requests.get(source_url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def parse_events(raw_document):
    args = raw_document.get("args", {})
    count = int(args.get("count", "0"))
    active = args.get("active", "false").lower()
    if active != "true":
        return []
    events = []
    for index in range(count):
        events.append({"index": index})
    return events


def store_events(batch_id, events):
    if not events:
        return f"{batch_id} EMPTY 0"
    stored_count = len(events)
    return f"{batch_id} STORED {stored_count}"


def process_batch(batch_id, source_url):
    document = download_document(source_url)
    events = parse_events(document)
    return store_events(batch_id, events)


def read_rows(count):
    rows = []
    for _ in range(count):
        batch_id, source_url = sys.stdin.readline().split()
        rows.append((batch_id, source_url))
    return rows


def main():
    parts = sys.stdin.readline().split()
    parse_limit, store_limit, n = map(int, parts)
    rows = read_rows(n)
    output = []
    for batch_id, source_url in rows:
        output.append(process_batch(batch_id, source_url))
    for line in output:
        print(line)


main()
