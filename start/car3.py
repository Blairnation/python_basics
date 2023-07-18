import datetime


class EENG208_20:
    def __init__(self):
        self.product = {"laptop": "laptop",
                        "pen drive": "pen drive",
                        "hard disk": "hard disk"
                        }

    def greet_user(self):
        now = datetime.datetime.now()
        hour = now.hour
        if hour < 12:
            print(f"Good morning {name}")
        elif 12 <= hour < 18:
            print(f"Good afternoon {name}")
        else:
            print(f"Good evening {name}")

    def displaying_product(self):
        print("These are the products available")
        for local_name, standard_name in self.product.items():
            print(f"{local_name}:{standard_name}")

    def price_function(self, product_name):
        prices = {"laptop": "1500",
                  "pen drive": "100",
                  "hard disk": " 300"}
        return prices.get(product_name, "Product Not Found!")

    def delivery_function(self):
        print("How do you want to receive product")
        print('''
1.delivery
2.self pickup
3.use product at the shop
        ''')
        option = input("Enter your choice: ")
        if option == "1":
            print("you have chosen delivery")
        if option == "2":
            print("you have chosen self pickup")
        if option == "3":
            print("you have chosen use product at the shop ")


eeng208_20 = EENG208_20()
print("WELCOME TO  BLAIR COMPUTERS")
name = "Tony"
eeng208_20.greet_user()
print(f"Please {name}, "
      f"Which service do you want from the company.")
print('''1. Buying product
2. Survey''')
access = input("Enter 1 or 2: ")
if access == "1":
    eeng208_20.displaying_product()
    product = input("Enter product name: ")
    price = eeng208_20.price_function(product)
    print(f"The price of {product} is {price}")
    eeng208_20.delivery_function()
else:
    print("Invalid")
