import asyncio
import time
from typing import List
import asyncio

import httpx


async def append_two_values(lst, value1, value2):
    lst.append(value1)
    await asyncio.sleep(0.5)
    lst.append(value2)


lst = []


async def main():
    await asyncio.gather(
        append_two_values(lst, 1, 4),
        append_two_values(lst, 3, 6),
        append_two_values(lst, 2, 5),
    )


asyncio.run(main())


with open("scrappers/top15websites.txt", "r", encoding="utf-8") as catalogue:
    links = [link.strip() for link in catalogue.readlines()]


async def read_links(web_links: List[str]):
    async with httpx.AsyncClient() as web_client:
        tasks = (web_client.get(link) for link in web_links)
        reqs = await asyncio.gather(*tasks)
    [print(req.text) for req in reqs]


start = time.perf_counter()
asyncio.run(read_links(links))
print(f"{(time.perf_counter() - start):.2f}'s")
