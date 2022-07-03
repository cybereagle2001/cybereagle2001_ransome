#coded by cybereagle2001

import socket

server_ip ='0.0.0.0'
server_port = 443
data_size = 1024 * 500
cyber = socket.socket()
cyber.bind((server_ip,server_port))
cyber.listen(10)
client_socket,client_ip = cyber.accept()
key = client_socket.recv(data_size).decode()
print(key)
