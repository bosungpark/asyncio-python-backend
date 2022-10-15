import asyncio
from random import sample, randint
from typing import List, Tuple, Union

import asyncpg
from asyncpg import Record, Connection
from schema import *

def load_common_words() -> List[str]:
    with open("common_words.txt") as common_words:
        return common_words.readlines()

def generate_brand_names(words: List[str]) -> List[Tuple[Union[str, ]]]:
    return [(words[index], ) for index in sample(range(100), 100)]

async def insert_brands(common_words, connection : Connection) -> int:
    brands = generate_brand_names(common_words)
    q = "INSERT INTO brand VALUES (DEFAULT, $1)"
    return await connection.executemany(q, brands)

def gen_products(common_words: List[str],
                 brand_id_start: int,
                 brand_id_end: int,
                 products_to_create: int) -> List[Tuple[str, int]]:
    products = []
    for _ in range(products_to_create):
        description = [common_words[index] for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))
    return products


def gen_skus(product_id_start: int,
             product_id_end: int,
             skus_to_create: int) -> List[Tuple[int, int, int]]:
    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus

# simple usage
# async def main():
#     connection : Connection= await asyncpg.connect(host="localhost",
#                                        port=5432,
#                                        user="parkbosung",
#                                        database="aysncpg"
#                                        )
#     await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
#
#     q = "SELECT brand_id, brand_name FROM brand"
#     results: List[Record] = await connection.fetch(q)
#
#     for brand in results:
#     # < Record brand_id = 1 brand_name = 'Levis' >
#         print(brand)
#     await connection.close()

# gen many data at once
# async def main():
#     common_words=load_common_words()
#     connection: Connection = await asyncpg.connect(host="localhost",
#                                        port=5432,
#                                        user="parkbosung",
#                                        database="aysncpg"
#                                        )
#     await insert_brands(common_words,connection)
#
#     product_tuples = gen_products(common_words,
#                                   brand_id_start=1,
#                                   brand_id_end=100,
#                                   products_to_create=1000)
#     await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)",
#                                  product_tuples)
#
#     sku_tuples = gen_skus(product_id_start=1,
#                           product_id_end=1000,
#                           skus_to_create=100000)
#     await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)",
#                                  sku_tuples)
#
#     await connection.close()

# FIXME: errror 1개 이상의 con을 sql에서 구할 수는 없다! -> 해결을 위해서는 connection pool이 필요하다!
async def main():
    connection: Connection = await asyncpg.connect(host="localhost",
                                           port=5432,
                                           user="parkbosung",
                                           database="aysncpg"
                                           )
    qs = [connection.execute(PRODUCT_QUERY) for _ in range(2)]
    _ = await asyncio.gather(*qs)
asyncio.run(main())