import asyncio

from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str, delay: int) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status