import socket
import threading
import json
import struct

HOST = ''  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

try:
    def handle_client(conn, addr):
        """Handles a client connection by receiving and responding to messages."""
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            
            # Required to send the size of the data before sending the data, because of the kotlin app, that requres modified utf8
            response = f"Hello, {addr}! You sent: {data.decode()}"
            response_data = bytearray(response, 'utf8')
            size = len(response_data)
            conn.sendall(struct.pack("!H", size))
            conn.sendall(response_data)
        conn.close()
        print(f"Client {addr} disconnected")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
except Exception as e:
    print("Error in server_v2.py" + e)