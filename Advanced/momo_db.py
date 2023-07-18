import sqlite3
from momo_class import MobileMoney
import pickle
import datetime
import time


def create_table():
    connection = sqlite3.connect('mobile-money.db')
    c = connection.cursor()

    c.execute('''CREATE TABLE users
                (first_name text,
                 last_name text,
                 id_num text,
                 address text,
                 phone_number text,
                 pin text,
                 momo_account blob
                   )''')

    connection.commit()
    c.close()


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


def call_db():
    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    base = c.fetchall()
    return base


def register():
    class_obj = MobileMoney()
    outfile = open('momo_file.dat', 'wb')
    pickle.dump(class_obj, outfile)
    outfile.close()
    infile = open('momo_file.dat', 'rb')
    serialised_obj = infile.read()
    infile.close()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    id_num = input('Enter ID card number: ')
    address = input("Enter Address: ")
    phone_num = input("Enter phone number: ")
    while True:
        pin = input("Enter 4 Digit Pin: ")
        while not validate_pin(pin):
            print('Pin must be 4 digits')
            pin = input("Enter a Valid Pin: ")
        re_pin = input('Re-enter Pin: ')
        if re_pin != pin:
            print('Pin Does Not match!!')
            continue

        items = (first_name, last_name, id_num, address, phone_num, pin, sqlite3.Binary(serialised_obj))

        conn = sqlite3.connect('mobile-money.db')
        c = conn.cursor()

        c.execute('INSERT INTO users VALUES(?,?,?,?,?,?,?)', items)
        conn.commit()
        conn.close()
        print('Registering....')
        time.sleep(3)
        print("Registered Successfully")
        return


def greeting():
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 12:
        print('Good Morning Customer,')
    elif 12 <= hour < 18:
        print("Good Afternoon Customer,")
    else:
        print('Good Evening Customer,')

    print('WELCOME TO MTN MOBILE MONEY SERVICES')
    print("__________________________")


def look_up():
    print('Enter Info To Lookup Details')
    found = False
    phone_num = input('Enter phone number: ')
    pin = input('Enter pin: ')
    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()

    c.execute(f'''SELECT * FROM users''')
    details = c.fetchall()
    for info in details:
        if info[4] == phone_num and info[5] == pin:
            time.sleep(2)
            print('Searching Details...')
            print()
            print('Details')
            print(f'First Name: {info[0]}\n'
                  f'Last Name: {info[1]}\n'
                  f'Index Number: {info[2]}\n'
                  f'Address: {info[3]}\n'
                  f'Phone Number: {info[4]}')
            found = True
    conn.commit()
    conn.close()
    if not found:
        print('Details Not Found!!!')


def update():
    print("Enter Info To Update Details")
    found = False
    pin = input('Enter pin: ')
    phone_num = input("Enter Phone Number: ")

    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute(f'''SELECT * FROM users''')

    details = c.fetchall()
    for users in details:
        if users[5] == pin and users[4] == phone_num:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            id_num = input('Enter ID card number: ')
            address = input("Enter Address: ")

            c.execute(f'''UPDATE users SET
             first_name = "{first_name}",
             last_name = "{last_name}",
             id_num = "{id_num}",
             address = "{address}" 
             WHERE pin = "{pin}" AND
             phone_number = "{phone_num}"                    
                                 ''')
            conn.commit()
            print("Details Updating...")
            time.sleep(4)
            conn.close()
            print("Details Updated Successfully")
            found = True

    if not found:
        print("Invalid Phone Or Pin Number")


def delete():
    print("Enter Info To Delete MOMO Account")
    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()

    pin = input("Enter pin: ")
    row_id = input("Enter Row ID: ")

    c.execute(f'''DELETE FROM users WHERE rowid = "{row_id}" AND pin = "{pin}" ''')

    conn.commit()
    print('MOMO Account Successfully Deleted')
    conn.close()


def check_database():
    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute('SELECT rowid, * FROM users')
    users = c.fetchall()
    for user in users:
        print(user)
    conn.commit()
    conn.close()


def retrieve_momo():
    pin = input('Enter pin: ')
    phone_num = input("Enter phone number: ")
    conn = sqlite3.connect('mobile-money.db')
    c = conn.cursor()
    c.execute(f'SELECT momo_account FROM users WHERE phone_number = "{phone_num}" AND pin = "{pin}"')
    binary_file = c.fetchone()

    conn.commit()
    conn.close()
    if binary_file is not None:
        class_obj = binary_file[0]
        with open('momo_file2.dat', 'wb') as file:
            file.write(class_obj)

        with open('momo_file2.dat', 'rb') as infile:
            obj = pickle.load(infile)
            print(obj)

    else:
        print('Invalid Phone Number Or Pin!!')


def main():
    check_database()


if __name__ == '__main__':
    main()
