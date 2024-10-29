# server.py
import socket
import random
import threading


#Handles all the people connected to the server
connected = []

def handle_client(client_socket, addr):
    print(f"Connected by {addr}")
    connected.append(client_socket)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            for connection in connected:
                if connection != client_socket:
                    try:
                        connected.sendall(data)
                    except BrokenPipeError:
                        print(f"Connection with {addr} lost.")
                        break
                
            client_socket.sendall(data)
        except ConnectionResetError:
            print(f"Connection with {addr} lost.")
            break
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '172.20.10.3'
    port = 65432
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server Settings: \n IP: {host} \n Port: {port}")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
