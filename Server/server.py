#!/usr/bin/env python3

from lib.configparser import parseConfig
import select, socket, sys, random
import time

# Set up some global variables
host, port = parseConfig('ini/config.ini')
imageName = "pneumonia%s.jpg"
incomingFolder = "temp"

def parseImage(data, saveLocation):
	# Save each image into temp with random num
	randNum =random.randint(0,10)

	imageFile = open(imageName % randNum, 'wb')
	imageFile.write(data)
	imageFile.close()

def serverListen(host, port):
	data = b''

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

	incommingTotal = b''
	while True:
		incommingPart = connected.recv(4096)

		if not incommingPart:
			break
		print("Received 4096 bytes")
		incommingTotal += incommingPart

	print("Image received")
	parseImage(incommingTotal, incomingFolder)
#	connected.sendall(b'Image saved')


serverListen(host, port)
