import sys
import requests
API_ROOT = "https://api.github.com/repos/{}/{}"
HEADERS = {
    "User-Agent": "sync-to-async-practice",
    "Accept": "application/vnd.github+json",
}
TIMEOUT = 10
def build_url(owner, repo):
    return API_ROOT.format(owner, repo)
def normalize_field(value):
    if value is None:
        return "None"
    return str(value)
def format_repository(data):
    full_name = normalize_field(data.get("full_name"))
    language = normalize_field(data.get("language"))
    branch = normalize_field(data.get("default_branch"))
    return f"{full_name} {language} {branch}"
def load_repository(owner, repo):
    url = build_url(owner, repo)
    response = requests.get(
        url, headers=HEADERS, timeout=TIMEOUT
    )
    response.raise_for_status()
    data = response.json()
    return format_repository(data)
def read_rows(count):
    rows = []
    for _ in range(count):
        owner, repo = sys.stdin.readline().split()
        rows.append((owner, repo))
    return rows
def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    output = []
    for owner, repo in rows:
        output.append(load_repository(owner, repo))
    for line in output:
        print(line)
main()