class CellPhone:
    def __init__(self, manufacturer, model_number, retail_price):
        self.__manufacturer = manufacturer
        self.__model_number = model_number
        self.__retail_price = retail_price

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_model_number(self, model_number):
        self.__model_number = model_number

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model_number(self):
        return self.__model_number

    def get_retail_price(self):
        return self.__retail_price


def main():
    make = make_list()

    display_list(make)


def make_list():
    phone_list = []
    for cell in range(5):
        manu = input("Enter manufacturer: ")
        model = input("Enter model number: ")
        retail = float(input("Enter retail price: "))
        phone = CellPhone(manu, model, retail)
        phone_list.append(phone)
    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufacturer())
        print(item.get_model_number())
        print(item.get_retail_price())


# hospital

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number,
                 emergency_contact_name, emergency_contact_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_middle_name(self):
        return self.__middle_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_zip_code(self):
        return self.__zip_code

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def set_emergency_contact_name(self, emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone

    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.__emergency_contact_phone = emergency_contact_phone

    def __str__(self):
        return f'First name: {self.__first_name}\n' \
               f'Middle name: {self.__middle_name}\n' \
               f'Last name: {self.__last_name}\n' \
               f'Address: {self.__address}\n' \
               f'City: {self.__city}\n' \
               f'State: {self.__state}\n' \
               f'Zip code: {self.__zip_code}\n' \
               f'Phone number: {self.__phone_number}\n' \
               f'Name of emergency contact: {self.__emergency_contact_name}\n' \
               f'Phone number of emergency contact: {self.__emergency_contact_phone}'


class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner_name, procedure_charges):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitioner = practitioner_name
        self.__procedure_charges = procedure_charges

    def get_procedure_name(self):
        return self.__procedure_name

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def get_procedure_date(self):
        return self.__procedure_date

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def get_practitioner(self):
        return self.__practitioner

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def get_procedure_charges(self):
        return self.__procedure_charges

    def set_procedure_charges(self, procedure_charges):
        self.__procedure_charges = procedure_charges

    def __str__(self):
        return f'Name of procedure: {self.__procedure_name}\nDate of procedure: {self.__procedure_date}\nName of ' \
               f'practitioner: {self.__practitioner}\nCharges for procedure: ${self.__procedure_charges} '


def main():
    patient = Patient('Yeboah', 'Tony', 'Blair', 'Dream.field', 'Accra', 'Ghana', '202-930-393', 987654321, 'Bhim', 222)
    procedure1 = Procedure('Physical Exam', '13/02/2000', 'Dr. Irvine', 250.00)
    procedure2 = Procedure('X-ray', '13/02/2000', 'Dr. Jamison', 500.00)
    procedure3 = Procedure('Blood test', '13/02/2000', 'Dr. Smith', 200.00)
    print('Patient Information')
    print(patient)
    print()
    print('Procedure #1')
    print(procedure1)
    print()
    print('Procedure #2')
    print(procedure2)
    print()
    print('Procedure #3')
    print(procedure3)
    print()
    total_charges = procedure1.get_procedure_charges() + procedure2.get_procedure_charges() + \
                    procedure3.get_procedure_charges()
    print(f'The total charge is ${total_charges}')


# pro from tony

import pickle


class Employee:
    def __init__(self, name, id_num, department, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'ID number: {self.__id_num}\n' \
               f'Department: {self.__department}\n' \
               f'Job title: {self.__job_title}'


# functions
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = 'employee_data.dat'


def main():
    dic = load()

    while True:
        try:
            option = menu()
            if option == LOOKUP:
                look_up(dic)
            elif option == ADD:
                add(dic)
            elif option == CHANGE:
                change(dic)
            elif option == DELETE:
                delete(dic)
            elif option == QUIT:
                upload(dic)
                print("Program Quiting...")
                break
        except ValueError:
            print("Enter a valid digit")


def load():
    try:
        infile = open(FILENAME, 'rb')
        dic = pickle.load(infile)
        infile.close()
    except IOError:
        dic = {}
    return dic


def menu():
    print()
    print('Employee Information Menu')
    print("___________________________")
    print()
    print('1.Look Up Employee\n'
          '2.Add New Employee\n'
          '3.Change Employee Information\n'
          '4.Delete An Employee\n'
          '5.Quit Program')
    option = int(input('Select option: '))
    while option < LOOKUP or option > QUIT:
        option = int(input("Select options available: "))
    return option


def look_up(dic):
    print('Enter ID number to look up information')
    id_num = int(input("Enter: "))
    if id_num in dic:
        print()
        print(dic[id_num])
    else:
        print("Invalid ID Number!!")


def add(dic):
    print("Enter ID number to add information")
    id_num = int(input("Enter: "))
    if id_num not in dic:
        name = input("Enter name: ")
        department = input("Enter department: ")
        job_title = input('Enter job title: ')
        employee = Employee(name, id_num, department, job_title)
        dic[id_num] = employee
        print("Information Added Successfully")
    else:
        print('ID Number Already Exists')


def change(dic):
    print('Enter ID number to change information')
    id_num = int(input("Enter: "))
    if id_num in dic:
        name = input("Enter new name: ")
        department = input("Enter new department: ")
        job_title = input("Enter new job title: ")
        emp = Employee(name, id_num, department, job_title)
        dic[id_num] = emp
        print("Information Updated Successfully")
    else:
        print("Invalid ID Number!!")


def delete(dic):
    id_num = int(input("Enter ID number to delete information: "))
    if id_num in dic:
        del dic[id_num]
        print('Information Deleted Successfully')
    else:
        print('ID number not found!!')


def upload(dic):
    outfile = open(FILENAME, 'wb')
    pickle.dump(dic, outfile)
    outfile.close()


# shop(register class take retail class object)

class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.__description = description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_units_in_inventory(self, units):
        self.__units_in_inventory = units

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price


class CashRegister:
    def __init__(self):
        self.__cash_list = []

    def purchase_item(self, item):
        self.__cash_list.append(item)

    def get_total(self):
        total = 0
        for item in self.__cash_list:
            total += item.get_price()
        return total

    def Show_items(self):
        count = 0
        if self.__cash_list:
            for item in self.__cash_list:
                count += 1
                print(f'Item #{count}')
                print(f'Description: {item.get_description()}\n'
                      f'Price: ${item.get_price()}')
                print()
        else:
            print('No item Available')

    def clear(self):
        self.__cash_list = []


def main():
    retail1 = RetailItem('Gucci shirt', '120cm', 50)
    retail2 = RetailItem('Dior bag', '70cm', 100)
    retail3 = RetailItem('Balenciaga shoe', '60cm', 150)

    register = CashRegister()
    register.purchase_item(retail1)
    register.purchase_item(retail2)
    register.purchase_item(retail3)

    print('Do you want to check your purchase item(s) and price(s)')
    again = input('y for yes and n for no: ').lower()
    while again == 'y':
        register.Show_items()
        print()
        print(f"The total price is ${register.get_total()}")
        break

    print()
    register.clear()
    register.Show_items()


# polymorphism

class Mammal:
    def __init__(self, species):
        self.__species = species

    def get_species(self):
        print(f'I am a {self.__species}')

    def make_sound(self):
        print("Grrrrr")


class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'dog')

    def make_sound(self):
        print('Wooow')


class Cat(Mammal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        super().make_sound()
        print('Meow')


def main():
    mammal = Mammal('regular mammal')
    dog = Dog()
    cat = Cat('cat')
    show(mammal)
    show(dog)
    show(cat)
    show('I am a string')


def show(animal):
    if isinstance(animal, Mammal):
        animal.get_species()
        animal.make_sound()
        print()


main()

dog = Dog()
dog.make_sound()


# questions and answers project(capital city)

class Question:
    def __init__(self, question, possible_ans, correct_ans):
        self.question = question
        self.possible_ans = possible_ans
        self.correct_ans = correct_ans

    def display_question(self):
        print(self.question)
        for index, answer in enumerate(self.possible_ans, start=1):
            print(f'({index}). {answer}')

    def check_answer(self, answers):
        return answers == self.correct_ans


def question_call():
    questions = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2),
        Question("What is the capital of Germany?", ["Berlin", "Paris", "Rome", "London"], 1),
        Question("What is the capital of Spain?", ["Madrid", "Athens", "Amsterdam", "Lisbon"], 3),
        Question("What is the capital of Italy?", ["Rome", "Vienna", "Moscow", "Dublin"], 2),
        Question("What is the capital of Canada?", ["Ottawa", "Washington D.C.", "London", "Paris"], 4),
        Question("What is the capital of Australia?", ["Canberra", "Sydney", "Melbourne", "Perth"], 3),
        Question("What is the capital of Japan?", ["Tokyo", "Beijing", "Seoul", "Osaka"], 4),
        Question("What is the capital of Brazil?", ["Brasília", "Rio de Janeiro", "São Paulo", "Buenos Aires"], 2),
        Question("What is the capital of India?", ["New Delhi", "Mumbai", "Bangkok", "Jakarta"], 1),
        Question("What is the capital of South Africa?", ["Pretoria", "Cape Town", "Johannesburg", "Nairobi"], 3)
    ]
    return questions


def game(questions):
    player1_score = 0
    player2_score = 0
    for question in questions:
        print("Player number 1")
        question.display_question()
        answer = int(input('Enter answer(1-4): '))
        if question.check_answer(answer):
            print('Correct')
            player1_score += 1
        else:
            print('Incorrect')
            print()

        print('Player number 2')
        question.display_question()
        answer = int(input("Enter answer(1-4): "))
        if question.check_answer(answer):
            print("Correct")
            player2_score += 1

        else:
            print("Incorrect")
            print()

    print(f'Player1 score: {player1_score}')
    print(f'Player2 score: {player2_score}')
    if player1_score > player2_score:
        print('Player1 wins')
    if player2_score > player1_score:
        print("Player2 wins")
    else:
        print('Tied')


def main():
    questions = question_call()
    game(questions)


main()
