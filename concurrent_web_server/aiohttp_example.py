"""
expected:

starting <function main at 0x10219dcf0> with args () {}
starting <function fetch_status at 0x100d58160> with args (<aiohttp.client.ClientSession object at 0x102126cb0>, 'http://www.example.com') {}
finished <function fetch_status at 0x100d58160> in 0.9863 second(s)
status for http://www.example.com was 200 # -> printed
finished <function main at 0x10219dcf0> in 0.9869 second(s)
"""
import asyncio

import aiohttp
from aiohttp import ClientSession

from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url= "http://www.example.com"
        status = await fetch_status(session,url)
        print(f"status for {url} was {status}")

asyncio.run(main())