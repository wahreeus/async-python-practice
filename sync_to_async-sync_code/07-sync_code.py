import re
import sys
import requests

TITLE_RE = re.compile(
    r"<title>(.*?)</title>", re.I | re.S
)
TIMEOUT = 10

def normalize_title(text):
    return " ".join(text.split())

def extract_title(html_text):
    match = TITLE_RE.search(html_text)
    if not match:
        return "NO_TITLE"
    title = match.group(1)
    return normalize_title(title)

def fetch_title(label, url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    title = extract_title(response.text)
    return f"{label} {title}"

def read_rows(count):
    rows = []
    for _ in range(count):
        label, url = sys.stdin.readline().split()
        rows.append((label, url))
    return rows

def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    results = []
    for label, url in rows:
        results.append(fetch_title(label, url))
    for line in results:
        print(line)

main()