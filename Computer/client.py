# socket_echo_client.py
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "192.168.1.54"
PORT = 8000

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# try:

def send_message(pitch, volume):

    # Send data
    # message = '{:10}{:10}{:10}{:10}'.format(50, 100, 150, 200).encode()
    pitch, volume = ["{:0>10}".format(v)[0:10] for v in (pitch, volume)]
    message = (pitch + volume).encode()
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # amount_received = 0
    # amount_expected = len(message)

    # while amount_received < amount_expected:
        # data = sock.recv(16)
        # amount_received += len(data)
        # print('received {!r}'.format(data))

# finally:
    # print('closing socket')
    # # sock.close()
