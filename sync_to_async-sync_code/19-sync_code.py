import sys
import requests

TIMEOUT = 10


def parse_log_levels(text):
    warnings = 0
    errors = 0
    for token in text.split():
        level = token.strip().upper()
        if level == "WARN":
            warnings += 1
        elif level == "ERROR":
            errors += 1
    return warnings, errors


def download_text(url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.text


def summarize(label, url):
    text = download_text(url)
    warnings, errors = parse_log_levels(text)
    return f"{label} {warnings} {errors}"


def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows


def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    output = []
    for label, url in rows:
        output.append(summarize(label, url))
    for line in output:
        print(line)


main()
