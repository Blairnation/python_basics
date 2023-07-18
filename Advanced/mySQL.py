import mysql.connector
from mysql.connector import Error
import subprocess


# import pyodbc
# connection = pyodbc.connect("DRIVER={SQL Server};SERVER=your_server_name;DATABASE=your_database_name;
# UID=your_username;PWD=your_password")


# Connecting To MySQL Server
def server_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="Localhost",
            user="root",
            passwd="chipsatony2002"
        )
        # print('Connection Successful')
    except Error as err:
        print(f'Error: {err}')
    return conn


# Creating A Database In MySQL Server
def create_database(conn):
    database = 'CREATE DATABASE mydb_python'
    c = conn.cursor()
    try:
        c.execute(database)
        conn.commit()
        conn.close()
        print('Database Created Successfully')

    except Error as err:
        print(f'Error: {err}')


# Connecting To A Database Created In MySQL Server
def database_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="Localhost",
            user="root",
            passwd="chipsatony2002",
            database="mydb_python"
        )
        print('Connection To Database Successful')
    except Error as err:
        print(f'Error: {err}')
    return conn


# Deleting A Database In MySQL Server
def delete_database(conn):
    try:
        c = conn.cursor()
        c.execute('DROP DATABASE clients_db;')
        conn.commit()
        conn.close()
        print("Database Deleted Successfully")
    except Error as err:
        print(f'Error: {err}')


# Showing All Databases In MySQL Server
def show_databases(conn):
    try:
        c = conn.cursor()
        c.execute('SHOW DATABASES;')
        db = c.fetchall()
        for databases in db:
            print(databases[0])
        conn.commit()
        conn.close()
    except Error as err:
        print(f'Error: {err}')


# Not much
def backup_database(conn):
    try:
        command = 'mysqldump --user=root --password=chipsatony2002 > C:\\Users\\BLAIR NATION\\Desktop\\db_backup'
        subprocess.call(command, shell=True)
        print('Database backup successful')
    except Error as err:
        print(f'Error: {err}')


def create_table(conn):
    c = conn.cursor()
    c.execute('CREATE TABLE customers('
              'customerName DATATYPE,'
              'contactName DATATYPE'
              'address DATATYPE); ')
    # Copy Table
    c.execute("CREATE TABLE TestTable AS"
              "SELECT customerName, contactName"
              "FROM customers;")


def delete_table(conn):
    try:
        c = conn.cursor()
        c.execute('DROP TABLE customers')  # TRUNCATE TABLE table_name # deletes data from table not the table itself
        conn.commit()
        conn.close()
        print("Table Deleted Successfully")
    except Error as err:
        print(f'Error: {err}')


def alter_table(conn):
    try:
        c = conn.cursor()
        # ADD COLUMN
        # ALTER TABLE tableName ADD columnName DATATYPE
        c.execute('ALTER TABLE Customers'
                  'ADD Email varchar(255);')

        # DROP COLUMN
        c.execute('ALTER TABLE Customers'
                  'DROP COLUMN Email;')

        # RENAME COLUMN
        c.execute('ALTER TABLE table_name'
                  'RENAME COLUMN old_name to new_name;')

        # CHANGE DATATYPE (maybe DateOfBirth datatype was DateTime)
        c.execute("ALTER TABLE Persons"
                  "MODIFY COLUMN DateOfBirth year;")

    except Error as err:
        print(f'Error: {err}')


def create_procedure(conn):
    c = conn.cursor()
    # CREATE PROCEDURE procedure_name AS BEGIN code END
    c.execute('CREATE PROCEDURE SelectAllCustomers'
              'AS'
              'BEGIN'
              'SELECT * FROM Customers;'
              'END;')

    # Execution
    # CALL  procedure_name

    # with Parameters
    c.execute('DELIMITER //'  # limits the sql query to not consider (;) in the whole query

              'CREATE PROCEDURE SelectAllCustomers(IN cityName VARCHAR(30))'  # Introducing parameter with datatype 
              'BEGIN'
              '   SELECT * FROM Customers WHERE City = cityName;'
              'END //'

              'DELIMITER ;'  # takes it back to its original state to consider (;)
              '')


def main():
    conn = database_connection()
    executions(conn)


def executions(conn):
    c = conn.cursor()

    # SELECT AND DISTINCT SELECT
    # SELECT ALL FROM TABLE
    c.execute('SELECT * FROM customers;')

    # SELECT SELECTED COLUMN NAME(S) IN FROM TABLE
    c.execute('SELECT customer_name, city FROM customers;')

    # SELECT DIFFERENT ITEM NAMES FROM COLUMN NAME(S) FROM TABLE
    c.execute('SELECT DISTINCT customer_name, city, country FROM customers;')

    # COUNT NUMBER OF DISTINCT ITEMS FROM TABLE
    c.execute('SELECT COUNT(DISTINCT country) FROM customers;')

    # WHERE CLAUSE
    # SELECT COLUMN NAME FROM TABLE WHERE CONDITION
    c.execute('SELECT customer_name, city FROM customers WHERE country = "Brazil";')
    # c.execute('SELECT customer_name, city FROM customers WHERE country LIKE "Bra%" AND rowid BETWEEN 1 AND 50;')

    # (AND,OR,NOT OPERATORS) IS USED WITH THE WHERE CLAUSE
    c.execute('SELECT customer_name, city FROM customers WHERE country = "Germany" AND rowid BETWEEN 1 AND 50;')
    c.execute('SELECT * FROM Customers WHERE NOT Country = "Brazil" AND CustomerID = 20 OR City = "Berlin";')

    # ORDER BY(ASC / DESC)
    c.execute('SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;')

    # INSERT INTO TABLE
    # Insert Into TABLE NAME(Column names) VALUES (values for the column names provided)
    c.execute('INSERT INTO customers(customer_name,address,city,country) '
              'VALUES("Blair", "East Legon", "Accra", "Ghana")'
              )
    # Insert Into TABLE NAME  VALUES(All column values in that table)
    c.execute('INSERT INTO customers VALUES (?,?,?,?,?,?,?)')

    # Null
    # Test For Null In Table
    c.execute('SELECT * FROM customers WHERE ContactName IS NULL;')

    # Test For Null In Table
    c.execute('SELECT * FROM customers WHERE ContactName IS NOT NULL;')

    # UPDATE,
    # Update Table Name SET column name = value1, Another Column name = value2 WHERE CONDITION;
    c.execute('UPDATE customers SET customer_name = "Blair" '
              'WHERE city  = "Accra"')
    c.execute('UPDATE customers SET contact_name = "Alfred Smith", city = "Frankfurt"'
              'WHERE customer_name = "Alfreds Futterkiste" '
              'AND city = "Berlin";')

    # DELETE,
    # DELETE FROM TABLE NAME WHERE condition;
    c.execute('DELETE FROM Customers WHERE CustomerName = "Blair Nation"')

    # DELETE FROM TABLE NAME (Deletes all rows without deleting the table)
    c.execute('DELETE FROM CUSTOMERS')

    # LIMIT,
    # Number of rows in limit to select
    c.execute('SELECT * FROM Customers WHERE Country = "Brazil" '
              'ORDER BY CustomerName DESC LIMIT 10;')

    # MAX AND MIN
    # Select MAX(Column Name) From Table Name
    c.execute('SELECT MAX(Price) AS HighestPrice FROM Products')
    c.execute('SELECT MAX(Price) FROM Products '
              'WHERE Price BETWEEN 10 AND 60;')

    # Select MIN(Column Name) From Table Name
    c.execute('SELECT MIN(ProductID)  FROM Products')
    c.execute('SELECT MIN(Price) FROM Products AS SmallestPrice '
              'WHERE Price < 60;')

    # COUNT, AVERAGE and SUM
    # COUNT
    c.execute("SELECT count(*) FROM Customers "
              "WHERE Country = 'Brazil';")
    c.execute('SELECT COUNT(City) FROM Customers '
              'WHERE CustomerID > 60;')

    # AVERAGE
    c.execute('SELECT AVG(Price) FROM Products')
    c.execute('SELECT AVG(Quantity) FROM OrderDetails')

    # SUM
    c.execute('SELECT SUM(Quantity) FROM OrderDetails')
    c.execute('SELECT SUM(Price) FROM Products')

    # LIKE,
    # Starts With(word%), Ends with(%word), between or any position (%word%)
    c.execute("SELECT * FROM Customers "
              "WHERE CustomerName LIKE 'An%'")  # Starts with An
    c.execute("SELECT * FROM Customers "
              "WHERE City LIKE '%F.'")  # Ends with F
    c.execute('SELECT * FROM Customers'
              'WHERE CustomerName NOT LIKE "a%";')  # Does not start with a

    # Wildcard Characters (Used with WHERE and LIKE operator)
    # _ondon - start with character and ends with ondon
    # [bsp]% - starts with b,s or p
    # %[qsr]- ends with q,s or r
    # [a-d]% - starts with a,b,c or d
    # [!bsp]% -  does not starts with b,s or p
    # 2#5 - single number starts from 2 and ends with 5 like 205,235...
    # h?t - single character starts from h and ends with t like hat,hot...
    c.execute('SELECT * FROM Customers'
              'WHERE City LIKE "[bsp]%";')

    # IN STATEMENT (used in place of multiple OR)
    c.execute('SELECT * FROM customers '
              'WHERE Country IN ("Germany", "Brazil", "USA")')
    # selects all customers that are from the same countries as the suppliers
    c.execute('SELECT * Customers '
              'WHERE Country IN (SELECT Country FROM Supplier)')

    # BETWEEN,
    c.execute('SELECT * FROM Products'
              'WHERE Price BETWEEN 10 AND 20')
    c.execute('SELECT * FROM Customers'
              'WHERE ContactName BETWEEN "Alfred Smith" AND "Hanna Moos"'
              'ORDER BY ContactName;')
    # BETWEEN DATES
    c.execute('SELECT * FROM Orders'
              'WHERE OrderDate BETWEEN "1996-07-01" '
              'AND "1996-07-31"')

    # ALIASES(AS)
    c.execute('SELECT CustomerName AS Customer, ContactName AS [Contact Person]'
              'FROM Customers;')
    # add more columns as one name using CONCAT
    c.execute('SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address'
                                                                                'FROM Customers;')

    # Querying between tables in database
    # TableName.ColumnName
    c.execute('SELECT c.CustomerName, s.SupplierName, c.City '
              'FROM Customers As c , Suppliers as s '
              'WHERE c.City = s.City AND SupplierName = "Refrescos Americanas LTDA";')
    # Can use straight instead of aliases
    c.execute('SELECT Customers.CustomerName, Suppliers.SupplierName, Customers.City '
              'FROM Customers, Suppliers'
              'WHERE Customers.City = Suppliers.City ;')

    # INNER JOIN
    # Select Column names(Between Different Tables) From Main Table INNER JOIN Sub Table ON Condition
    # Returns all matching rows from the two tables
    c.execute('SELECT  Orders.OrderID, Customers.CustomerName, Orders.OrderDate'
              'FROM Orders'
              'INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;')
    # Adding rows from two or more tables Using Inner Join
    c.execute('SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName '
              'FROM ((Orders '
              'INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)'
              'INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);')

    # LEFT JOIN (LEFT OUTER JOIN)
    # (Return all rows from left table(Whether there is a match or not with right table)
    # AND its matching rows from right table )
    c.execute('SELECT Customers.CustomerName, Orders.OrderID'
              'FROM Customers'
              'LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID')

    # RIGHT JOIN (RIGHT OUTER JOIN)
    # (Return all rows from right table(Employees)(Whether there is a match or not with left table)
    # AND its matching rows from left table (Orders), returns null if no match from right table)
    c.execute('SELECT Orders.OrderID, Employees.LastName, Employees.FirstName'
              'FROM Orders'
              'RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID'
              'ORDER BY Orders.OrderID;')

    # FULL JOIN (FULL OUTER JOIN)
    # Returns all rows from the all tables whether there is a match or not
    # Matches each other when there is a match and produces Null when no much on both tables
    c.execute('SELECT Customers.CustomerName, Orders.OrderID'
              'FROM Customers'
              'FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID'
              'ORDER BY Customers.CustomerName;')

    # SELF JOIN (Table Joined with itself)
    # One table separated into two or more parts using aliases with conditions
    c.execute('SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City'
              'FROM Customers A, Customers B'
              'WHERE A.CustomerID <> B.CustomerID'
              'AND A.City = B.City'
              'ORDER BY A.City;')

    # UNION
    # Used to combine two SELECT statements with same formula
    # into one column  (With no distinct/different values)
    c.execute('SELECT City FROM Customers'
              'UNION'
              'SELECT City FROM Suppliers'
              'ORDER BY City;')
    # UNION ALL (Bring out all values from the select statement)
    c.execute('SELECT City FROM Customers'
              'UNION ALL'
              'SELECT City FROM Suppliers'
              'ORDER BY City;')
    # Adding string and more table columns of same name and type
    c.execute("SELECT 'Customer' AS Type, ContactName, City, Country"  # AS Type creates an alias used as a column name 
              "FROM Customers"  # that contains the strings(Customer and Supplier)
              "UNION"
              "SELECT 'Supplier', ContactName, City, Country"
              "FROM Suppliers;")

    # Suggestion
    c.execute('SELECT Country, SUM(CustomerCount) AS TotalCustomerCount, SUM(SupplierCount) AS TotalSupplierCount'
              'FROM ('
              'SELECT c.Country, COUNT(c.CustomerID) AS CustomerCount, 0 AS SupplierCount'
              'FROM Customers c'
              'GROUP BY c.Country'
              'UNION ALL'
              'SELECT s.Country, 0 AS CustomerCount, COUNT(s.SupplierID) AS SupplierCount'
              'FROM Suppliers s'
              'GROUP BY s.Country) AS CombinedCounts'
              'GROUP BY Country;')

    # GROUP BY
    # Groups by rows with same values and always used with count, max, min, avg, sum
    c.execute('SELECT COUNT(CustomerID), Country'
              'FROM Customers'
              'GROUP BY Country;')  # count the number of customers using customerID
    # that are from the same country (GROUP BY COUNTRY)

    c.execute("SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders"
              "LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID"
              "GROUP BY ShipperName;")

    # HAVING
    # Used in place of WHERE, where there are aggregate functions like COUNT,MAX,...
    c.execute('SELECT COUNT(CustomerID), Country'
              'FROM Customers'
              'GROUP BY Country'
              'HAVING COUNT(CustomerID) > 5;')

    c.execute('SELECT e.LastName, Count(o.OrderID) as [No Of Orders]'
              'FROM Employees e'
              'RIGHT JOIN Orders o ON e.EmployeeID = o.EmployeeID'
              'GROUP BY FirstName'
              'HAVING COUNT(o.OrderID) > 10'
              'ORDER BY COUNT(o.OrderID) DESC;')

    # Using where together with having
    c.execute('SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders'
              'FROM Orders'
              'INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID'
              'WHERE LastName = "Davolio" OR LastName = "Fuller"'
              'GROUP BY LastName'
              'HAVING COUNT(Orders.OrderID) > 25;')

    # EXIST
    # Return True and brings query records if condition is True or row Exists
    c.execute('SELECT SupplierName'
              'FROM Suppliers'
              'WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID '
              'AND Price < 20);')

    # ANY (USES COMPARISON OPERATORS)
    # Compares a value with set of values if at least one of the values return True
    c.execute('SELECT ProductName'
              'FROM Products'
              'WHERE Price > ANY (SELECT Price FROM Products WHERE CategoryID = 1);')
    # Returns productName where its price is greater than at least one price
    # with categoryID equal one

    # ALL
    # Compares a value with set of values if all the values return True
    c.execute('SELECT ProductName'
              'FROM Products'
              'WHERE Price > ALL (SELECT Price FROM Products WHERE CategoryID = 1);')
    # Returns productName where its price is greater than all price
    # with categoryID equal one

    c.execute('SELECT CustomerName'
              'FROM Customers'
              'WHERE Country = ALL (SELECT Country FROM Customers WHERE City = "London");')
    # Returns all customerNames where their country's city is London
    # If it is ANY, It returns all customerNames from the same COUNTRY as those
    # located in London

    # SELECT INTO
    # creates a new table for backup(with IN if into another database)
    # Select Column name(s) into new table from old table where condition
    c.execute('SELECT * INTO CustomersBackup2017'
              'FROM Customers;')

    # Create table in Backup.mdb
    c.execute("SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'"
              "FROM Customers;")

    # Selecting specific columns to create into new database and can add where
    # clause for specific options also
    c.execute("SELECT CustomerName, ContactName INTO CustomersBackup2017"
              "FROM Customers"
              "WHERE Country = 'Germany';")

    # Creating table with same datatypes and arrangement without copying its contents
    c.execute('SELECT * INTO new table'
              'FROM old table'
              'WHERE 1 = 0;')

    # INSERT INTO SELECT
    # Requires the datatype in both tables match and append the rows from the
    # source table to target table (produces null in unselected columns)
    c.execute('INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)'
              'SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROM Suppliers;')
    # Insert all items from one table to another with same datatypes and arrangement
    c.execute('INSERT INTO table2'
              'SELECT * FROM table1'
              'WHERE condition;')

    # CASE
    # Returns a value once a condition is met
    # Starts with CASE and ends with END
    c.execute("SELECT OrderID, Quantity,"
              "CASE"
              "WHEN Quantity > 30 THEN 'The quantity is greater than 30'"
              "WHEN Quantity = 30 THEN 'The quantity is 30'"
              "ELSE 'The quantity is under 30'"
              "END AS QuantityText"
              "FROM OrderDetails;")

    # Order by City, if city is empty, Order by Country
    c.execute('SELECT CustomerName, City, Country'
              'FROM Customers'
              'ORDER BY'
              '(CASE'
              'WHEN City IS NULL THEN Country'
              'ELSE City'
              'END);')

    # IFNULL AND COALESCE
    # It enables you to select own value if selected column is NULL
    c.execute('SELECT ProductName, UnitPrice * (UnitsInStock + IFNULL(UnitsOnOrder, 0))'
              'FROM Products;')
    c.execute('SELECT ProductName, UnitPrice * (UnitsInStock + COALESCE(UnitsOnOrder, 0))'
              'FROM Products;')


def constraint(conn):
    c = conn.cursor()

    # CONSTRAINT
    # Gives restrictions to columns when creating them
    # NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT

    # NOT NULL
    # Should not accept empty columns
    c.execute('CREATE TABLE table_name('
              'column_name DATATYPE NOT NULL );')
    # ADD NOT NULL
    # ALTER TABLE table_name MODIFY COLUMN column_name DATATYPE NOT NULL;
    # REMOVE NOT NULL
    # ALTER TABLE table_name MODIFY COLUMN column_name DATATYPE NULL;

    # UNIQUE
    # Enables columns to have different values throughout
    c.execute('CREATE TABLE table_name('
              'CustomerID DATATYPE, '
              'last_Name DATATYPE NOT NULL,'
              'UNIQUE(CustomerID) );'
              )  # For one column

    c.execute('CREATE TABLE table_name('
              'CustomerID DATATYPE, '
              'last_Name DATATYPE NOT NULL,'
              'first_name DATATYPE,'
              'CONSTRAINT constraint_name UNIQUE(CustomerID, last_Name) );'
              )  # Adding unique to two or more columns

    # ADD (Adding Unique to already created table column)
    # ALTER TABLE table_name ADD UNIQUE(column_name);  # for one column
    # ALTER TABLE table_name ADD CONSTRAINT constraint_name UNIQUE(column_names); # Two or more columns

    # REMOVE
    # ALTER TABLE table_name DROP INDEX column_name; # For one column
    # ALTER TABLE table_name DROP INDEX constraint_name; # For two or more columns

    # PRIMARY KEY
    # Restrict columns to have UNIQUE and NOT NULL values
    c.execute('CREATE TABLE table_name ('
              'CustomerID DATATYPE NOT NULL,'
              'last_name DATATYPE, '
              'first_name DATATYPE, '
              'PRIMARY KEY(CustomerID) );'
              )  # For one column

    c.execute('CREATE TABLE table_name ('
              'CustomerID DATATYPE NOT NULL,'
              'last_name DATATYPE, '
              'first_name DATATYPE, '
              'CONSTRAINT constraint_name PRIMARY KEY(CustomerID, last_name) );'
              )  # For two or more columns

    # ADD PRIMARY KEY
    # ALTER TABLE table_name ADD PRIMARY KEY(column_name);
    # ALTER TABLE table_name ADD CONSTRAINT PK_Person PRIMARY KEY(column_names); # For two or more columns

    # REMOVE PRIMARY KEY
    # ALTER TABLE table_name DROP PRIMARY KEY;
    # ALTER TABLE table_name DROP PRIMARY KEY constraint_name;

    # FOREIGN KEY
    # Create link between different table columns without affecting tables
    # It references to PRIMARY KEY of another table column
    c.execute('CREATE TABLE Orders ('
              'orderID DATATYPE NOT NULL,'
              'CustomerID DATATYPE, '
              'last_name DATATYPE NOT NULL,'
              'first_name DATATYPE, '
              'age DATATYPE, '
              'PRIMARY KEY(orderID),'
              'FOREIGN KEY(CustomerID) REFERENCES reference_table(reference_column) )'
              )

    c.execute('CREATE TABLE Orders ('
              'orderID DATATYPE NOT NULL,'
              'CustomerID DATATYPE,'
              'last_name DATATYPE NOT NULL,'
              'first_name DATATYPE, '
              'age DATATYPE, '
              'PRIMARY KEY(orderID),'
              'CONSTRAINT FK_CustomerOrder FOREIGN KEY(CustomerID) '
              'REFERENCES Customers(CustomerID) );'
              )  # Adding constraint_name
    # ADD FOREIGN KEY
    # ALTER TABLE table_name ADD FOREIGN KEY(column_name)
    # REFERENCES reference_table(reference_column);
    # like
    # ALTER TABLE Orders ADD FOREIGN KEY(CustomerID)
    # REFERENCES Customers(CustomerID);

    # DROP FOREIGN KEY
    # ALTER TABLE table_name DROP FOREIGN KEY;
    # ALTER TABLE table_name DROP FOREIGN KEY constraint_name;

    # CHECK
    # Allows column to check certain conditions before accepting values
    c.execute("CREATE TABLE table_name("
              "CustomerID DATATYPE NOT NULL, "
              "last_name DATATYPE,"
              "age DATATYPE,"
              "PRIMARY KEY(CustomerID),"
              "CHECK(age >= 18) );"
              )  # For one column

    c.execute("CREATE TABLE table_name("
              "CustomerID DATATYPE NOT NULL, "
              "last_name DATATYPE,"
              "age DATATYPE,"
              "Country DATATYPE"
              "PRIMARY KEY(CustomerID),"
              "CONSTRAINT CHK_CustomerAge CHECK(age >= 18 AND Country = 'Ghana') );"
              )  # For two or more columns

    # ADD
    # ALTER TABLE table_name ADD CHECK(column_name condition)
    # like CHECK(age >= 18) # For one column
    # ALTER TABLE table_name ADD CONSTRAINT constraint_name
    # CHECK(column1 condition AND column2 condition) # For two or more columns

    # DROP
    # ALTER TABLE table_name DROP CHECK(column_name)
    # ALTER TABLE table_name DROP CHECK constraint_name

    # DEFAULT
    # Set default value for a column if no value is inserted
    c.execute('CREATE TABLE table_name('
              'ID DATATYPE NOT NULL,'
              'last_name DATATYPE,'
              'age DATATYPE,'
              'country DATATYPE DEFAULT "Ghana",'
              'date DATATYPE DEFAULT CURRENT_TIMESTAMP() );'
              # set date default to current date using CURRENT_DATESTAMP
              )

    # ADD DEFAULT
    # ALTER TABLE table_name ALTER column_name SET DEFAULT 'default_name';

    # DROP DEFAULT
    # ALTER TABLE table_name ALTER column_name DROP DEFAULT;

    # INDEX
    # Given to columns to enable removal of data from database faster without having to
    # search an entire table but search right through the indexed columns
    # CREATE INDEX
    c.execute('CREATE INDEX index_name '  # or CREATE UNIQUE INDEX for unique indexes  
              'on table_name(columns to place index); ')
    # Like
    c.execute('CREATE INDEX idx_country '
              'on Customers(Country); ')

    # Searching table using index
    c.execute('SELECT * FROM Customers '
              'WHERE Country = "Ghana";')  # (AND ID = 1) if ID column is also indexed
    # Country is the indexed column created to search the Customers table
    # without having to search the entire table

    # DROP INDEX
    # ALTER TABLE table_name DROP INDEX index_name;

    # AUTO INCREMENT (starts from 1 default)
    # Allows unique values to be generated automatically everytime a new
    # record is inserted, and also it is not selected and given a value on a query
    # since it will be  generated automatically
    c.execute('CREATE TABLE table_name('
              'ID DATATYPE NOT NULL AUTO_INCREMENT,'
              'last_name DATATYPE NOT NULL,'
              'age DATATYPE,'
              'PRIMARY KEY(ID) );')

    # SETTING the starting AUTO INCREMENT of choice
    c.execute(' ALTER TABLE table_name AUTO_INCREMENT = 100')  # starting from 100

    # VIEW
    # It is created virtually  to view specific information from one or more tables for fast querying
    # Create view
    c.execute('CREATE VIEW [view_name] as'
              'SELECT columns FROM table_name'
              'WHERE condition')
    # like
    c.execute('CREATE VIEW [Brazil Customers] AS'
              'SELECT CustomerName, ContactName, City'
              'FROM Customers'
              'WHERE Country = "Brazil"; ')

    c.execute("CREATE VIEW [Products Above Average Price] AS"
              "SELECT ProductName, Price"
              "FROM Products"
              "WHERE Price > (SELECT AVG(Price) FROM Products);")

    # Query View
    c.execute('SELECT * FROM [Brazil Customers];')
    c.execute('SELECT * FROM [Products Above Average Price];')

    # UPDATE VIEW
    c.execute('CREATE OR REPLACE VIEW view_name AS'
              'SELECT column1, column2, ...'
              'FROM table_name'
              'WHERE condition;')

    # DROP VIEW
    c.execute('DROP VIEW view_name')
    c.execute('DROP VIEW [Brazil Customers];')

    # SQL INJECTIONS
    # SQL injection is a type of security vulnerability that occurs when an attacker can manipulate
    # or inject malicious SQL code into an application's database query

    # Taking input USERNAME and PASSWORD in web apps to query a database
    c.execute('SELECT * FROM Users WHERE username = "<username>"'
              "AND password = '<password>")
    # If not validated user can enter malicious code to fetch all item in the database

    # Attackers Code 1
    c.execute("SELECT * FROM Users WHERE username = '' OR '1'='1' --' AND password = ''")
    # users input ('' OR '1'='1' --' AND password = '')
    # condition |'' OR '1'='1'| is always True and |--' AND password = ''| will turn rest of code into a comment

    # code 2
    c.execute("SELECT * FROM Users WHERE UserId = 105 OR 1=1;")
    # Userinput ( 105 OR 1=1 ) # Returns all rows from Users table

    # code 3 like code 1
    c.execute('SELECT * FROM Users WHERE Name ="" or ""="" AND Pass ="" or ""=""')
    # UserInput ("" OR ""="")

    # To prevent this, Use placeholders in query like
    c.execute('"INSERT INTO Customers VALUES (?, ?)",name,password')


main()
