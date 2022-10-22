import asyncio
import functools
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

from util import async_timed


def mean_cal_for_row(arr, row):
    return np.mean(arr[row], axis=1)

data_points=400000000
rows=50
columns=int(data_points/rows)

matrix=np.arange(data_points).reshape(rows,columns)

@async_timed()
async def main():
    loop=asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks=[]
        for i in range(rows):
            mean=functools.partial(mean_cal_for_row, matrix, i)
            tasks.append(loop.run_in_executor(pool, mean))
        result= asyncio.gather(*tasks)
asyncio.run(main())