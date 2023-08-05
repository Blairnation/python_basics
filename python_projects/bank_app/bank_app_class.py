class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount
        print(f"${amount} added to account successfully")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'{amount} redrawn from account successfully')
        else:
            print("Insufficient balance to redraw!!")

    def show_balance(self):
        return print(f'Your balance is ${self.__balance:,.2f}')

    def __str__(self):
        return f'Your current balance is ${self.__balance:,.2f}'




