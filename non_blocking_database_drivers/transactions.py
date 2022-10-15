import asyncio
import logging

import asyncpg
from asyncpg import Connection


async def main():
    conn : Connection= await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="parkbosung",
                                       database="aysncpg"
                                 )
    async with conn.transaction():
        await conn.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis3')")
        try:
            # nested trx possible like save-point
            async with conn.transaction():
                await conn.execute("INSERT INTO brand VALUES(1, 'Levis')")
        except Exception:
            logging.exception("error while running trx")
        finally:
            q = """
            SELECT brand_name FROM brand
            WHERE brand_name LIKE 'Levis%'
            """
            brands= await conn.fetch(q)
            print(brands)
            await conn.close()
asyncio.run(main())