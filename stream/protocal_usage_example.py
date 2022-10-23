import asyncio
from asyncio import AbstractEventLoop

from transports_and_protocols import HTTPGetClientProtocol


async def make_req(host: str, port: int, loop:AbstractEventLoop) -> str:
    def protocol_factory():
        return HTTPGetClientProtocol(host,loop)

    _, protocal = await loop.create_connection(protocol_factory,host=host,port=port)
    return await protocal.get_response()

async def main():
    loop = asyncio.get_running_loop()
    result = await make_req("www.example.com", 80, loop)
    print(result)

asyncio.run(main())