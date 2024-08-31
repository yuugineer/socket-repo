import socket
import os
from faker import Faker


sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)
sock.listen(1)

print(f'starting up on {server_address}')

while True:
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        while True:

            data = connection.recv(4096)

            data_str = data.decode('utf-8')

            print('Received' + data_str)


            if data:
                fake = Faker()
                response = fake.text()

                connection.sendall(response.encode())
            else:
                print('no data from', client_address)
                break

    finally:
        print("closing current connection")
        connection.close()

        