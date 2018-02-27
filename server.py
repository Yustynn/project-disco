# socket_echo_server.py
import socket
import sys
from time import sleep
from light_controller import set_light

READING_MAX_LENGTH = 10
PORT = 8000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('10.12.14.249', PORT)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(50)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        res = ''
        while True:
            data = connection.recv(16).decode()
            while len(data) > 0:
                if len(res) < READING_MAX_LENGTH * 2:
                    stop_point = READING_MAX_LENGTH * 2 - len(res)
                    new_data = data[stop_point:]
                    res += data[:stop_point]
                    data = new_data
            
                if len(res) == READING_MAX_LENGTH * 2:
                    pitch, volume = [float(v) for v in (res[:READING_MAX_LENGTH],
                                                   res[READING_MAX_LENGTH:])]

                    print(pitch, volume)
                    set_light(pitch, volume)
                    res = ''
                    # sleep(1)

            # print('received {}'.format(res))
            # if data:
                # print('sending data back to the client')
                # connection.sendall(data.encode())
            # else:
                # print('no data from', client_address)
                # break

    finally:
        # Clean up the connection
        connection.close()
