"""
cmd: telnet localhost 8000
"""
import asyncio
import socket

class ConnectedSocket:
    def __init__(self, server_socket):
        self.connection=None
        self._server_soctet=server_socket

    async def __aenter__(self):
        print("enter context manager")
        loop = asyncio.get_event_loop()
        conn, addr = await loop.sock_accept(self._server_soctet)
        self.connection=conn
        print("accepted conn")
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("exit context manager")
        self.connection.close()
        print("close conn")

async def main():
    loop = asyncio.get_event_loop()

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # to avoid port already in use

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as conn:
        data = await loop.sock_recv(conn, 1024)
        print(data)

asyncio.run(main())