import pickle


def main():
    outfile = open('dic_pickle2.dat', 'wb')
    again = 'y'.lower()
    while again == 'y':
        make_file(outfile)
        again = input("Do you want to add information again(y/n): ")


def make_file(outfile):
    person = {}

    person['name'] = input("name: ")
    person['age'] = int(input("age: "))
    person['weight'] = float(input('Weight: '))

    pickle.dump(person, outfile)


# unpickle

import pickle


def main():
    infile = open('dic_pickle2.dat', 'rb')
    end_of_file = False
    while not end_of_file:
        try:
            person = pickle.load(infile)
            show_item(person)
        except EOFError:
            end_of_file = True


def show_item(person):
    print(f'Name: {person["name"]}')
    print(f'Age: {person["age"]}')
    print(f'Weight: {person["weight"]}')
    print()


# simple unpickle
import pickle


def main():
    outfile = open('dic_pickle.dat', 'rb')
    end_of_file = False
    count = 0
    while not end_of_file:
        try:
            count += 1
            print(f'Person #{count}')
            self = pickle.load(outfile)
            print(f'Name: {self["name"]}')
            print(f'Age: {self["age"]}')
            print(f'height: {self["height"]}')
            print()
        except EOFError:
            end_of_file = True
    outfile.close()





