import socket
import random
from threading import Thread
from datetime import datetime

# server's IP address
SERVER_SIDE_HOST = "127.0.0.1"
SERVER_SIDE_PORT = 6149 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize TCP socket
ser = socket.socket()
print(f"Connecting to {SERVER_SIDE_HOST} : {SERVER_SIDE_PORT}")
# connect to the server
ser.connect((SERVER_SIDE_HOST, SERVER_SIDE_PORT))
print("Connected successfully.")
print("Welcome to sercli app")
name = input("Enter your name -  ")
def listen_for_messages():
    while True:
        message = ser.recv(1024).decode()# receives messages from server
        print("\n" + message)# prints on console 

# thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()
while True:
    # input message we want to send to the server
    to_send =  input()
    # to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"[{date_now}] {name}{separator_token}{to_send}"
    # finally, send the message
    ser.send(to_send.encode())

# close the socket
ser.close()
