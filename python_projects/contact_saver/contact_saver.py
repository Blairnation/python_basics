import pickle
from contact_saver_class import Contact

FILENAME = 'dic_class_contacts.dat'
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    diction = load_info()
    while True:
        try:
            print()
            option = menu()
            if option == LOOK_UP:
                look_up(diction)
            if option == ADD:
                add(diction)
            if option == CHANGE:
                change(diction)
            if option == DELETE:
                delete(diction)
            if option == QUIT:
                save(diction)
                print('Program quiting...')
                break
        except ValueError as error:
            print(error)
            print('Enter the options available')


def load_info():
    try:
        infile = open(FILENAME, 'rb')
        dic = pickle.load(infile)
        infile.close()
    except IOError:
        dic = {}

    return dic


def menu():
    print('''MENU
________
1. Look up info
2.Add info
3.Change info
4.Delete info
5.Quit''')

    option = int(input('Enter option: '))
    while option < LOOK_UP or option > QUIT:
        option = int(input("Enter a valid option: "))

    return option


def look_up(diction):
    print('Enter name to view information')
    name = input('Enter name: ')
    if name in diction:
        print(diction[name])
    else:
        print('Name not available!!')


def add(diction):
    print("Enter information to store")
    name = input("Enter name: ")
    if name not in diction:
        phone = input("Enter phone number: ")
        email = input('Enter email: ')
        info = Contact(name, phone, email)
        diction[name] = info

    else:
        print("Name already exist!!")


def change(diction):
    print('Enter information to change')
    name = input("Enter name: ")
    if name in diction:
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        info = Contact(name, phone, email)
        diction[name] = info
        print("Information updated")
    else:
        print('Name not found!!')


def delete(diction):
    print("Enter name to delete information")
    name = input('Enter name: ')
    if name in diction:
        del diction[name]
        print('Information deleted')
    else:
        print("Name not found!!")


def save(diction):
    outfile = open(FILENAME, 'wb')
    pickle.dump(diction, outfile)
    outfile.close()


main()