import asyncio
import functools
import time
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List, Dict


def partitoin(data: List,
              chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def map_fiequencies(chunk: List[str]) -> Dict[str,int]:
    freq = {}
    for line in chunk:
        word, _, cnt, _= line.split("\t")
        if word in freq:
            freq[word]+=int(cnt)
        else:
            freq[word]=int(cnt)
    return freq

def merge_dicts(first: Dict[str, int],
                second: Dict[str,int]) -> Dict[str, int]:
    merge = first
    for key in second:
        if key in merge:
            merge[key]+=second[key]
        else:
            merge[key]=second[key]
    return merge

async def reduce(loop, pool, counter, chunk_size) -> Dict[str,int]:
    chunks:List[List[Dict]] = list(partitoin(counter, chunk_size))
    reducers=[]
    while len(chunks[0])>1:
        for chunk in chunks:
            reducer = partial(functools.reduce, merge_dicts, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))
        reducer_chunk = await asyncio.gather(*reducers)
        chunks = list(partitoin(reducer_chunk, chunk_size))
        reducers.clear()
    return chunks[0][0]

async def main(partition_size: int):
    with open("googlebooks-eng-all-1gram-20120701-a.txt", encoding="utf-8") as f:
        lines = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with ProcessPoolExecutor() as pool:
            for chunk in partitoin(lines, partition_size):
                tasks.append(loop.run_in_executor(pool, partial(map_fiequencies, chunk)))

            intermediate_results = await asyncio.gather(*tasks)
            final_result = await reduce(loop, pool, intermediate_results, 500)
            print(f"Aardvark={final_result['Aardvark']}")
            end = time.time()
            print(f"{end-start:.4f}")

if __name__ == '__main__':
    asyncio.run(main(partition_size=60000))