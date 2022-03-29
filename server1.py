import socket

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))  # BOT PARAMETER NEEDED
print("[STARTING] Server is starting...")

s.listen()
print(f"[LISTENING] Server is listening on {HOST}")

conn, addr = s.accept()
print(f"[NEW CONNECTION] Connection from: {addr}")
conn.send("Hello Client, how can I help you?".encode())

while conn:
    recv_msg = conn.recv(1024).decode()
    print(f"Client [{addr}]: {recv_msg}")


    if recv_msg == "!KILL":
        conn.send("It has been a pleasant experience getting to know you! Farewell".encode())
        print(f"[DISCONNECTED] {addr} has disconnected from the server.")
        break

s.close()