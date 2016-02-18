import asyncio
import json
from gameobjects.vector2 import Vector2

connected_clients = 0
clients = {}


class Client(object):
    def __init__(self, id):
        self.id = id
        self.pos = [0, 0]
        

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        global connected_clients
        connected_clients += 1
        print('Connection from {}'.format(peername))
        print('Clientes conectados: {}'.format(connected_clients))
        self.transport = transport

    def data_received(self, data):
        global clients
        #~ import pdb; pdb.set_trace()
        message = json.loads(data.decode())
        #print('Data received: {!r}'.format(message))
        
        # login
        if message['action'] == 'login':
            clients[message['id']] = Client(message['id'])
        elif message['action'] == 'update':
            clients[message['id']].pos = message['pos']

        #print('Send: {!r}'.format(message))
        data = json.dumps([v.__dict__ for v in clients.values()])
        self.transport.write(bytes(data, "utf-8"))

        #print('Close the client socket')
        #self.transport.close()

loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 9999)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
