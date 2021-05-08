## Requirements

1. ConfigParser
2. tensorflow
3. numpy
4. opencv

## Configuration

The configuration files contains settings to setup the server

The first configuration option should be set to the servers external ip, unless using it for local usage only, then the default can be used

HOST = "94.7.190.69"

The port should be any free port on the system and sufficient firewall rules setup to allow traffic on the specified port

PORT = "50022"

## Commands

The server will listen for specific commands.

Before sending a command, the server will send "?" to see if the client is connected still.
Receive and handle this before sending a command.

All commands are 4 bytes and after a command is sent a response will be 1 byte response will be sent back indicating 
an error or success. Success is indicated by a reply of 0.

The server will timeout after 20 seconds of not receiving a command and will close the connection.

1) FILE

Sending a packet containing the text "FILE" will let the server know that the next incoming data will be a file

After sending the command FILE the server will respond with 0 indicating that it is okay to send the next packet.

After receiving the reply, the server expected the size of the file as the next command. The buffer for the file size is 10 bytes, so if needed add some characters to fill the buffer. The server will handle this and remove them.

Once the server has received the file size it will start listening for the incoming image data. The image data should 
be sent over in 1 byte chunks. This is subject to change in the future.


2) MODE

This will let the server know that the next incoming data will be the requested model to run the predictions on.

Once the command has been sent. Handle the incoming response accordingly which will be 0 indicatign succes.

The buffer for the incoming model is 4 bytes: These can be the following:

1. INCE - Request the inception model
2. DENS - Request the densenet model
3. MYCN - Request our CNN model
4. VGG! - Request the VGG model
5. XCEP - Request the EXEP model
6. ENSE - Reqiest the ensembled model

if the model is incorrect the server will return error code 3. Otherwise if the model received is an appropriate
model, server returns code 0.

3) PRED

Sending "PRED" will inform the server that you want the prediction based on the model requested and file sent

Once the server has received the PRED command, the server will return a code to indicate it's success.

After which the server will send a 1 byte packet to the client which will either be P or N.

P being pneumonia detected
N being the image is normal

Handle these on the client

4) BYE

Server will close the connection and wait for the next one.



## Return Codes

0: Success

1: Model or image file hasn't been sent

2:

3: Invalid model


## TODO

These items are requirements to implement but where lower on the priority list

[] Check hash sum of the file and return 0 for match 4 for mismatch

[] Check that the file we received is a valid image file. Return 5 for invalid image

[] Security: Impliment ssh keys to only allow authorised apps.. Could be stolen?

[] Security: Limit the amount of connections from host.


