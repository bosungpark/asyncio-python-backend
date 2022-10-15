import asyncio

import asyncpg


async def main():
    connection = await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="parkbosung",
                                       database="aysncpg")

    query = 'SELECT product_id, product_name FROM product'
    # normal for loops and next functions won’t work with these types of generators
    async with connection.transaction():
        # 한번에 오는 로드를 분산
        async for product in connection.cursor(query):
            print(product)
    await connection.close()
asyncio.run(main())
