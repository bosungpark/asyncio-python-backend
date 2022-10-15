import asyncio

import asyncpg
from schema import *

async def main():
    connection = await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="parkbosung",
                                       database="aysncpg"
                                       )
    # version = connection.get_server_version()
    # print("server version=",version)

    statemants = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT
    ]
    print("creating db")
    for s in statemants:
        status= await connection.execute(s)
        print(f"executed in con {status}")
    print("fin db creation")
    await connection.close()

asyncio.run(main())