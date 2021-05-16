import socket
import struct
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ip_port = ("127.0.0.1", 8081)
socket_s.bind(ip_port)
socket_s.listen(5)
while True:
    conn, addr = socket_s.accept()
    print(conn)
    print(addr)

    while True:
        # msg = conn.recv(1024)
        # print(msg)
        # conn.send(msg.upper())
        try:
            msg = conn.recv(1024)
            print(msg)
            conn.send(msg.upper())
        except Exception as e:
            print(e)
            break

    # break
socket_s.close()