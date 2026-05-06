import sys
import requests

TIMEOUT = 10

def parse_numbers(text):
    values = []
    for token in text.split():
        if token.lstrip('-').isdigit():
            values.append(int(token))
    return values

def download_text(url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.text

def summarize(label, url):
    text = download_text(url)
    values = parse_numbers(text)
    return f"{label} {len(values)} {sum(values)}"

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