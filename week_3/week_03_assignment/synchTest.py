import requests

from timer import timer


url = 'https://httpbin.org/uuid'

def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@timer(1,1)
def main():
    with requests.Session() as session:
        for _ in range(100):
            print(fetch(session, url))