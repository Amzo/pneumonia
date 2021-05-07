#!/usr/bin/env python3

from lib.configparser import parseConfig
import select, socket, sys, random
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
selectedModel = "myCNN"

def requestModel(connection):
	print("Waiting for model")

	connected, addr = connection.accept()

	model = connected.recv(1024).decode()

	connected.close()
	selectedModel = str(model)
	print(model)

def prepareImage(imageFile):
	image = cv2.imread(imageFile)
	image = cv2.resize(image,(224,224))
	image = np.asarray(image)
	image = np.expand_dims(image, axis=0)

	return image

def makePrediction(connection, imageFile, model):
	connected,addr, = connection.accept()
	print(modelFolder + model)
	trainedModel = tf.keras.models.load_model(modelFolder + model)

	processedImage = prepareImage(imageFile)

	pred = np.argmax(trainedModel.predict(processedImage), axis=-1)

	if pred == 0:
		results = "Normal"
	else:
		results = "Pneumoni"

	print("prediction is " + results)
	connected.sendall(results.encode())
	connected.close()

def parseImage(data, saveLocation):
	# Save each image into temp with random num
	randNum =random.randint(0,100)

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

	# Execute the function depending on the request
	connected, addr = connection.accept()
	message = connected.recv(4096).decode()

	print("Received: " + message)
	connected.close()

	if message == "FILE":
		imageFile = receiveImage(connection)
	elif message == "MODEL":
		model = requestModel(connection)
	elif message == "PRED":
		makePrediction(connection, imageFile, selectedModel)
	elif message == "BYE":
		connection.close()
	else:
		print("invalid request")
