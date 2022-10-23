import asyncio
from asyncio import AbstractEventLoop, Future, Transport
from typing import Optional


class HTTPGetClientProtocol(asyncio.Protocol):
    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host:str=host
        self._future: Future= loop.create_future()
        self._transport: Optional[Transport] = None
        self._res_buffer: bytes = b""

    async def get_response(self):
        return await self._future

    def _get_request_bytes(self) -> bytes:
        req = f"GET / HTTP/1.1\r\nConnection: close\r\nHost:{self._host}\r\n\r\n"
        return req.encode()

    def connection_made(self, transport: Transport):
        print(f"Conn made by {self._host}")
        self._transport=transport
        self._transport.write(self._get_request_bytes())

    def data_received(self, data: bytes):
        print("Data resieved!")
        self._res_buffer+=data

    def eof_received(self) -> bool | None:
        self._future.set_result(self._res_buffer.decode())
        return False

    def connection_lost(self, exc: Exception | None) -> None:
        if exc is None:
            print("Conn closed without error!")
        else:
            self._future.set_exception(exc)