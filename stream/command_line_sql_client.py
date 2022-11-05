import asyncio
import os
import tty
from collections import deque

import asyncpg
from asyncpg import Pool

from create_stdin_reader import create_stadin_reader
from escape_sequence import move_to_top_of_screen, save_cursor_position, restore_cursor_position, delete_line
from message_store import MessageStore
from read_line import read_line


async def run_query(query: str, pool: Pool, messagestore: MessageStore):
    async with pool.acquire() as connection:
        try:
            result = await connection.fetchrow(query)
            await messagestore.append(f"Fetched {len(result)} row from: {query}")
        except Exception as e:
            await messagestore.append(f"got excetion {e} from :{query}")

async def main():
    tty.setcbreak(0)
    os.system("clear")
    rows = move_to_top_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(redraw_output, rows - 1)
    stdin_reader = await create_stadin_reader()

    async with asyncpg.create_pool(
            host="localhost",
            port=5432,
            user="parkbosung",
            database="aysncpg"
    ) as pool:
        while True:
            query = await read_line(stdin_reader)
            asyncio.create_task(run_query(query,pool,messages))
asyncio.run(main())