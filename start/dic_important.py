# Explaination

db = [{"name": "emma", "age": 25, "password": "the"}, {"name": "emma", "age": 25, "password": "the"}]
for item in db:
    print(item["name"])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

for key in thisdict:
    print(key, thisdict["brand"])

print(thisdict)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.get("year"))

print(thisdict.items())



# ecommerce simplified

db = [{"name": "emma", "password": "the"}]
products = [
    {"name": "milo", "price": 3},
    {"name": "milk", "price": 15},
    {"name": "bread", "price": 50}
]
cart_items = []


def welcome():
    print("WELCOME TO ECOMMERCE")
    print("Enter 1 to register and enter 2 to login")
    log_reg = input("Enter 1 or 2: ")
    if log_reg == "1":
        register()
    elif log_reg == "2":
        login()
    else:
        print("Invalid Input")


def register():
    print("THIS IS THE REGISTRY SECTION")
    name = input("Name: ")
    password = input("Password: ")
    credentials = {"name": name, "password": password}
    db.append(credentials)
    login()


def login():
    print("THIS IS THE LOGIN SECTION")
    name = input("Name: ")
    password = input("Password: ")
    if any(user["name"] == name and user["password"] == password for user in db):
        print("Login successful")
        item()
    else:
        print("Login failed")


def item():
    print("These are the items and their prices available.")
    for item in products:
        print(f"{item['name']} (${item['price']})")
    total_amount()


def total_amount():
    amount = 0
    while True:
        item_bought = input("Enter Item (or 'done' to finish): ")
        if item_bought == "done":
            break
        for product in products:
            if product["name"] == item_bought:
                cart_items.append(product["name"])
                amount += product["price"]
                print(f"Added {product['name']} to cart. Continue shopping.")
                break
    print(f"The items you bought are: {', '.join(cart_items)}")
    print(f"The total amount you will pay is ${amount}")


welcome()

# mine

import datetime

db = [{"name": "emma", "age": 23, "password": "one"}, {"name": "tony", "age": 27, "password": "then"}]
products = [{"name": "milo", "price": 13}, {"name": "milk", "price": 15}, {"name": "bread", "price": 50}]

cart = []


def welcome():
    print("WELCOME TO ECOMMERCE")
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 12:
        print("Good Morning Customer")
    elif 12 <= hour < 18:
        print("Good Afternoon Customer")
    else:
        print("Good Evening Customer")

    print("Press 1 to register and 2 to login ")
    log_reg = input("Enter number:")
    if log_reg == "1":
        register()
    elif log_reg == "2":
        login()
    else:
        print("Invalid Input")


def register():
    print("WELCOME TO REGISTRY SECTION")
    print("Fill in your credentials")
    name = input("Username: ")
    age = int(input("Age: "))
    password = input("Password: ")
    db.append({"name": name, "age": age, "password": password})
    login()


def login():
    print("WELCOME TO LOGIN SECTION")
    print("Fill in to login")
    name = input("Username: ")
    password = input("Password: ")
    for users in db:
        if users["name"] == name and users["password"] == password:
            print("Login Successful")
            items()
            return
    else:
        print("Password or Username Incorrect!!")
        print("Login Failed")


def items():
    print("These are the items available and their prices")
    for item in products:
        print(f"{item['name']} ${item['price']}")
    buy_product()


def buy_product():
    amount = 0
    print("Enter the item name to add to cart OR enter done to stop shopping")
    while True:
        item = input("Enter item name: ")
        if item == "done":
            break
        for product in products:
            if product["name"] == item:
                cart.append(product["name"])
                amount += product["price"]
                print("Item added. Continue Shopping!!")
                break
        else:
            print("Item Selected Unavailable")
    print(f"The items in your cart are{cart}")
    print(f"The total amount you will pay is ${amount}")


welcome()