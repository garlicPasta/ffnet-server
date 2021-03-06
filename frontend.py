from SocketServer import TCPServer, BaseRequestHandler

HOST, PORT = "localhost", 9999


class SetServer():
    # Create the server, binding to localhost on port 9999
    def __init__(self):
        self.queue = []
        self.server = TCPServer((HOST, PORT), MyTCPHandler)
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        self.server.serve_forever()

    def handle_timeout(self):
        pass



"""
The RequestHandler class for our server.

It is instantiated once per connection to the server, and must
override the handle() method to implement communication to the
client.
"""

class MyTCPHandler(BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.queue.append(self.data)
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


server = SetServer()






