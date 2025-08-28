import sys
import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


import socket
import threading


HOST = '127.0.0.1'
PORT = 5555

clients = []
usernames = []


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
            # Save chat to log
            with open("chat_log.txt", "a") as f:
                f.write(message.decode('utf-8') + "\n")
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} left the chat.".encode('utf-8'), client)
            usernames.remove(username)
            break


def receive():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server running on {HOST}:{PORT}...")

    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username of the client is {username}")
        broadcast(f"{username} joined the chat!".encode('utf-8'), client)
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
