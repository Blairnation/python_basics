look_up = 1
add = 2
change = 3
delete = 4
quit_choice = 5


def main():
    birthdays = {}

    while True:
        choice = choice_menu()
        if choice == look_up:
            look_birthday(birthdays)
            print(birthdays)
        elif choice == add:
            add_birthday(birthdays)
            print(birthdays)
        elif choice == change:
            change_birthday(birthdays)
            print(birthdays)
        elif choice == delete:
            delete_birthday(birthdays)
            print(birthdays)
        elif choice == quit:
            print('Quiting...')
            break


def choice_menu():
    print('''1.look up
2.add birthday
3.change birthday
4.delete birthday
5.quit ''')

    choice = int(input("Enter choice: "))
    while choice < look_up or choice > quit_choice:
        choice = int(input("Enter a valid choice: "))
    return choice


def look_birthday(birthdays):
    name = input('Name: ')
    if name in birthdays:
        print(birthdays[name])
    else:
        print('Name not available')


def add_birthday(birthdays):
    name = input("Enter name: ")
    birthday = input("Enter birthday: ")

    if name not in birthdays:
        birthdays[name] = birthday
    else:
        print('Name already exists')


def change_birthday(birthdays):
    name = input("Enter name: ")
    birthday = input("Enter new birthday")
    if name in birthdays:
        birthdays[name] = birthday
    else:
        print("Name not available")


def delete_birthday(birthdays):
    name = input("Enter name: ")
    if name in birthdays:
        del name
    else:
        print("Name unavailable or already deleted")


main()
