import socket
import sys

sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_address = '/tmp/socket_file'


print(f'connecting to {server_address}')




message = input('What would you like to send')

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    sock.sendall(message.encode())
    sock.settimeout(5)

    try:
        while True:
            data = sock.recv(4096)

            if data:
                print('server response:' + data.decode('utf-8'))
            else:
                break
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()