# join.py
import socket
import time


account = False
try:
    open("config.txt", "r")
    account = True
    with open("config.txt", "r") as f:
        name = f.read()
        username = "@" + name + ": "
        print(f"Welcome {name}")
except:
    print("cannot find account please register through 'account.py'")


def connect():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter server IP: ")
    port = int(input("Enter server port: "))

    try:
        client_socket.connect((host, port))
        print("Connected to the server.")
        
        while True:
            message = input("Enter message to send to the server (or 'exit' to quit): ")
            if message.lower() == 'exit':
                print("Closing connection.")
                time.sleep(1)
                break

            client_socket.sendall(username.encode() +  message.encode())
            data = client_socket.recv(1024)
            print(data.decode())

    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    connect()
