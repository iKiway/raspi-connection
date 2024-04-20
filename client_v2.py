import socket
import time

HOST = '192.168.178.157'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = "Hello, server! This is a client."
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"Received from server: {data.decode()}")
    time.sleep(20)
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"Received from server: {data.decode()}")
    s.close()
    
