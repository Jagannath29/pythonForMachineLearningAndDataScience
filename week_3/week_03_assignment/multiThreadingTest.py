from concurrent.futures import ThreadPoolExecutor
import requests
from timer import timer


url = 'https://httpbin.org/uuid'
def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

@timer(1,1)
def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session]* 100, [url]*100)
            executor.shutdown(wait=True)

