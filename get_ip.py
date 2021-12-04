import socket

class GetIp:
    
    def __init__(self):
        self.ip_local = socket.gethostbyname(socket.gethostname())

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))

        self.ip_lan = s.getsockname()[0]
        s.close()

    def get_ip_local(self):
        return self.ip_local

    def get_ip_lan(self):
        return self.ip_lan

gp = GetIp ()
print(gp.get_ip_lan())