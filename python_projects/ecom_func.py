db = [{"name": "emma", "age": 25, "password": "the"}]
products = [
    {
        "name": "milo",
        "price": 3
    },
    {
        "name": "milk",
        "price": 15
    },
    {
        "name": "bread",
        "price": 50
    }]
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
    print("Fill in the following credentials")
    name = input("Name: ")
    age = int(input("Age: "))
    password = input("Password: ")
    credentials = {"name": name, "age": age, "password": password}
    db.append(credentials)
    print(db)
    login()


def login():
    print("THIS IS THE LOGIN SECTION")
    print("Input your login credentials below")
    name = input("Name: ")
    password = input("Password: ")
    for users in db:
        if users["name"] == name and users["password"] == password:
            print("Login successful")
            item()
            return
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
        item_bought = input("Enter Item : ")
        if item_bought == "done":
            break
        for product in products:
            if product["name"] == item_bought:
                cart_items.append(product["name"])
                amount += product["price"]
                print('Added! continue shopping')
                break
    print(f"The item you bought are {cart_items}")
    print(f"The total amount you will pay is ${amount} ")


welcome()
