"""
making single thread socket-based network applicaton:)

this commuitcates with non-blocking manner with asyncio event loop which throwing exception
"""
import asyncio
from asyncio import AbstractEventLoop
import logging
import signal
import socket
from typing import List

async def echo(connection: socket, loop: AbstractEventLoop)->None:
    try:
        while data:=await loop.sock_recv(connection, 1024):
            print(f"got data {data}")
            if data == b'boom\r\n':
                raise Exception("BOOM!! Error happen!!")
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close

echo_tasks=[]

async def connection_listener(server_socket: socket, loop:AbstractEventLoop):
    while True:
        connection, client_address= await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"i got a connection from {client_address}!!!!!")
        echo_task=asyncio.create_task(echo(connection,loop))
        echo_tasks.append(echo_task)

class GracefulExit(SystemExit):
    pass

def shutdown():
    raise GracefulExit()

async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters= [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            #time out error happen here
            pass

async def main():
    server_socket=socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to avoid port already in use

    server_address=("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    
    for signame in {"SIGINT","SIGTERM"}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await connection_listener(server_socket, loop)

loop=asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()