import asyncio
import aiohttp
import time

url = "https://api.flexobo.com/api/search-cargo?from_location_id=2256&per_page=20"

headers = {
    "accept-currency": "UZS",
    "accept-language": "ru",
}

async def fetch(url):
    async with aiohttp.ClientSession() as session: 
        async with session.get(url, headers=headers) as response:
            return await response.text()

requestsCount = 50

async def main():
    tasks = [fetch(url) for _ in range(requestsCount)] 
    responses = await asyncio.gather(*tasks)
    return responses

start_time = time.time()
asyncio.run(main())
print("Время выполнения:", round(time.time() - start_time, 3), "секунд на", requestsCount, "запросов")
