#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:        Anthony Donnelly
@contributor:
"""

import socket
import time
import os

def getReply():
	response = remote.recv(1).decode()

	return response

def sendMessage(msg):
	# our packets should be four bytes
	# prevent hanging
	if len(msg) > 4 or len(msg) < 4:
		("Message must be 4 bytes")
	else:
		print("Sending Commands: " + msg)
		remote.sendall(msg.encode())
		response = getReply()
		return response

def sendModel(model):
	response = sendMessage("MODE")

	if response == "0":
		print("Got OK response, sending model")
		model = model[0:4]

		# only send 4 bytes of data
		remote.sendall(model.encode())

		print("Model sent, waiting reply")
		reply = getReply()
		print("Got reply: " + reply)

def sendImage(imageFile):
	bufferSize = 4096

	response = sendMessage("FILE")
	if response == "0":
		print("Got OK response, sending file size and file")

		filesize = os.path.getsize(imageFile)

		# Increase size to meet the buffer
		# since the size is numeric, add digits to fill the buffer
		# strip on server side
		# string start from index 0
		dummysize = str(filesize)
		while (len(dummysize) < 10):
			dummysize += "z"

		print(len(dummysize))
		remote.sendall(dummysize.encode())
		response = getReply()

		while filesize % bufferSize != 0:
			bufferSize -= 1


		count = filesize / bufferSize
		i = 0
		print(response)
		if response == "0":
			with open(imageFile, "rb") as sendFile:
				print(f"Sending {count} chunks")
				while i != filesize:
					chunk = sendFile.read(1)
					if not chunk:
						break
					remote.sendall(chunk)
					i += 1
			sendFile.close()
			print("image file sent")

def receivePred():
	response = sendMessage("PRED")

	if response == "0":
		pred =  getReply()
		print("prediciton is " + pred)

		return pred
