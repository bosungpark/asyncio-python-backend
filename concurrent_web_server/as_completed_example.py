import asyncio

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session,"http://www.example.com",1),
            fetch_status(session, "http://www.example.com", 10),
            fetch_status(session, "http://www.example.com", 10)
        ]
        # -> 완료된 순으로 iter 반환: 반복문에 await 걸어도 상관이 없다!
        for fin_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                print(await fin_task)
            except asyncio.TimeoutError:
                print("time out!")
        # -> 예외가 발생하더라도, 태스크는 백그라운드에서 돌게 된다.
        for t in asyncio.tasks.all_tasks():
            print(t)

asyncio.run(main())