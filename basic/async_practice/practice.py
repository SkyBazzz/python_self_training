"""
https://www.youtube.com/watch?v=ftmdDlwMwwQ&ab_channel=mCoding
/robots.txt
"""

import asyncio
import time


async def do_work(job: str, delay: float = 1.0):
    print(f"Start doing {job}")
    await asyncio.sleep(delay)
    print(f"Finishing {job}")


async def main():
    start = time.perf_counter()

    todo = ["waiting package", "wash dishes", "play guitar"]

    tasks = [do_work(job) for job in todo]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(results)

    tasks = [asyncio.create_task(do_work(job)) for job in todo]
    done, pending = await asyncio.wait(tasks)
    for result in done:
        print(result)
    for result in pending:
        print(result)
    finish = time.perf_counter()
    print(f"It took: {finish - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
