import socket
import threading
import time


def handle_client(client):

    while True:
        msg = client.recv(1024).decode('utf-8')
        if msg == 'quit':
            print("Server Disconnecting...")
            break
        else:
            print(f'kwasi: {msg}')
            print()
        response = input('You: ').encode('utf-8')
        client.send(response)
    client.close()


def connect_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 5000

    server.bind((host, port))

    server.listen()
    print('Server Connectivity Available')
    print("Waiting For Connection...")
    time.sleep(3)

    while True:
        client, address = server.accept()
        print(f'Server Connected to {address} Successfully')
        print()

        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()


if __name__ == '__main__':
    connect_server()

# CLient Side

import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))

    while True:
        send = input('You: ').encode('utf-8')
        client.send(send)
        msg = client.recv(1024).decode('utf-8')
        if msg == 'quit':
            print('Server Disconnecting...')
            break
        else:
            print()
            print(f'Kwadwo: {msg}')
            print()
    client.close()


if __name__ == '__main__':
    main()
