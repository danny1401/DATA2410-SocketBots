import socket
import threading
from chatbot import *

HOST = 'localhost'
PORT = 5051

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] Connection from: {addr}")
    conn.send("Server: Hello Client, please type in the name of the bot you want to speak to: "
              "[Alice] [Bob] [Dora] [Chuck]".encode())

    while conn:
        chooseBot = conn.recv(1024).decode()
        if (chooseBot == "Alice") or (chooseBot == "alice"):
            print(f"Client {addr} has been assigned to Alice")
            conn.send("Alice: Hello there! What are you interested in doing today? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "!quit":
                    conn.send("Alice: It has been a pleasant experience getting to know you! Farewell "
                              "\nYou've been disconnected from the chatbot. "
                              "Feel free to chat with another bot or "
                              "disconnect from the server (\x1B[3m!quit\x1B[0m).".encode())
                    print(f"[DISCONNECTED] {addr} has disconnected from the chatbot.")
                    connected = False

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Alice: {alice(reply)}".encode())
        if (chooseBot == "Bob") or (chooseBot == "bob"):
            print(f"Client {addr} has been assigned to Bob")
            conn.send("Bob: Hey, what do you want to do? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "!quit":
                    conn.send("Bob: See you later! "
                              "\nYou've been disconnected from the chatbot. "
                              "Feel free to chat with another bot or "
                              "disconnect from the server (\x1B[3m!quit\x1B[0m).".encode())
                    print(f"[DISCONNECTED] {addr} has disconnected from the chatbot.")
                    connected = False

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Bob: {bob(reply)}".encode())
        if (chooseBot == "Dora") or (chooseBot == "dora"):
            print(f"Client {addr} has been assigned to Dora")
            conn.send("Dora: Hello, what do you want to do today? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "!quit":
                    conn.send("Dora: Take care! "
                              "\nYou've been disconnected from the chatbot. "
                              "Feel free to chat with another bot or "
                              "disconnect from the server (\x1B[3m!quit\x1B[0m).".encode())
                    print(f"[DISCONNECTED] {addr} has disconnected from the chatbot.")
                    connected = False

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Dora: {dora(reply)}".encode())
        if (chooseBot == "Chuck") or (chooseBot == "chuck"):
            print(f"Client {addr} has been assigned to Chuck")
            conn.send("Chuck: Hello, what can i help you with? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "!quit":
                    conn.send("Chuck: Goodbye! Hope we meet again! "
                              "\nYou've been disconnected from the chatbot. "
                              "Feel free to chat with another bot or "
                              "disconnect from the server (\x1B[3m!quit\x1B[0m).".encode())
                    print(f"[DISCONNECTED] {addr} has disconnected from the chatbot.")
                    connected = False

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Chuck: {chuck(reply)}".encode())
        chooseBot = conn.recv(1024).decode()

        if chooseBot == "!quit":
            conn.send("[DISCONNECTED] You have been disconnected from the server.".encode())
            print(f"[DISCONNECTED] {addr} has disconnected from the server.")
            break

        else:
            conn.send("Chatbot: Please try again. \x1B[3m(Type !quit to disconnect the server)\x1B[0m".encode())
            continue
    conn.close()


def start():
    s.listen(10)
    print(f"[LISTENING] Server is listening on {HOST}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def sendAllClients():
    s.sendall()


print("[STARTING] Server is starting...")
start()
