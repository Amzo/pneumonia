#!/usr/bin/env python3

import socket

def makeConnection(port, host, data):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as remote:
		remote.connect(('127.0.0.1',50022))
		remote.sendall('Hello, world')

		data = remote.recv(1024)
		print('Received', repr(data))




