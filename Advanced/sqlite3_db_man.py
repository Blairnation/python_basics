import sqlite3

# DATATYPES:NULL, INTEGER, REAL, TEXT AND BLOB

# CREATE DATABASE AND TABLE

# conn = sqlite3.connect(':memory:') #connection to database temporary(delete after quiting)

# connect to database
conn = sqlite3.connect('customers.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute('''CREATE TABLE customers
             (first_name text,
             last_name text,
             email text
             )''')  # or CREATE TABLE IF NOT EXIST customers

# commit our command
conn.commit()

# close our connection
conn.close()

# INSERT A RECORD AT A TIME TO DATABASE

conn = sqlite3.connect('customers.db')

c = conn.cursor()

# Insert record
c.execute('''INSERT INTO customers VALUES("Bhim",
                                 "Nation",
                                 "bhimnation@gmail.com"
                                 )
''')

conn.commit()

conn.close()

# adding rowid and specifying each insertion
conn = sqlite3.connect('customers.db')
c = conn.cursor()

c.execute('''INSERT OR REPLACE INTO customers(rowid,first_name,last_name,email)
            VALUES(3,
            "Kylian",
            "Lottin", 
            "kylianmbappe@gmail.com"
            )
''')

conn.commit()

conn.close()

# INSERT MANY RECORDS INTO DATABASE

conn = sqlite3.connect('customers.db')

c = conn.cursor()

many_customers = [
    ('Lionel', 'Messi', 'lionelmessi@gmail.com'),
    ('Cristiano', 'Ronaldo', 'cristianoronaldo@gmail.com'),
    ('Stone', 'Bwoy', 'stonebwoy@gmail.com')
]

c.executemany('''INSERT INTO customers VALUES(?,?,?)
''', many_customers)

conn.commit()

conn.close()

# SUGGESTION

conn = sqlite3.connect('customers.db')

c = conn.cursor()

customers_list = []
while True:
    first_name = input('Enter  first name: ')
    second_name = input('Enter second name: ')
    email = input("Enter email: ")
    many_customers = (first_name, second_name, email)
    customers_list.append(many_customers)

    again = input('Do you want to insert into database again(y/n): ')
    if again != 'y'.lower():
        print("Database Updated...")
        break

c.executemany('''INSERT INTO customers VALUES(?,?,?)
''', customers_list)

conn.commit()

conn.close()

print("customers database updated successfully")

# QUERY AND FETCHING DATABASE

conn = sqlite3.connect('customers.db')

c = conn.cursor()

# query the database
c.execute('''SELECT * FROM customers''')

# fetch the database
# c.fetchone()  # fetch first item in table
# c.fetchmany(3)  # fetch first order items according to numbers(size) provided
# c.fetchall() # fetch everything from database
database = c.fetchall()  # or print(c.fetchall())
print(database)

conn.commit()

conn.close()

# QUERYING SINGLE OBJECT FROM TABLE

conn = sqlite3.connect('customers.db')

c = conn.cursor()

# query the database
c.execute('''SELECT * FROM customers''')

# fetch the database and bring out individual elements using their indexes

# one_item = c.fetchone()  # [1] can add to this
# print(one_item[1])  # First item index 1

# one_item = c.fetchone() # using while loop to fetch all item row by row
# while one_item is not None:
#    print(one_item)
#    one_item = c.fetchone()

# items = c.fetchmany(3)
# for item in items:
#    print(item[2]) # First three items index 2

database = c.fetchall()
for users in database:
    print(users[0])  # all items in database index 1

conn.commit()

conn.close()

# SUGGESTION 2
conn = sqlite3.connect('customers.db')

c = conn.cursor()

c.execute('''SELECT * FROM customers''')

database = c.fetchall()
count = 0
for users in database:
    count += 1
    print(f'User #{count}')
    print(f'Full name: {users[0] + " " + users[1]}')  # all items in database index 0 and 1
    print(f'Email: {users[2]}')
    print()

# or
name = input('Enter first name: ').capitalize()
database = c.fetchall()
found = False
for users in database:
    if users[0] == name or users[1] == name:
        print('Your Information')
        print(f'Name: {users[0] + " " + users[1]}')
        print(f'Email: {users[2]}')
        found = True
if not found:
    print('Name unavailable')

conn.commit()

conn.close()

# Querying using the execution (WHERE)

c.execute('''SELECT rowid, * FROM customers WHERE last_name = "Blair"''')  # can add ID of row using rowid

# using (LIKE) to bring all lookalike items
c.execute('''SELECT * FROM customers WHERE first_name LIKE "Cr%"''')  # for starting with
# c.execute('''SELECT * FROM customers WHERE email LIKE "%@gmail.com"''')  # for ending with
database = c.fetchall()
for users in database:
    print(users)


# UPDATE DATABASE

# using other column names
conn = sqlite3.connect('customers.db')

c = conn.cursor()

c.execute('''UPDATE customers SET first_name = "Junior"
                              WHERE last_name = "Ronaldo"

''')

conn.commit()

print('Database Updated successfully')
conn.close()

# using row id
conn = sqlite3.connect('customers.db')

c = conn.cursor()

c.execute('''UPDATE customers SET first_name = "Emmanuel"
                              WHERE rowid = 8

 ''')

conn.commit()

print('Database Updated successfully')
conn.close()


# DELETE ROWS FROM DATABASE
conn = sqlite3.connect('customers.db')

c = conn.cursor()

c.execute('''DELETE FROM customers  WHERE rowid = 7''')  # Can use other column names

conn.commit()

conn.close()


# SORTING DATABASE
conn = sqlite3.connect('customers.db')
c = conn.cursor()

c.execute('''SELECT rowid, * FROM customers ORDER BY rowid ASC''')  # or DESC and any column name

conn.commit()

conn.close()

# AND/OR STATEMENT
# and
conn = sqlite3.connect('customers.db')
c = conn.cursor()

# using two column name lookalike(start% and %end)
c.execute('''SELECT rowid, * FROM customers
             WHERE first_name LIKE "K%"
             AND last_name LIKE "L%"''')
# using rowid and any column name
# c.execute('''SELECT rowid, * FROM customers
#             WHERE first_name LIKE "K%"
#             AND rowid = 2''')

db = c.fetchall()
for user in db:
    print(user)

conn.commit()

conn.close()

# or
conn = sqlite3.connect('customers.db')
c = conn.cursor()

# Can use any other name or rowid
c.execute('''SELECT rowid, * FROM customers
             WHERE first_name LIKE "K%"
             OR rowid = 5''')
db = c.fetchall()
for user in db:
    print(user)

conn.commit()

conn.close()


# ADDING LIMIT

conn = sqlite3.connect('customers.db')
c = conn.cursor()

c.execute('''SELECT rowid, * FROM customers LIMIT 3''')
db = c.fetchall()
for user in db:
    print(user)

conn.commit()

conn.close()

# DELETE TABLE

conn = sqlite3.connect('customers.db')
c = conn.cursor()

c.execute('''DROP TABLE customers''')

conn.commit()

conn.close()
