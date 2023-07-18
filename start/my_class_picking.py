import pickle
import Accessor_mutator as am


def main():
    outfile = open("phones.dat", 'wb')
    while True:
        phone_list = get_items()
        pickle.dump(phone_list, outfile)
        again = input("Do you want to store phones information again (y/n):")
        if again != "y".lower():
            print("All information saved. Quiting...")
            break
    outfile.close()


def get_items():
    phone_list = []
    manu = input("Enter manufacturer: ")
    model = input("Enter model number: ")
    retail = float(input("Enter retail price: "))
    phone = am.CellPhone(manu, model, retail)
    phone_list.append(phone)
    return phone_list


import pickle
import Accessor_mutator as am


def main():
    end_of_file = False
    infile = open("phones.dat", 'rb')
    while not end_of_file:
        try:
            phones = pickle.load(infile)
            show_items(phones)

        except EOFError:
            end_of_file = True


def show_items(phones):
    for item in phones:
        print(f'Manufacturer: {am.CellPhone.get_manufacturer(item)}')
        print(f'Model number: {am.CellPhone.get_model_number(item)}')
        print(f'Retail price : {am.CellPhone.get_retail_price(item)}')
        print()



