import socket
import asyncio
import json

HOST, PORT = "localhost", 9999


class Network():
    def connect(self):
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        self.sock.connect((HOST, PORT))
        
    def login(self, username):
        "Send login info"
        data = {'action': 'login', 'id': username}
        self.sock.sendall(bytes(json.dumps(data), "utf-8"))
        received = str(self.sock.recv(1024), "utf-8")
        
    def update(self, data):
        self.sock.sendall(bytes(data, "utf-8"))

        # Receive data from the server
        received = str(self.sock.recv(1024), "utf-8")
        
        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        return received
        
    def __del__(self):
        self.sock.close()
