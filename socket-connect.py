#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 40100
BUFFER_SIZE = 20
MESSAGE = "a"
MESSAGE2 = "a\n"
MESSAGE3 = "b\n"
MESSAGE4 = "c\n"
MESSAGE5 = "test"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
print('sending ' + MESSAGE)

'''
s.send(MESSAGE2.encode('utf-8'))
print('sending ' + MESSAGE2)
s.send(MESSAGE3.encode('utf-8'))
print('sending ' + MESSAGE3)
s.send(MESSAGE4.encode('utf-8'))
print('sending ' + MESSAGE4)
s.send(MESSAGE5.encode('utf-8'))
print('sending ' + MESSAGE5)
'''
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)