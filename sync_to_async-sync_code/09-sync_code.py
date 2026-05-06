import sys
from urllib.request import Request, urlopen
TIMEOUT = 10
USER_AGENT = "sync-to-async-practice"
def build_request(url):
    return Request(
        url, headers={"User-Agent": USER_AGENT}
    )
def download_text(url):
    request = build_request(url)
    with urlopen(request, timeout=TIMEOUT) as response:
        raw_bytes = response.read()
    return raw_bytes.decode("utf-8", "replace")
def inspect_document(label, url):
    text = download_text(url)
    if "User-agent" in text:
        return f"{label} OK"
    return f"{label} MISSING"
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
        results.append(inspect_document(label, url))
    for line in results:
        print(line)
main()