import requests
from program_timer import timer
from multiprocessing.pool import Pool


url = 'https://httpbin.org/uuid'

def fetch_uuid(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])
        
# @timer(1,1)
def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch_uuid, [(session, url) for _ in range(100)])
            
            
if __name__ == "__main__":
    main()





