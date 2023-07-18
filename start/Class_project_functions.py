import pickle
import Class_project_class as contact

lookup = 1
Add = 2
Change = 3
Delete = 4
Quit = 5

FILENAME = 'dic_class_contacts.dat'


def main():
    contacts = load_contacts()
    while True:
        choice = menu_choice()
        if choice == lookup:
            look_up(contacts)
        elif choice == Add:
            add(contacts)
        elif choice == Change:
            change(contacts)
        elif choice == Delete:
            delete(contacts)
        elif choice == Quit:
            save_contact(contacts)
            print(f'Contacts saved to {FILENAME}')
            print('Program quiting...')
            break


def load_contacts():
    try:
        infile = open(FILENAME, 'rb')
        dic = pickle.load(infile)
        infile.close()
    except IOError:
        dic = {}
    return dic


def save_contact(contacts):
    outfile = open(FILENAME, 'wb')
    pickle.dump(contacts, outfile)
    outfile.close()


def look_up(contacts):
    name = input('Enter name: ')
    if name in contacts:
        print(contacts[name])
    else:
        print("That name not found")


def menu_choice():
    print('MENU')
    print("______")
    print('''1.look up a contact
2.Add a new contact
3.Change a  contact
4.Delete a contact
5.Quit the program ''')
    print()
    choice = int(input("Enter choice: "))
    while choice < lookup or choice > Quit:
        choice = int(input("Enter a valid choice"))
    return choice


def add(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    entry = contact.Contact(name, phone, email)
    if name not in contacts:
        contacts[name] = entry
        print("Information added")
    else:
        print("Name already exists")


def change(contacts):
    name = input("Enter name: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        entry = contact.Contact(name, phone, email)

        contacts[name] = entry
        print('Information updated')
    else:
        print("Name doesn't exit")


def delete(contacts):
    name = input('Enter name: ')
    if name in contacts:
        del contacts[name]
        print('Contact information deleted')
    else:
        print("Name doesn't exist")





# copy

import pickle
from Class_project_class import Contact

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

