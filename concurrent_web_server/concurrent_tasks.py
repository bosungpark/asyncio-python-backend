import asyncio

from util import delay, async_timed


@async_timed()
async def main()-> None:
    # case 1 -> fine approach
    # task_one=asyncio.create_task(delay(3))
    # task_two = asyncio.create_task(delay(3))
    # task_three = asyncio.create_task(delay(3))
    #
    # await task_one
    # await task_two
    # await task_three

    # case 2 -> bad approach
    # [await asyncio.create_task(delay(sec)) for sec in [3,3,3]]

    # case 3 -> make case 2 better
    tasks = [asyncio.create_task(delay(sec)) for sec in [3, 3, 3]]
    [await t for t in tasks]

asyncio.run(main())