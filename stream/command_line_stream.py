import asyncio
import os
import sys
import tty
from collections import deque

from escape_sequence import *

from message_store import MessageStore
from create_stdin_reader import create_stadin_reader
from read_line import read_line


async def sleep(delay: int, message_store: MessageStore):
    await message_store.append(f"Starting delay {delay}")
    await asyncio.sleep(delay)
    await message_store.append(f"Finished delay {delay}")

async def main():
    tty.setcbreak(sys.stdin)
    os.system("clear")
    rows = move_to_top_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(redraw_output, rows-1)
    stdin_reader = await create_stadin_reader()

    while True:
        line = await read_line(stdin_reader)
        delay_time = int(line)
        asyncio.create_task(sleep(delay_time, messages))

asyncio.run(main())