import socket
import pickle


class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.180"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p_id = self.connect()

    def get_p_id(self):
        return self.p_id

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            frame = pickle.loads(self.client.recv(4096))
            return frame
        except socket.error as e:
            print(e)
