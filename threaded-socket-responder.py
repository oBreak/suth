#!/usr/bin/env python

import socket
from threading import Thread
#from SocketServer import ThreadingMixIn


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print ("[+] New thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print ("received data:", data)
            if data.decode('utf-8') == 'a':
                resp = "0.1"
                conn.send(resp.encode('utf-8'))
                print('Received input asking for version number.')
            if data.decode('utf-8') == 'version\n':
                resp = "0.1"
                conn.send(resp.encode('utf-8'))
                print('Received input asking for version number.')
            if data.decode('utf-8') == 'b':
                resp = "0.2"
                conn.send(resp.encode('utf-8'))
                print('Option b')
            #print data.decode('utf-8')
                #resp = str('0.1')
                #conn.send(resp.encode('utf-8'))
            '''if not data: break
            print ("received data:", data)'''
            #conn.send(data)  # echo


TCP_IP = '127.0.0.1'
TCP_PORT = 40100
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
'''
#new stuff

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
#end new stuff
'''
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(4)
    print ("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
