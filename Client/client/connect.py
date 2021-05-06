#!/usr/bin/env python3

import socket
import time
def makeConnection(port, host):
	remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remote.connect(('127.0.1.1',50022))

	return remote

def sendImage(imageFile):
	sendFile = open(imageFile, 'rb')

	remote = makeConnection(50022, "127.0.1.1")

	while True:
		chunk = sendFile.read(4096)
		if not chunk:
			break

		remote.sendall(chunk)
	sendFile.close




image = "test.jpeg"

data = sendImage(image)
