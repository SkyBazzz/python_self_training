import asyncio


async def append_two_values(lst, value1, value2):
    lst.append(value1)
    await asyncio.sleep(0.5)
    lst.append(value2)


lst = []


async def main():
    await asyncio.gather(append_two_values(lst, 1, 4), append_two_values(lst, 3, 6), append_two_values(lst, 2, 5))


asyncio.run(main())
