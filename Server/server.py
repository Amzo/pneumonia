#!/usr/bin/env python3

from lib.configparser import parseConfig
import select, socket, sys, random
import time

# Set up some global variables
host, port = parseConfig('ini/config.ini')
imageName = "pneumonia%s.jpg"
incomingFolder = "temp"

def makePrediction(connection, imageFile):
	connected,addr, = connection.accept()
	connected.sendall(b'1')
	connected.close()

def parseImage(data, saveLocation):
	# Save each image into temp with random num
	randNum =random.randint(0,10)

	imageFile = open(imageName % randNum, 'wb')
	imageFile.write(data)
	imageFile.close()

	return (imageName % randNum)

def waitForConnection(host, port):
	# Create a TCP/IP socket
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = (host, int(port))
	print('starting up on %s port %s' % server_address)
	server.bind(server_address)

	server.listen()

	return server

def receiveImage(connection):
	data = b''

	print("waiting for image")
	connected, addr = connection.accept()

	incommingTotal = b''
	while True:
		incommingPart = connected.recv(4096)

		if not incommingPart:
			break
		incommingTotal += incommingPart

	print("Image received")
	savedName = parseImage(incommingTotal, incomingFolder)

	return savedName

	connected.close()

while True:
	try:
		connection
	except NameError:
		connection = waitForConnection(host, port)

	imageFile = receiveImage(connection)

	makePrediction(connection, imageFile)
