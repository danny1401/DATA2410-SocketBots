import socket
import threading
from chatbot import *

HOST = 'localhost'
PORT = 5052

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

listClients = []


def helpMessage(conn):
    helpMSG = "Chatbot Description:" \
              "\nIn this application, there's 4 different chatbots you can choose to talk to. " \
              "This can be done by typing their name in the command line. " \
              "\nThese bots are able to respond to you, based what to say to them." \
              "\n " \
              "\nList of instructions:" \
              "\n* Type --list to get a list of all the connected clients." \
              "\n* Type --bcON to turn on broadcast mode. You will be able to broadcast your " \
              "message to every available client on the server until you turn this mode off." \
              "\n* Type --bcOFF to turn off broadcast mode." \
              "\n* Type --leave to disconnect from the chatbot." \
              "\n* Type --disconnect to disconnect from the server." \
              "\n "
    helpEncoded = helpMSG.encode()
    conn.send(helpEncoded)


def disconnect(conn, addr):
    conn.send("[DISCONNECTED] You have been disconnected from the server.".encode())
    print(f"[DISCONNECTED] {addr} has disconnected from the server.")
    listClients.remove(addr)


def printList(conn):
    print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")
    print("List of Clients:")
    printMSG = "List of Clients:"
    for clients in listClients:
        printMSG += f"\n{clients}"
        print(clients)
    printMSG += "\n"
    helpEncoded = printMSG.encode()
    conn.send(helpEncoded)


def shutdown():
    print("Shutting down the server...")
    for client in listClients:
        client.send("test").encode()


def client_control(conn, addr):
    print(f"[NEW CONNECTION] Connection from: {addr}\n")
    listClients.append(addr)
    firstMessage = "Server: Hello Client! If you need any help, please type --help for more info.\n" \
                   "Server: Feel free to type in the name of the bot you want to talk to: " \
                   "[Alice] [Bob] [Dora] [Chuck]"
    conn.send(firstMessage.encode())

    while conn:
        chooseBot = conn.recv(1024).decode()
        if (chooseBot == "Alice") or (chooseBot == "alice"):
            print(f"Client {addr} has been assigned to Alice")
            conn.send("Alice: Hello there! What are you interested in doing today? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "--help":
                    helpMessage(conn)
                elif reply == "--list":
                    printList(conn)
                elif reply == "--leave":
                    conn.send("Alice: It has been a pleasant experience getting to know you! Farewell "
                              "\nServer: You have left the chatbot. Feel free to chat with another bot.".encode())
                    connected = False
                elif reply == "--disconnect":
                    disconnect(conn, addr)
                    break

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Alice: {alice(reply)}".encode())
        elif (chooseBot == "Bob") or (chooseBot == "bob"):
            print(f"Client {addr} has been assigned to Bob")
            conn.send("Bob: Hey, what do you want to do? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "--help":
                    helpMessage(conn)
                elif reply == "--list":
                    printList(conn)
                elif reply == "--leave":
                    conn.send("Bob: See you later! "
                              "\nServer: You have left the chatbot. Feel free to chat with another bot.".encode())
                    connected = False
                elif reply == "--disconnect":
                    disconnect(conn, addr)
                    break

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Bob: {bob(reply)}".encode())
        elif (chooseBot == "Dora") or (chooseBot == "dora"):
            print(f"Client {addr} has been assigned to Dora")
            conn.send("Dora: Hello, what do you want to do today? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "--help":
                    helpMessage(conn)
                elif reply == "--list":
                    printList(conn)
                elif reply == "--leave":
                    conn.send("Dora: Take care! "
                              "\nServer: You have left the chatbot. Feel free to chat with another bot.".encode())
                    connected = False
                elif reply == "--disconnect":
                    disconnect(conn, addr)
                    break

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Dora: {dora(reply)}".encode())
        elif (chooseBot == "Chuck") or (chooseBot == "chuck"):
            print(f"Client {addr} has been assigned to Chuck")
            conn.send("Chuck: Hello, what can i help you with? "
                      "(try to write a verb in pre tense form)".encode())

            connected = True
            while connected:
                reply = conn.recv(1024).decode()

                if reply == "--help":
                    helpMessage(conn)
                elif reply == "--list":
                    printList(conn)
                elif reply == "--leave":
                    conn.send("Chuck: Goodbye! Hope we meet again! "
                              "\nServer: You have left the chatbot. Feel free to chat with another bot.".encode())
                    connected = False
                elif reply == "--disconnect":
                    disconnect(conn, addr)
                    break

                else:
                    print(f"Client {addr}: {reply}")
                    conn.send(f"Chuck: {chuck(reply)}".encode())

        elif chooseBot == "--help":
            helpMessage(conn)

        elif chooseBot == "--list":
            printList(conn)

        elif chooseBot == "--shutdown":
            shutdown()

        elif chooseBot == "--bcON":
            conn.send("Server: Broadcast Mode is turned on. "
                      "You are now able to broadcast messages across all clients.".encode())
            broadcastMode = True
            while broadcastMode:
                reply = conn.recv(1024).decode()
                if reply == "--help":
                    helpMessage(conn)
                elif reply == "--list":
                    printList(conn)
                elif reply == "--bcOFF":
                    conn.send("Server: Broadcast Mode is turned off.".encode())
                    broadcastMode = False
                elif reply == "--disconnect":
                    disconnect(conn, addr)
                    break

                else:
                    print(f"Broadcast Message {addr}: {reply}")
                    for clients in listClients:
                        clients.send(f"From {addr}: {reply}".encode())

        elif chooseBot == "--leave":
            conn.send("Server: You are not talking to any chatbots at the moment.".encode())

        elif chooseBot == "--disconnect":
            disconnect(conn, addr)
            conn.close()
            break

        else:
            conn.send("Server: Please try again. \x1B[3m(Type --help for more info)\x1B[0m".encode())


def start():
    s.listen()
    print(f"[LISTENING] The server is listening on {HOST}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=client_control, args=(conn, addr))
        thread.start()


print("[STARTING] The server is starting...")
start()
