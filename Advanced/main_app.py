import pickle
import time

from momo_db import *
import sqlite3


def main():
    print("Dial *170# to view options")
    while True:
        dial = input("Dial: ")
        if dial != '*170#':
            print('Invalid Input !!!')
            break

        print('SIM Requesting...')
        time.sleep(4)
        print()
        greeting()
        menu1()
        break
    print('Program Quiting', end='')
    print('..', end='')
    time.sleep(1)
    print('..', end='')
    time.sleep(1)
    print('..', end='')
    time.sleep(1)
    print('..', end='')


def menu1():
    while True:
        print('OPTIONS')
        print('1.Register MOMO Account\n'
              '2.Look Up Details\n'
              '3.Update Details\n'
              '4.Delete MOMO Account\n'
              '5.My wallet\n'
              '6.Quit')
        option = int(input("Enter option: "))
        while option < 1 or option > 5 and option != 6:
            option = int(input("Select a valid option: "))

        if option == 1:
            print('Please wait...')
            time.sleep(3)
            print()
            register()

        elif option == 2:
            print('Please wait...')
            time.sleep(3)
            print()
            look_up()

        elif option == 3:
            print('Please wait...')
            time.sleep(3)
            print()
            update()

        elif option == 4:
            print('Please wait...')
            time.sleep(3)
            print()
            delete()

        elif option == 5:
            print('Please wait...')
            time.sleep(2)
            menu2()

        time.sleep(1)
        return


def menu2():
    while True:
        time.sleep(1)
        print()
        print('Menu')
        print('1.Transfer Money\n'
              '2.Deposit Money\n'
              '3.Redraw Money\n'
              '4.Check Balance\n'
              '5.Change Pin\n'
              '6.Go Back To Main Menu')
        option = int(input("Select option: "))
        while option < 1 or option > 6:
            option = int(input("Enter options available: "))

        if option == 1:
            print('Please wait...')
            time.sleep(3)
            print()
            transfer()
        elif option == 2:
            print('Please wait...')
            time.sleep(3)
            print()
            deposit()
        elif option == 3:
            print('Please wait...')
            time.sleep(3)
            print()
            redraw()
        elif option == 4:
            print('Please wait...')
            time.sleep(3)
            check_balance()
        elif option == 5:
            print('Please wait...')
            time.sleep(3)
            print()
            change_pin()
        elif option == 6:
            print('Please wait...')
            time.sleep(3)
            print()
            menu1()
            break

        back = int(input('Press 0 To GO Back OR Any Digit To Quit: '))
        if back != 0:
            break


def transfer():
    phone_num = input('Enter Your Phone Number: ')
    pin = input('Enter Pin: ')

    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute(f'SELECT momo_account FROM users WHERE '
              f'phone_number = "{phone_num}" AND '
              f'pin = {pin}')
    binary_file = c.fetchone()
    conn.commit()
    conn.close()
    while binary_file is not None:
        class_obj = binary_file[0]
        with open('momo_file2.dat', 'wb') as outfile:
            outfile.write(class_obj)
        with open('momo_file2.dat', 'rb') as infile:
            money = pickle.load(infile)
            amount = float(input('Enter Amount To Transfer: '))
            send_num = float(input('Enter Number To Send Money: '))
            money.send(amount)
            time.sleep(1)
            print(f'${amount} Sent To {send_num} Successfully')
    else:
        print('Invalid Phone Number Or Pin!!')


def deposit():
    num = input('Enter Phone number: ')
    pin = input('Enter pin: ')
    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute(f'SELECT momo_account FROM users'
              f' WHERE phone_number = "{num}" AND pin = "{pin}"')
    s_object = c.fetchone()
    conn.commit()
    conn.close()
    if s_object is not None:
        money = s_object[0]
        with open('momo_file2.dat', 'wb') as infile:
            infile.write(money)

        with open('momo_file2.dat', 'rb') as outfile:
            class_obj = pickle.load(outfile)
            amount = float(input('Enter Amount To Deposit: '))
            class_obj.deposit(amount)
            time.sleep(1)
            print(f'${amount} Deposited into Account Successfully')
    else:
        print("Invalid Pin Or Phone Number")


def redraw():
    phone_num = input('Enter phone number: ')
    pin = input('Enter pin: ')

    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute(f'SELECT momo_account FROM users'
              f' WHERE phone_number = "{phone_num}" '
              f'AND pin = "{pin}"')
    binary_file = c.fetchone()
    conn.commit()
    conn.close()
    while binary_file is not None:
        class_obj = binary_file[0]
        with open('momo_file2.dat', 'wb') as outfile:
            outfile.write(class_obj)
        with open('momo_file2.dat', 'rb') as infile:
            money = pickle.load(infile)
            amount = float(input("Enter Amount To Redraw: "))
            money.redraw(amount)
            time.sleep(1)
            print(f'${amount} Redrawn from Account Successfully')
    else:
        print('Invalid Phone Number Or Pin!!')


def check_balance():
    print()
    print('Enter Info To Check Balance')
    number = input("Enter phone number: ")
    pin = input('Enter pin: ')
    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute(f'SELECT momo_account FROM users WHERE pin = "{pin}" '
              f'AND phone_number = "{number}"')
    binary_file = c.fetchone()
    conn.commit()
    conn.close()
    if binary_file is not None:
        class_obj = binary_file[0]
        with open('momo_file2.dat', 'wb') as outfile:
            outfile.write(class_obj)
        with open('momo_file2.dat', 'rb') as infile:
            money = pickle.load(infile)
            time.sleep(1)
            print(money.balance())
    else:
        print('Invalid Phone Or Pin')


def change_pin():
    found = False
    row_id = input('Enter Row ID: ')
    pin = input("Enter Old pin: ")
    users = call_db()
    for user in users:
        if user[5] == pin:
            new_pin = input("Enter new pin: ")
            while len(new_pin) != 4:
                new_pin = input("Enter a 4 digit pin: ")
            conn = sqlite3.connect('mobile-money.db')
            c = conn.cursor()
            c.execute(f''' UPDATE users SET pin = "{new_pin}"
                       WHERE rowid = {row_id}
                       ''')
            conn.commit()
            print('Pin Updated Successfully')
            found = True
            break
    if not found:
        print('Invalid Pin Entered')


if __name__ == '__main__':
    main()
