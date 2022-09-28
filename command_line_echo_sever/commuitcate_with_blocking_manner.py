"""
making single thread socket-based network applicaton:)

this commuitcates with blocking manner

cmd: telnet localhost 8000

example: "hihi" + enter

expected: 
i got a connection from ('127.0.0.1', 53534)!!!!!
i got data: b'hi'!
i got data: b'hi'!
i got data: b'\r\n'!
All data i got: b'hihi\r\n'
"""
import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)# addr, tcp
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to avoid port already in use

server_address=("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address= server_socket.accept()
    print(f"i got a connection from {client_address}!!!!!")

    buffer=b""

    while buffer[-2:] != b"\r\n":
        data= connection.recv(2)
        if not data:
            break
        else:
            print(f"i got data: {data}!")
            buffer+=data
    print(f"All data i got: {buffer}")
finally:
    server_socket.close()