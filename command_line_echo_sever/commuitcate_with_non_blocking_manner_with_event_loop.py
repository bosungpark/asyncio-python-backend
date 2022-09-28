"""
making single thread socket-based network applicaton:)

this commuitcates with non-blocking manner with event loop
"""
import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector=selectors.DefaultSelector()

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)# addr, tcp
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to avoid port already in use

server_address=("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)

selector.register(server_socket, selectors.EVENT_READ)

connections=[]

while True:
    events: List[Tuple[SelectorKey, int]]=selector.select(timeout=1)

    if len(events)==0:
        print("No event, wait a bit more!")

    for event, _ in events:
        event_socket=event.fileobj

        if event_socket==server_socket:
            connection, client_address= server_socket.accept()
            connection.setblocking(False)
            print(f"i got a connection from {client_address}!!!!!")
            selector.register(connection, selectors.EVENT_READ)
        else:
            data=event_socket.recv(1024)
            print(f"i got some data: {data}!")
            connection.sendall(data)