def validate_password(password):
    correct_len = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    if len(password) > 8:
        correct_len = True
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digit = True

    if correct_len and has_uppercase and has_lowercase and has_digit:
        valid = True
        return valid


def main():
    while True:
        password = input("Enter password: ")
        while not validate_password(password):
            password = input("Enter a valid password: ")
        re_password = input('Re-enter password: ')
        if re_password != password:
            print('Password Does Not match!!')
            continue


def validate_pin(pin):
    correct_len = False
    has_digit = False

    if len(pin) == 4:
        correct_len = True
    for ch in pin:
        if ch.isdigit():
            has_digit = True

    if has_digit and correct_len:
        valid = True
        return valid


def pass_exceed_check(pin):
    count = 0
    while count < 4:
        user_pin = input('Enter pin: ')
        if user_pin == pin:
            print("Correct Pin Entered")
            break
        else:
            print("Invalid Pin Entered")
            count += 1
    else:
        print("Maximum limit exceeded")


# CHAT
# SERVER
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 9000))

server.listen()
client, address = server.accept()

done = False

while not done:
    msg = client.recv(1724).decode('utf-8')
    if msg == 'quit':
        done = True
        break
    else:
        print(msg)
    client.send(input('Message: ').encode('utf-8'))

client.close()
server.close()

# CLIENT
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9000))

done = False

while not done:
    client.send(input("Message: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
        break
    else:
        print(msg)
