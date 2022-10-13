from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status