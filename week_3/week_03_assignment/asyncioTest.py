import aiohttp
import asyncio

from timer import timer


url = 'https://httpbin.org/uuid'

async def fetch(session, url):
    async with session.get(url) as response:
       json_response = await response.json()
       print(json_response['uuid'])


async def main():
    async with aiohttp.ClientSession() as session:
        task = [fetch(session, url) for _ in range(100)]
        await asyncio.gather(*task)
@timer(1,1)      
def func():
    asyncio.run(main())
    