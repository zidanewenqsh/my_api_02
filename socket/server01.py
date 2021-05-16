import socket
import struct
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ("127.0.0.1", 8081)
socket_s.bind(ip_port)
socket_s.listen(5)
conn, addr = socket_s.accept() # 放到循环里就会阻塞
while True:
    print("start")

    # print(conn)
    # print(addr)
    bufsize = struct.calcsize(">I")
    msg = conn.recv(bufsize)
    bufsize = struct.unpack(">I", msg)[0]
    print("bufsize", bufsize, len(msg))
    if bufsize == 0:
        continue
    msg = conn.recv(bufsize)
    print("msg", msg)
    conn.send(msg.upper())
    print("send success")
    # break
socket_s.close()