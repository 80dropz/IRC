# server.py
import socket
import random
import threading
import subprocess


#basic grabbing the ip to host the server on local machine but the server is public


#MacOS version
iplist = subprocess.run(["ifconfig | grep 'inet ' | awk '{print $2}'"], capture_output=True, text=True, shell=True)
iplines = iplist.stdout.splitlines()
print(len(iplines))
ip = iplines[1]
ipconfig1 = iplines[0]
print(ipconfig1)
print(ip)

#Windows version


#Handles all the people connected to the server
connected = []

def handle_client(client_socket, addr):
    print(f"Connection by {addr}")
    connected.append(client_socket)
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")

            # Broadcast data to other clients
            for connection in connected:
                if connection != client_socket:
                    try:
                        connection.sendall(data)
                    except BrokenPipeError:
                        print(f"Lost connection with a client.")
                        connected.remove(connection)
                
        client_socket.close()
    except ConnectionResetError:
        print(f"Connection with {addr} lost.")
    finally:
        #ensures the client is removed from the connections list
        connected.remove(client_socket)
        client_socket.close()



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ip
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
