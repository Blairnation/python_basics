import socket
import threading


def handle_client(client):
    while True:
        msg = client.recv(1024).decode('utf-8')
        if msg == 'quit':
            break
        else:
            print(msg)
        snd_msg = input("Message: ").encode('utf-8')
        client.send(snd_msg)
    client.close()


def connect():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('localhost', 5006))
    server.listen()
    print('Server Active Waiting For Connections')

    while True:
        client, address = server.accept()
        print(f'{address} Connected to Server successfully')
        print()
        server_thread = threading.Thread(target=handle_client, args=(client,))
        server_thread.start()


if __name__ == '__main__':
    connect()
