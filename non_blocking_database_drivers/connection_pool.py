"""
we can only execute one q in one conn
so we need to manage multiple conn

connection pool is kind of cache that manage existing conn of db instance
"""
import asyncio

import asyncpg
from asyncpg import Pool

from schema import *
from util import async_timed

prduct_query=PRODUCT_QUERY

async def query_product(pool: Pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(prduct_query)

@async_timed()
async def query_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]

@async_timed()
async def query_asynchronously(pool, queries):
    queries= [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)

async def main():
    """
    return:

    starting <function query_synchronously at 0x101de2a70> with args (<asyncpg.pool.Pool object at 0x1019329b0>, 10000) {}
    finished <function query_synchronously at 0x101de2a70> in 2.3866 second(s)
    starting <function query_asynchronously at 0x102292cb0> with args (<asyncpg.pool.Pool object at 0x1019329b0>, 10000) {}
    finished <function query_asynchronously at 0x102292cb0> in 0.8887 second(s)
    """
    async with asyncpg.create_pool(
                                    host="localhost",
                                    port=5432,
                                    user="parkbosung",
                                    database="aysncpg",
                                    min_size=6,
                                    max_size=6
                                    ) as pool:
        await query_synchronously(pool, 10000)
        await query_asynchronously(pool, 10000)
if __name__ == '__main__':
    asyncio.run(main())