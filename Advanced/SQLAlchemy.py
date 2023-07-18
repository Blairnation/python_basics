from sqlalchemy import create_engine, Column, Integer, String, DefaultClause
from sqlalchemy.schema import UniqueConstraint, CheckConstraint, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Mapped

# returns base class for declarative class definitions
# used as superclass for models
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customer'

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    first_name = Column("FirstName", String(255), nullable=False)
    last_name = Column("LastName", String(255))
    address = Column('Address', String(255))
    age = Column('Age', Integer, CheckConstraint('age >= 10'))
    city = Column('City', String(255))  # default=DefaultClause('"Accra'))

    def __init__(self, id, first_name, last_name, address, age, city):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.city = city

    def __repr__(self):
        return f'First Name: {self.first_name}\n' \
               f'Last Name: {self.last_name}\n' \
               f'Address:{self.address}\n' \
               f'Age: {self.age}\n' \
               f'City: {self.city}'


class Items(Base):
    __tablename__ = 'Items'

    description = Column('Description', String(255))
    telephone = Column('Order ID', String, primary_key=True)
    customer_id = Column("Customer ID", Integer, ForeignKey('Customer.id'))
    price = Column('Price', Integer, nullable=False)

    # __table_args__ = (
    #   PrimaryKeyConstraint('description', 'order_id'),
    #  UniqueConstraint('order_id',
    #                  'description'))

    def __int__(self, descript, customer_id, price, order_id):
        self.description = descript
        self.customer_id = customer_id
        self.price = price
        self.order_id = order_id

    def __repr__(self):
        return f'Description: {self.description}\n' \
               f'Price: ${self.price}'


# engine = create_engine('mysql+mysqlconnector://root:chipsatony2002@Localhost:3306/clients_db')
engine = create_engine('sqlite:///mydb.db', echo=False)

# FIRST CLASS(Customer)
# Method to create database table based on defined model(declarative_base)
# Base.metadata.create_all(bind=engine)

# connect with database for CRUD operations
Session = sessionmaker(bind=engine)
session = Session()

# ADD TO DATABASE
# create instance of class and inserting
# customer = Customer(1, 'Tony', 'Blair', 'c100', 30, 'Accra')
# session.add(customer)

# customer1 = Customer(2, 'Lionel', 'Messi', 'c200', 36, 'Maimi')
# customer2 = Customer(3, 'Kylian', 'Mbappe', 'c300', 24, 'Paris')
# customer3 = Customer(4, 'Cristiano', 'Ronaldo', 'c400', 38, 'Abu Dhabi')

# session.add(customer1)
# session.add(customer2)
# session.add(customer3)
# commit the changes
# session.commit()


# QUERYING DATABASE

# Query all Items
# results = session.query(Customer).all()
# for result in results:
#    print(result)

# Query specified columns
# One column
# cities = session.query(Customer.city)
# for city in cities:
#  print(city[0])

# Two Or More
# results = session.query(Customer.last_name, Customer.first_name)
# for last_names, first_name in results:
#    print(f'{first_name} {last_names}')

# Querying with Filter
# results = session.query(Customer).filter(Customer.first_name == 'Kylian')
# results = session.query(Customer).filter(Customer.first_name == 'Cristiano').first() # without iterating
# results = session.query(Customer).filter(Customer.city == 'Abu Dhabi' and Customer.first_name == 'Cristiano')
# results = session.query(Customer).filter(Customer.city.in_(['Paris', 'Accra']))
# results = session.query(Customer).filter(Customer.city.like('Pa%'))
# results = session.query(Customer).order_by(Customer.first_name)
# results = session.query(Customer).count()
# results = session.query(Customer).filter(or_(Customer.age == 38, Customer.id == 4))
# session.delete()
# print(results)


# session.close()


# TRY CODE
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import mysql.connector
import time
import datetime

engine = create_engine('mysql+mysqlconnector://root:chipsatony2002@Localhost:3306/mydb')
# engine = create_engine('sqlite:///mydb.db')
Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'

    product_id = Column("Product ID", Integer, primary_key=True, autoincrement=True)
    product_name = Column("Product Name", String(255), unique=True)
    price = Column('Price', Float, nullable=False)
    brand = Column('Brand', String(255))

    def __init__(self, product_name, price, brand):
        self.product_name = product_name
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f'Product: {self.product_name}\n' \
               f'Price: ${self.price}'


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
