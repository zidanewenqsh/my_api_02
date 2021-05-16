import socket
import struct
import signal
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ("127.0.0.1",8081)
socket_c.connect(ip_port)
while True:

    msg = input("please input:")
    msg = msg.encode("utf-8")
    bufsize = len(msg)
    msgsize = struct.pack(">I", bufsize)
    socket_c.send(msgsize)
    socket_c.send(msg)
    msg_1 = socket_c.recv(bufsize)
    print("msg_1", msg_1)
    # signal.signal(signal.SIGPIPE, signal.SIG_IGN)
    # break
socket_c.close()