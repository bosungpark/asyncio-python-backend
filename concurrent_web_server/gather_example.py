import asyncio

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ["http://www.example.com", "http_raise_exception"]
        req = [fetch_status(session, url) for url in urls]
        # return val in order, and show exception after loop and never throw exception after loop finished
        # -> [200, < InvalidURL http_raise_exception >]
        results = await asyncio.gather(*req, return_exceptions=True)

        exceptions = [r for r in results if isinstance(r, Exception)]
        status_codes = [r for r in results if not isinstance(r, Exception)]
        print("exceptions=",exceptions)
        print("status_codes=", status_codes)

asyncio.run(main())