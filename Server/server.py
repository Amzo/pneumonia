#!/usr/bin/env python3

from lib.configparser import parseConfig
import select, socket, sys

def serverListen(host, port):
	# Create a TCP/IP socket
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = (host, int(port))
	print('starting up on %s port %s' % server_address)
	server.bind(server_address)

	# Listen for incoming connections
	server.listen()

	# Keep up with the queues of outgoing messages
	message_queues = {}

	connected, addr = server.accept()

	with connected:
		print('Connected by', addr)
		while True:
			data = connected.recv(1024)
			if not data:
				 break
			connected.sendall(data)


host, port = parseConfig('ini/config.ini')

print(host, port)
serverListen(host, port)
