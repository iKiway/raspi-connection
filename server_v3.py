import socket
import threading
import json
import struct
import os

HOST = ''  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def swich_station(station):
    with open('test.txt', 'w') as file:
        file.write(station)

def set_wifi(wifi):
    wifiName = wifi["name"]
    wifiPassword = wifi["password"]
    os.system(f"sudo raspi-config nonint do_wifi_ssid_passphrase {wifiName} {wifiPassword} [hidden] [plain] 2>&1")

def writeUTF(data):
    """Decodes a modified UTF-8 encoded message to UTF-8."""
    length = struct.unpack("!H", data[:2])[0]
    return data[2:].decode('utf8')

def message_processing(message):
    """Processes a message received from a client."""
    try:
        message_json = json.loads(message)
        for obj in message_json:
            if obj == "station":
                swich_station(message_json[obj])
                return "Station changed"
            if obj == "wifi":
                set_wifi(message_json[obj])
                return "Wifi changed"
            else: 
                return "Unknown message type"
    except json.JSONDecodeError:
        return message

try:
    def handle_client(conn, addr):
        """Handles a client connection by receiving and responding to messages."""
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            print(data.decode())
            test = writeUTF(data)
            print(test)
            print(f"Received: {test}")
            response = message_processing(test)
            
            # Required to send the size of the data before sending the data, because of the kotlin app, that requres modified utf8
            # response = f"Hello, {addr}! You sent: {data.decode()}"
            # response = data.decode()
            # response = "lskdjflkkjsdfl"
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