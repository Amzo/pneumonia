The client has a simple interface to showcase the server and API in use.

The connect.py script can be included in any application to communicate with the server.

## Functions 
 
These are a list of functions used by connect.py to communicate with the server. Connect.py is just an immediate implementation to show functionality.

### getReply(connection) 
	Get a response from the server

	Args connection: An open connection to the server.

	returns a 1 byte string 
 
### sendMessage(msg, connection) 
	Sends a message to the server

	Args msg: Should be a 4-byte string to send to the server.
	Args connection: It should be an open connection.
 
### sendModel(model, connection) 
	Send the requested model to the server. 
 
	args connection: The current open connection to the server
	args 'model': Should be a 4 byte string of the model. Available options are: 
 
	INCE - Inception model 
 
	DENS - Densenet odel 
 
	MYCN - My CNN model 
 	
	VGG! - VGG19 model 
 
	XCEP - Xception Model 
 
	RESN - Resnet Model 
 
	ENSM - Ensembled model 
 
### sendImage(imageFile, connection) 
 	Sends the image file to the server 
 
	Args imageFile: complete path to the image file
	Args connection: Open connection to the server

### disconnect(connection) 
	Closes the open connection to the server

	Args connections: The open connection to the server

	Returns a string.

	Possible return values:
		"Disconnected"
		"No reply from server"

### receivePred(connection) 
	Receive a prediction from the server.
 	
	Args connection: Open connection to the server

	returns a 1 byte string
		possible return values:
			'P' - Indicates pneumonia detected
			'N' - Indicates that everything is normal
 

