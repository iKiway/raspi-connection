import socket
import time

HOST = '10.42.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = "Hello, server! This is a client."
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"Received from server: {data.decode()}")
    time.sleep(2)
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"Received from server: {data.decode()}")
    s.close()
    
