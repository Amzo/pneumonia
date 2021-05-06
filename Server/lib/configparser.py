#!/usr/bin/env python3

import configparser

def parseConfig(filename):
	config = configparser.ConfigParser()
	config.read(filename)

	host = config['Server']
	port = config['Port']


	return host['servername'], port['port']

