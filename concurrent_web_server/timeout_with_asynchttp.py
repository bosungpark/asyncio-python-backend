"""
expected:

asyncio.exceptions.TimeoutError
"""
import asyncio

import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:

    ten_millis = aiohttp.ClientTimeout(total=.01)
    async with session.get(url, timeout=ten_millis) as result: # default timeout: 5 min
        return result.status


async def main():
    session_timeout=aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        url= "http://www.example1.com"
        status = await fetch_status(session,url)
        # print(f"status for {url} was {status}")

asyncio.run(main())