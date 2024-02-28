from communication.udp_sender import UDPSender
import threading
from communication.udp_receiver import start_udp_receiver

def main():
    # Define the IP and port for the UDP receiver
    IP = "127.0.0.1"  # Localhost (for testing purposes)
    PORT = 5065       # Port number to listen on

    # Start the UDP receiver in a background thread
    udp_thread = threading.Thread(target=start_udp_receiver, args=(IP, PORT), daemon=True)
    udp_thread.start()
    print("UDP Receiver is running in a background thread.")

    # Initialize the UDP sender
    udp_sender = UDPSender()

    # Main application loop
    try:
        while True:
            # Your hand tracking and gesture recognition loop
            gesture = "some_gesture"  # Placeholder for gesture recognition logic
            udp_sender.send_message(gesture)
    except KeyboardInterrupt:
        print("Application terminated by user.")

if __name__ == "__main__":
    main()
