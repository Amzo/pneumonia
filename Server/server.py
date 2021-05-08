#!/usr/bin/env python3

from lib.configparser import parseConfig
import select, socket, sys, random
from threading import Thread
import time

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
import numpy as np
import cv2

host, port = parseConfig('ini/config.ini')

# GPU setup
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
config = tf.config.experimental.set_memory_growth(physical_devices[0], True)

imageName = "pneumonia%s.jpg"
incomingFolder = "./temp/"
modelFolder = "./models/"

def sendMessage(connected, msg):
	print("Replying: " + msg)
	connected.sendall(msg.encode())

def requestModel(connected):
	print("Waiting for model")

	model = connected.recv(4).decode()

	print("Got model: " + model.lower())
	model = model.lower()
	if model == "ince":
		model = "Inception"
	elif model == "dens":
		model = "densenet"
	elif model == "mycn":
		model = "myCNN"
	elif model == "vgg1":
		model = "VGG"
	elif model == "xcep":
		model = "Xception"
	else:
		model = "fail"

	if model == "fail":
		print("Returning Error code 3")
		connected.sendall("3".encode())
	else:
		print("returning success")
		connected.sendall("0".encode())
		return model

def prepareImage(imageFile):
	image = cv2.imread(imageFile)
	image = cv2.resize(image,(224,224))
	image = np.asarray(image)
	image = np.expand_dims(image, axis=0)

	return image

def makePrediction(connected, imageFile, model):
	trainedModel = tf.keras.models.load_model(modelFolder + model)

	processedImage = prepareImage(imageFile)

	pred = np.argmax(trainedModel.predict(processedImage), axis=-1)

	if pred == 0:
		results = "N"
	else:
		results = "P"

	print("prediction is " + results)
	connected.sendall(results.encode())

def parseImage(data, saveLocation):
	# Save each image into temp with random num
	randNum =random.randint(0,100)

	imageFile = open(imageName % randNum, 'wb')
	imageFile.write(data)
	imageFile.close()

	return (imageName % randNum)

def receiveImage(connected):
	bufferSize = 4096

	print("waiting for image")
	results = connected.recv(10).decode()
	print("Sending okay")
	sendMessage(connected, ("0"))
	print("Got size: " + results)

	fileSize = ""
	for digit in results:
		if digit.isdigit():
			fileSize += digit

	while ((int(fileSize) % bufferSize) != 0):
		bufferSize -= 1


	# Receive files in chunks, handle remainder if file isn't divisble by chunk size
	incommingTotal = b''
	i = 0

	count = int(fileSize) / bufferSize
	print(f"Waiting on file in {count} chunks")
	while i != int(fileSize):
		incommingPart = connected.recv(1)

		if not incommingPart:
			break
		incommingTotal += incommingPart
		i += 1


	print("Image received")
	savedName = parseImage(incommingTotal, incomingFolder)

	return savedName

def removeClient(connected, msg):
	print(f"remove client: {msg}")
	try:
		clientSockets.remove(connected)
	except KeyError:
		print("client already removed")

def parseCommand(connected):
		stillThere = True
		timeout = 0

		# Execute the function depending on the request
		while stillThere:
			message = ''
			print("Waiting for next command")

			while message == '':
				if timeout >= 20:
					removeClient(connected, "timeout")
					stillThere = False
					break

				time.sleep(1)
				try:
					message = connected.recv(4).decode()
				except Exception as e:
					print(f"{e}")
					removeClient(connected, "Error occured")
					stillThere = False
				timeout += 1

			if stillThere:
				print("Command: " +message)
				if message == "FILE":
					sendMessage(connected, "0")
					imageFile = receiveImage(connected)
					breakCon = True
				elif message == "MODE":
					sendMessage(connected, "0")
					selectedModel = requestModel(connected)
					print("Got model:" + selectedModel)
				elif message == "PRED":
					try:
						selectedModel, imageFile
					except NameError:
						print("Sending error 1")
						sendMessage(connected, "1")
					else:
						print("Sending Success")
						sendMessage(connected, "0")
						makePrediction(connected, imageFile, selectedModel)
				elif message == "BYE!":
					sendMessage(connected, "0")
					removeClient(connected, "bye")
				else:
					print(f"[*] invalid request: {message}")

def waitForClient(socket):
	try:
		msg = socket.send("?".encode())
	except Exception as e:
		# client no longer connected
		# remove it from the set
		print(f"[!] Error: {e}")
		try:
			clientSockets.remove(socket)
		except Exception as e:
			print(f"[!] Error: {e}")
	else:
		parseCommand(socket)

# initialize list/set of all connected client's sockets
clientSockets = set()

# create a TCP socket
serverSocket = socket.socket()

# make the port as reusable port
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)

# bind the socket to the address we specified
serverSocket.bind((host, int(port)))

# timeout socket after 10 seconds of no command
socket.setdefaulttimeout(10)

# listen for upcoming connections
serverSocket.listen(5)

print(f"[*] Starting up server as {host}:{port}")

while True:
	# we keep listening for new connections all the time
	clientSocket, clientAddress = serverSocket.accept()
	print(f"[+] {clientAddress} connected.")

	 # add the new connected client to connected sockets
	clientSockets.add(clientSocket)

	# start a new thread that listens for each client's messages
	threadT = Thread(target=waitForClient, args=(clientSocket,))

	# make the thread daemon so it ends whenever the main thread ends
	threadT.daemon = True
	# start the thread
	threadT.start()


for cs in clientSockets:
	cs.close()
