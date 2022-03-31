import socket

HOST = 'localhost'
PORT = 5052

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = client.recv(1024).decode()
    print(f"{msg}")

    connected = True
    while connected:
        reply = input("Me: ")
        if reply == "--disconnect":
            client.close()
            break

        else:
            client.send(reply.encode())
            print(f"{client.recv(1024).decode()}")
    break
