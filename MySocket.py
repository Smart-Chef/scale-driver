import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 10001


class MySocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

    def connect(self):
        self.sock.connect((UDP_IP, UDP_PORT))

    def mysend(self, message):
        self.sock.sendto(message, (UDP_IP, UDP_PORT))
