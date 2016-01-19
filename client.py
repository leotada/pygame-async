import socket
import sys

HOST, PORT = "localhost", 9999


class Client():
    def __init__(self):
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        self.sock.connect((HOST, PORT))
        
    def update(self, data):
        self.sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server
        received = str(self.sock.recv(1024), "utf-8")
        
        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        
    def __del__(self):
        self.sock.close()
