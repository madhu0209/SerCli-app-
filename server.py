import socket
import select
from threading import Thread

# to mention server IP address
SERVER_SIDE_HOST = "0.0.0.0"
SERVER_SIDE_PORT = 6149 # port we want to use
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize list of all connected client's sockets
client_sockets = set()
# create a Ipv4 format and TCP socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# make the port as reusable port for binding multiple sockets , set before address is bound to the socket 
ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
ser.bind((SERVER_SIDE_HOST, SERVER_SIDE_PORT))
# listen for upcoming connections
ser.listen(5)
print(f"Listening on process with {SERVER_SIDE_HOST} : {SERVER_SIDE_PORT}")

def listen_for_client_connection(cser):
    # This function keep listening for a message from `cser` socket,When a message is received, broadcast it to all other connected clients
     while True:
        try:
            # keep listening for a message from `cser` socket
            msg = cser.recv(1024).decode()
        except Exception as e:
            # client no longer connected,remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cser)
        else:
            # if received a message, replace the <SEP> 
            msg = msg.replace(separator_token, " - ")
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # send the message
            client_socket.send(msg.encode())

while True:
    # listening for new connections all the time
    client_socket, client_address = ser.accept()
    print(f"Accepted new client - {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client_connection, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
    # close client sockets
for cser in client_sockets:
    cser.close()
# close server socket
ser.close()
