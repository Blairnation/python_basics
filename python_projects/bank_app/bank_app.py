import bank_app_class


def main():
    amount = welcome()
    bank = bank_app_class.BankAccount(amount)

    again = 0
    while again == 0:
        try:
            display_menu()
            select = int(input("Select option: "))
            if select == 1:
                deposit = float(input("Enter amount to deposit: "))
                bank.deposit(deposit)

            elif select == 2:
                withdraw = float(input("Enter amount to redraw: "))
                bank.withdraw(withdraw)

            elif select == 3:
                bank.show_balance()
                print(bank)

            elif select == 4:
                print("Program Exiting.......")
                break
            else:
                print("Invalid Option Selected")
                print("Select a valid option")
            print("Enter 0 to go back to menu or Enter any digit to exit")
            again = int(input("Enter:  "))
            if again != 0:
                print('Program Exiting...')
                break

        except ValueError:
            print('Enter a digit number!!')
    else:
        print("Unknown Input")
        print("Program exiting....")


def welcome():
    print("Welcome to Tony's Banking App")
    print("______________________________")
    print()
    print("Account Inactive")
    print("Enter initial deposit to activate account")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Enter a valid amount")
                continue
            else:
                print(f"Your initial deposit is ${amount}")
                print("Account Activated")
                print()
            return amount
        except ValueError:
            print("Alphabet not Accepted!! Enter a number")


def display_menu():
    print("""Banking Service Menu
------------
1.Deposit
2.Withdraw
3.Show balance
4.Quit""")


main()
