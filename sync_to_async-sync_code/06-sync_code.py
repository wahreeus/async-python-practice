import sys
import requests

BASE_URL = "https://pypi.org/pypi/{}/json"
TIMEOUT = 10

def build_url(package_name):
    return BASE_URL.format(package_name)

def extract_name(data):
    info = data.get("info", {})
    return info.get("name", "UNKNOWN")

def load_package(package_name):
    url = build_url(package_name)
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    canonical_name = extract_name(data)
    return f"{package_name} {canonical_name}"

def read_package_names(count):
    package_names = []
    for _ in range(count):
        package_names.append(sys.stdin.readline().strip())
    return package_names

def collect_results(package_names):
    results = []
    for package_name in package_names:
        result = load_package(package_name)
        results.append(result)
    return results

def main():
    limit, n = map(int, sys.stdin.readline().split())
    package_names = read_package_names(n)
    results = collect_results(package_names)
    for line in results:
        print(line)

main()