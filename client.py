__author__ = 'jakob'

import socket
import sys

HOST, PORT_set, PORT_get = "localhost", 8888, 9999


class ann_client():

    def __init__(self):
        # self.set_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.set_sock.connect((HOST, PORT_send))
        self.get_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.get_sock.connect((HOST, PORT_get))

    def set_ann(self):
        pass

    def call_ann(self, input):
        self.get_sock.sendall(input + "\n")
        received = self.get_sock.recv(1024)
        print "Received: {}".format(received)
        return received

    def disconnect(self):
        #self.set_socksock.close()
        self.get_sock.close()

if __name__ == '__main__':
    client = ann_client()
    client.call_ann("Hallo Welt")
