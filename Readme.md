Sercli Chat Application

Sercli chat application is designed with the python language which allows two or more clients /people to join the chat. It allows clients to send messages to all the clients in the chat room.
I have used a socket module that plays a major role in connection and communication.

Here the major role of the server is to listen for requesting client connections and updating the client socket list based on the connection acceptance of the clients. Also for each client connected to the server a new thread is started for listening for upcoming messages from the clients.

The client-side code initially connects to the server and continually listens for the message from the server and prints the broadcasted messages to the console. Each client can proceed with the chat by giving an input message to the console which is then sent to the server.
