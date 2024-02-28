import socket

class UDPSender:
    def __init__(self, ip='127.0.0.1', port=5065):
        self.ip = ip
        self.port = port
        self.addr = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

    def send_message(self, message):
        self.sock.sendto(message.encode(), self.addr)

if __name__ == "__main__":
    # Quick test
    sender = UDPSender()
    sender.send_message("Hello Unity!")
