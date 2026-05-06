import sys
import requests
TIMEOUT = 10
def download_report(source_url):
    response = requests.get(source_url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()
def parse_records(raw_document):
    records = raw_document.get("records", [])
    clean = []
    for record in records:
        if record.get("active"):
            clean.append(record)
    return clean
def store_records(report_id, records):
    if not records:
        return f"{report_id} EMPTY 0"
    stored_count = len(records)
    return f"{report_id} STORED {stored_count}"
def process_report(report_id, source_url):
    document = download_report(source_url)
    records = parse_records(document)
    return store_records(report_id, records)
def read_rows(count):
    rows = []
    for _ in range(count):
        report_id, source_url = (
            sys.stdin.readline().split()
        )
        rows.append((report_id, source_url))
    return rows
def main():
    parts = sys.stdin.readline().split()
    parse_limit, store_limit, n = map(int, parts)
    rows = read_rows(n)
    output = []
    for report_id, source_url in rows:
        output.append(
            process_report(report_id, source_url)
        )
    for line in output:
        print(line)
main()