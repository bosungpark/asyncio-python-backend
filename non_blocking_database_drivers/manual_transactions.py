import asyncio
import logging

import asyncpg
from asyncpg import Connection
from asyncpg.transaction import Transaction


async def main():
    conn : Connection= await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="parkbosung",
                                       database="aysncpg"
                                 )
    trx: Transaction = conn.transaction()
    await trx.start()

    try:
        # nested trx possible like save-point
        async with conn.transaction():
            await conn.execute("INSERT INTO brand VALUES(1, 'Levis')")
    except asyncpg.PostgresError:
        print("error while running trx, rollback!")
        await trx.rollback()
    else:
        print("no error!")
        await trx.commit()
    finally:
        q = """
        SELECT brand_name FROM brand
        WHERE brand_name LIKE 'Levis%'
        """
        brands= await conn.fetch(q)
        print(brands)
        await conn.close()
asyncio.run(main())