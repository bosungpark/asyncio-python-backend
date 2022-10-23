import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

import requests

from util import async_timed


counter_lock = Lock()

def get_status_code(url: str) -> int:
    global counter

    res = requests.get(url)
    with counter_lock:
        counter+=1
    return res.status_code

async def reporter(request_count: int):
    while counter< request_count:
        print(f"fin {counter}/{request_count} req")
        await asyncio.sleep(.5)

@async_timed()
async def main():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        request_count = 200
        urls = ["https://www.example.com" for _ in range(request_count)]
        reporter_task = asyncio.create_task(reporter(request_count))
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results =await asyncio.gather(*tasks)
        await reporter_task
        print(results)

asyncio.run(main())
