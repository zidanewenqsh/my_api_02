import socket
import struct
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ("127.0.0.1",8081)
socket_c.connect(ip_port)
while True:

    msg = input("please input:")
    msg = msg.encode("utf-8")
    socket_c.send(msg)
    msg_1 = socket_c.recv(1024)
    print(msg_1)
    # break
socket_c.close()