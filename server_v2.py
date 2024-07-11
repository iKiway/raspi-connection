import socket
import threading
import json
import struct

HOST = ''  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
def decode_mutf8_to_utf8(mutf8_bytes):
    # Convert MUTF-8 to UTF-8 where needed
    utf8_bytes = bytearray()
    i = 0
    while i < len(mutf8_bytes):
        byte = mutf8_bytes[i]
        if byte == 0xC0 and i + 1 < len(mutf8_bytes) and mutf8_bytes[i + 1] == 0x80:
            utf8_bytes.append(0x00)  # Convert null character representation
            i += 2
        else:
            i += 1
    return utf8_bytes.decode('utf-8')


def message_processing(message):
    """Processes a message received from a client."""
    # message = json.loads(message)
    try:
        if message["message"] == "Hello, Server!":
            return f"Message received: {message['data']}"
        elif message["number"] == 42:
            return f"Command received: {message['data']}"
        else:
            return "Unknown message type"
    except json.JSONDecodeError:
        return "Invalid JSON"

try:
    def handle_client(conn, addr):
        """Handles a client connection by receiving and responding to messages."""
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            test = decode_mutf8_to_utf8(data)
            print(test)
            print(f"Received: {test.decode()[2:]}")
            # print(message_processing(data.decode()[2:]))
            
            # Required to send the size of the data before sending the data, because of the kotlin app, that requres modified utf8
            response = f"Hello, {addr}! You sent: {data.decode()}"
            response = data.decode()
            response = "lskdjflkkjsdfl"
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