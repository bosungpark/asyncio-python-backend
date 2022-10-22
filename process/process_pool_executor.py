import asyncio
import time
from asyncio import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import Process
from typing import List


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter< count_to:
        counter+=1
    end = time.time()
    print(f"fin cnting {count_to} in {end-start}")
    return counter

# FIXME: case1 -> iter 순서는 입력된 리스트에 제한된다.
# if __name__ == '__main__':
#     with ProcessPoolExecutor() as process_pool:
#         nums= [100000000,1,3,5,22]
        # for result in process_pool.map(count, nums):
        #     print(result)

async def main():
    with ProcessPoolExecutor() as process_pool:
        nums= [100000000,1,3,5,22]
        #case2
        loop: AbstractEventLoop = asyncio.get_running_loop()
        calls: List[partial[int]] = [partial(count, num) for num in nums]
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))

        for result in asyncio.as_completed(call_coros):
            print(await result)

if __name__ == '__main__':
    asyncio.run(main())