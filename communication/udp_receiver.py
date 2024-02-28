import socket

def start_udp_receiver(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.bind((ip, port))
    print(f"Listening on UDP {ip}:{port}")

    try:
        while True:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            print(f"Received message: {data.decode()} from {addr}")
    except KeyboardInterrupt:
        print("\nReceiver terminated.")
    finally:
        sock.close()

if __name__ == "__main__":
    IP = "127.0.0.1"  # Localhost (for testing purposes)
    PORT = 5065       # The same port as used by the sender
    start_udp_receiver(IP, PORT)
