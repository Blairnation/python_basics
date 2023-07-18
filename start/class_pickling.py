import pickle
import Accessor_mutator as AM


def main():
    print("Enter the following information for your car")
    outfile = open("cars_class_pickle.dat", 'wb')
    again = 'y'.lower()
    while again == "y":
        manu = input("Enter manufacturer: ")
        model = input("Enter model: ")
        retail = float(input("Enter retail price: "))

        cars = AM.CellPhone(manu, model, retail)
        pickle.dump(cars, outfile)

        again = input("Do you want to enter car information again(y/n): ")

    outfile.close()


import pickle
from Accessor_mutator import CellPhone


def main():
    end_of_file = False
    infile = open("cars_class_pickle.dat", 'rb')
    while not end_of_file:
        try:
            cars = pickle.load(infile)
            show(cars)
        except EOFError:
            end_of_file = True


def show(cars):
    print(f'Manufacturer: {cars.get_manufacturer()}')
    print(f'Model Number: {cars.get_model_number()}')
    print(f'Retail Price: {cars.get_retail_price()}')
    print()




