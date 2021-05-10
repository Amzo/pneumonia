# Pneumonia project for KF5012 module

## Table of contents
* [Project information](#project-information)
* [Technologies](#technologies)
* [Repository](#repository)
* [Documentation](#documentation)
* [Solution Development Report](#solution-development-report)
* [Server](#server)
* [Client](#client)

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

Anthony Donnelly - Baseline Implementation & User Interface


Gabriela Piatek - Project Ideation & Solution Review 


John Robson - Ethical Evaluation & Solution Testing


Navil Hassan - Project Management & Solution Design


## Solution Development report

### Pipeline Evaluations

Without any pre-processing of the dataset overfitting became problematic, making prediction accuracy very low with the test set. Also as a measure to ensure the models can handle a broad range of variables that could possibly occur in images as they are fed to the pipeline, training and test images went under data augmentation to produce images with possible expected variations. This consisted of rescaling, rotation, zoom, brightness changes, and even horizontal and vertical flips. By doing this it allows the models to be trained against these variations and better understand how to handle them. With the use of this augmentation method, overfitting no longer occurred and as the pipeline is designed for use with even lightweight systems like mobile phones, understanding how new data may be presented to the system has been addressed.

### Model Evaluations

As a baseline model, C-NN was used initially for the system which performed at 73% accuracy. To ensure better accuracy for predictions, alternative models were introduced to the data providing a range of models to test against. By doing this ensembling became possible as a method of connecting the performances of all the models to provide a high accuracy of 93% against the test set and 95% with the optional validation set.

### Parameter Justifications

Initially the final activation parameter for the baseline model was sigmoid as we have a binary classification issue
and this was the most suitable activation function. As we moved onto the iterative development, it was decided to switch
to softmax and categorical crossentropy so that the model can be retrained on more classes to detect a wider range of
lung diseases.

The optimiser adam was used as this along with RMSprop provided the highest accuracy yield. In the iterative model
we switched from Adam to RMSprop as RMSprop was slightly better.

The model layers where kept small 

10 epochs seemed to produce the best output, as anything after this point the model didn't improve much more. Using 10 epochs kept training time
to an optimal level without being too time consuming.

### Reproducible Code

For reproducing all experiments, the trained models are saved onto google drive and can be fetched within
the google colaboration file using shell script. The training history pickle file is also fetched so that
the training accuracy and training loss can be visualised as well as the validation loss.


## Server

This is a simple server written in python which accept numerous commands to be able to receive and image and make a prediction of the image and return the result

This server can perform the prediction on a server with the suitable hardware and allow people to run a client and still use the model regardless of their hardware.

An interface for the following devices can be used:

1. mobile devices
2. laptops
3. desktops

An example client is available in the client folder also written in python

Full documentation can be found [here](https://github.com/Amzo/pneumonia/tree/main/Documentation/Anthony/server)

## Client
 
Minimalistic gui and [connect.py](https://github.com/Amzo/pneumonia/blob/main/Client/client/connect.py) file to add some basic functions to allow sending and receiving replies from the server.

[connect.py](https://github.com/Amzo/pneumonia/blob/main/Client/client/connect.py) can be included into any python script and allow sending files to to the server.


An example gui making use of [connect.py](https://github.com/Amzo/pneumonia/blob/main/Client/client/connect.py) can also be found [here](https://github.com/Amzo/pneumonia/blob/main/Client/pneumoniaDetect.py).

For full documentation on the client check [here](https://github.com/Amzo/pneumonia/tree/main/Documentation/Anthony/client).



