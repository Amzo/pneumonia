# Pneumonia project for KF5012 module

## Table of contents
* [Project information](#project-info)
* [Technologies](#technologies)
* [Repository](#repository)

## Project information
This project is experimentation to create a model that uses static images of chest x-rays to detect pneumonia on an early stage.
Project made by:
Anthony Donnelly, John Robson, Gabriela Piatek, Navil Hassan 
	
## Technologies 
Project is devided into parts such as:

Google collaboration file for pneumonia detection:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Amzo/pneumonia/blob/main/cnnModels.ipynb)

Baseline model 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Amzo/pneumonia/blob/main/baseline.ipynb) 

## Repository
The repository of the project contains cnnModels.ipynb, pneumoniaDetect.py, README.md, gui files, as well as files with our missions. 

The first cnnModels.ipnyb file is the most important file of our project, the notebook where the project either trained or loaded 4 additional models ontop of our model that we have created. 

pneumoniaDetect.py file is a copied GUI over.   

README.md file, which helps to provide all neccessary information about the project and files.  


## Documentation

The documentation section shows the exact missions prepared by our team:

Anthony - 


Gabriela -


John -


Navil -



## Server

This is a simple server written in python which accept numerous commands to be able to receive and image and make a prediction of the image and return the result

This server can perform the prediction on a server with the suitable hardware and allow people to run a client and still use the model regardless of their hardware.

An interface for the following devices can be used:

1. mobile devices
2. laptops
3. desktops

An example client is available in the client folder also written in python

Full documentation can be foudd [here](https://github.com/Amzo/pneumonia/tree/main/Documentation/Anthony/server)

## Client

Minimalistic gui and [connect.py](https://github.com/Amzo/pneumonia/blob/main/Client/client/connect.py) file to add some basic functions to allow sending and receiving replies from the server.

[connect.py](https://github.com/Amzo/pneumonia/blob/main/Client/client/connect.py) can be included into any python script and allow sending files to to the server.


An example gui makign use of [connect.py](https://github.com/Amzo/pneumonia/blob/main/Client/client/connect.py) can also be found [here].(https://github.com/Amzo/pneumonia/blob/main/Client/pneumoniaDetect.py)

For full documentation on the client check [here](https://github.com/Amzo/pneumonia/tree/main/Documentation/Anthony/client).



