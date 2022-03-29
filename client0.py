import socket

HOST = 'localhost'
PORT = 5051

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = client.recv(1024).decode()
    print(f"ChatBot: {msg}")

    connected = True
    while connected:
        reply = input("Me: ")
        client.send(reply.encode())
        print(f"{client.recv(1024).decode()}")
