import asyncio
from typing import List

import asyncpg
from asyncpg import Record, Connection


async def main():
    connection : Connection= await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="parkbosung",
                                       database="aysncpg"
                                       )
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")

    q = "SELECT brand_id, brand_name FROM brand"
    results: List[Record] = await connection.fetch(q)

    for brand in results:
        print(brand)
    await connection.close()
asyncio.run(main())