import asyncio
import logging
import warnings

from aiohttp import ClientSession

from util import async_timed, fetch_status

warnings.filterwarnings("ignore", category=DeprecationWarning)

@async_timed()
async def main():
    async with ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session,"http://www.example.com")),
            asyncio.create_task(fetch_status(session, "bad request!")),
            asyncio.create_task(fetch_status(session, "http://www.example.com", 10)),
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED, timeout=1) # FIRST_EXCEPTION, FIRST_COMPLETED,

            for done_task in done:
                # result = await done_task
                # print(result)
                if done_task.exception() is None:
                    print(done_task.result())
                    print("DONE",len(done))
                    print("PENDING",len(pending))
                else:
                    logging.error("bad req!", exc_info=done_task.exception())
        # if loop done and exist tasks
        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())