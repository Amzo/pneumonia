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

1) FILE

Sending a packet containing the text "FILE" will let the server know that the next incoming data will be a file

2) MODEL

This will let the server know that the next incoming data will be the requested model to run the predictions on

3) PRED

Sending "PRED" will inform the server that you want the prediction based on the model requested and file sent

4) BYE

Server will close the connection and wait for the next one.



