"""
SHA is not best algorithm, it more suit for brute-force attack

if data is larger than 2048 byte GIL released
"""
import asyncio
import functools
import hashlib
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor

from util import async_timed


def random_password(lenth: int) -> bytes:
    ascii_lowercase = string.ascii_lowercase.encode()
    return b"".join(bytes(random.choice(ascii_lowercase)) for _ in range(lenth))

passwords = [random_password(10) for _ in range(10000)]

def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))

@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    tasks = []
    with ThreadPoolExecutor() as pool:
        for pw in passwords:
            tasks.append(loop.run_in_executor(pool, functools.partial(hash,pw)))
    await asyncio.gather(*tasks)
asyncio.run(main())