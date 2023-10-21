
class User:
  username = ''
  email = ''
  age = 0
  

  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

  def get_username(self):
     return self.username  
  
  def set_address(self, address):
     self.address = address

  def set_age(self, age):
     self.age = age

  def get_address(self):
     return self.age

  def get_age(self):
     return self.age   

# user1 = User('tony', 'tony@gmail.com', '1234')
# user2 = User('Blair', 'blair@gmail.com', '1000')
# user1.set_age(13)
# print(user1.get_username())
# print(user1.get_age())
    
   

class Item:
   name = ''
   price = 0
   manufacturer_date = ''
   expire_date = ''
   discount = 0.2
   discount_price = 0


   def __init__(self, name, price):
      self.name = name
      self.price = price

   def get_discount_price(self):
      self.discount_price = self.price * self.discount
      return self.discount_price


   def set_discount(self, discount):
      self.discount = discount
   
      
# milo = Item('milo', 5)

# nido = Item('nido', 6)
# iphone = Item('iphone', 250)
# # print(iphone.get_discount_price())

# products = [milo, nido, iphone]


class Cart:
  
   def __init__(self, user):
      self.user = user
      self.item_cart = []


   def add_product(self, item):
      self.item_cart.append(item)


                  
   def get_items(self):
      for item in self.item_cart:
          print (f"{item.name} ${item.price}")

   def get_total_price(self):
      total = 0
      for item in self.item_cart:
          total += item.price
      print (f"Total Cost Price: ${total}")
             

   def clear_cart(self):
      self.item_cart = []                  

# cart1 = Cart(user1) 
# cart2 = Cart(user2)


# cart1.add_product(milo)
# cart1.add_product(iphone)
# cart1.add_product(nido)

# cart1.get_items()
# cart1.get_total_price()

# print()
# cart2.add_product(milo)
# cart2.add_product(nido) 
# cart2.get_items()
# cart1.clear_cart()



def register():
   print()
   print("Registry Section")
   username = input("Enter username: ")
   email = input('Email: ')
   password = input('Enter Password: ')
   user = User(username, email, password)
   login(user)


def login(user):
   print()
   print('Login Section')
   username = input("Enter Username: ")
   password = input('Enter Password: ')
   if user.username == username and user.password == password:
      print('Login Successfully')
      shopping(user)
   else:
      print('Invalid Username Or Password!!')   


def shopping(user):
   item_list = []
   items_dic = [{'name':'milo','price':20},
            {'name':'nido', 'price':50},
            {'name':'gari', 'price':10}]

   while True:
      product_name = input('Enter Product to buy: ')
      for products in items_dic:
         if products['name'] == product_name:
            product = products['name']
            price = products['price']
      item = Item(product, price)
      item_list.append(item)
      option = input('Do u want to shop again(y/n): ')
      if option != 'y'.lower():
         break
   cart_items(item_list, user)   


def cart_items(item_list, user):
      cart  = Cart(user)
      for item in item_list:
         cart.add_product(item)
      print(f'The Item(s) {cart.user.username} bought and their Price(s): ')
      cart.get_items()
      cart.get_total_price()
         


def main():
   print('Welcome To Ecommerce')
   while True:
      option = int(input("option\n1.Register\n2.Login\nchoose option:"))
      if option == 1:
         register()
         break
      if option == 2:
         login()
         break
      
main()









# class Car:
   
#    def __init__(self, model, manufacture_year):
#       self.model = model
#       self.manufacturer_year = manufacture_year

  #  def set_model(self, model):
  #     self.model = model

  #  def get_model(self):
  #     return self.model

      

# benz = Car()
# car_model = benz.model
# car_year = benz.manufacturer_year
# print(car_model, car_year)   

# benz = Car()
# benz.set_model('Mercedes')
# print(benz.get_model())   
      

# item,cart,user