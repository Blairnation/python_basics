class MobileMoney:
    def __init__(self):
        self.__balance = 0
        self.__gov_tax_rate = 0.04
        self.__momo_tax_rate = 0.025

    def send(self, amount):
        total = amount - (amount * (self.__gov_tax_rate + self.__momo_tax_rate))
        if self.__balance >= total:
            self.__balance -= total
        else:
            print('Insufficient Balance!!')

    def deposit(self, amount):
        self.__balance += amount

    def redraw(self, amount):
        total = amount - (amount * self.__momo_tax_rate)
        if self.__balance >= total:
            self.__balance -= total
        else:
            print('Insufficient Balance!!')

    def balance(self):
        return self.__balance

    def __str__(self):
        return f'Current Balance: ${self.__balance}\n' \
               f'Available Balance: ${self.__balance}'


money = MobileMoney()
money.deposit(1000)
print(money.balance())
# money.redraw(200)
# print(money.balance())
