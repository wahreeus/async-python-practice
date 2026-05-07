import sys
import requests

TIMEOUT = 10


def split_urls(raw_urls):
    return raw_urls.split(',')


def probe_replica(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code >= 500:
            return None
        return response.status_code, url
    except requests.RequestException:
        return None


def check_service(service_id, raw_urls):
    urls = split_urls(raw_urls)
    for url in urls:
        result = probe_replica(url)
        if result is not None:
            status_code, chosen_url = result
            return (
                f"{service_id} OK {status_code} {chosen_url}"
            )
    return f"{service_id} FAIL"


def read_rows(count):
    rows = []
    for _ in range(count):
        service_id, raw_urls = sys.stdin.readline().split()
        rows.append((service_id, raw_urls))
    return rows


def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    output = []
    for service_id, raw_urls in rows:
        output.append(check_service(service_id, raw_urls))
    for line in output:
        print(line)


main()
