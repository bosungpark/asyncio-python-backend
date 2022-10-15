import asyncpg
import asyncio
async def main():
    connection = await asyncpg.connect(host="localhost",
                                       port=5432,
                                       user="parkbosung",
                                       database="aysncpg")
    async with connection.transaction():
        query = 'SELECT product_id, product_name from product'
        cursor = await connection.cursor(query)
        await cursor.forward(500)
        products = await cursor.fetch(100) # 500 to 600
        for product in products:
             print(product)
    await connection.close()

asyncio.run(main())