#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 20
# Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    # conn.send(data)  # echo
    if "/version" in data.decode('utf-8'):
        resp = "0.1"
        conn.send(resp.encode('utf-8'))

    if "/echo" in data.decode('utf-8'):
        data = data.replace("/echo", "")
        conn.send(data.encode('utf-8'))

conn.close()