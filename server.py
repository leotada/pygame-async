import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.wfile.write(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
