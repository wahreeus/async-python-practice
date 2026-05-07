import sys
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/photos"
TIMEOUT = 10


def build_url(album_id):
    return f"{BASE_URL}?albumId={album_id}"


def count_photos(data):
    return len(data)


def fetch_album(label, album_id):
    url = build_url(album_id)
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    photo_count = count_photos(data)
    return f"{label} {photo_count}"


def read_rows(count):
    rows = []
    for _ in range(count):
        label, album_id = sys.stdin.readline().split()
        rows.append((label, album_id))
    return rows


def run(rows):
    lines = []
    for label, album_id in rows:
        lines.append(fetch_album(label, album_id))
    return lines


def main():
    n = int(sys.stdin.readline())
    rows = read_rows(n)
    for line in run(rows):
        print(line)


main()
