# write or append

def main():
    coffee_file = open('coffee.txt', 'a')
    again = 'y'

    while again == 'y'.lower():
        descript = input("Enter coffee description: ")
        qty = float(input("Enter coffee quantity: "))
        coffee_file.write(descript + '\n')
        coffee_file.write(str(qty) + '\n')

        print("Do you want to add another coffee specifications")
        again = input("Enter y for yes and anything for no: ")

    coffee_file.close()
    print("New coffee specification has been added")


main()


# read

def main():
    coffee_file = open('coffee.txt', 'r')
    count = 0
    print("Coffee description and their quantities")

    descript = coffee_file.readline().rstrip('\n')
    while descript != '':
        qty = coffee_file.readline().rstrip('\n')
        count += 1
        print(f"Coffee #{count} Specifications")
        print('_______________________')
        print(f"Description: {descript}")
        print(f'Quantity(Pounds): {qty}')
        print()

        descript = coffee_file.readline().rstrip('\n')

    coffee_file.close()


main()


# search description to get quantity
def main():
    found = False
    print("Enter the coffee description to display quantity")
    search = input("Enter the description: ")

    coffee_file = open('coffee.txt', 'r')
    descript = coffee_file.readline()
    while descript != '':
        qty = coffee_file.readline()
        descript = descript.rstrip('\n')
        if descript == search:
            print(f"Description: {descript}")
            print(f'Quantity(Pounds): {qty}')
            found = True
            break
        descript = coffee_file.readline()
    coffee_file.close()
    if not found:
        print("Coffee description Unavailable")


main()

# change quantity and add all to new file

import os


def main():
    found = False
    print("Enter the description to update the quantity")
    search = input("Enter description: ")
    new_qty = float(input("Enter new quantity for description: "))
    coffee_file = open("coffee.txt", 'r')
    temp_file = open("temp.txt", 'w')
    descript = coffee_file.readline().rstrip('\n')
    while descript != '':
        qty = coffee_file.readline().rstrip('\n')
        descript = descript.rstrip('\n')

        if descript == search:
            temp_file.write(descript + '\n')
            temp_file.write(str(new_qty) + '\n')
            found = True
        else:
            temp_file.write(descript + '\n')
            temp_file.write(qty + '\n')

        descript = coffee_file.readline().rstrip('\n')
    coffee_file.close()
    temp_file.close()

    os.remove('coffee.txt')
    os.rename('temp.txt', "coffee.txt")

    if found:
        print("Description's quantity have been updated")
    else:
        print("Description not found")


main()

# delete item entered

import os


def main():
    found = False
    print("Enter coffee description to be be deleted")
    search = input("Enter description: ")

    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    descript = coffee_file.readline().rstrip('\n')
    while descript != '':
        qty = coffee_file.readline().rstrip('\n')

        if descript != search:
            temp_file.write(descript + '\n')
            temp_file.write(qty + '\n')
        else:
            found = True

        descript = coffee_file.readline().rstrip('\n')

    coffee_file.close()
    temp_file.close()

    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')
    if found:
        print("File has been updated")
    else:
        print("Description not found")


main()


# html makeup
def main():
    name = input("Enter name: ")
    description = input("Describe yourself: ")
    write_html_file(name, description)


def write_html_file(name, description):
    html_contents = (f'''<html>
<head>
</head>
<body>
    <center>
        <h1>{name}
     </center>
     < hr />
     {description}
</body>
</html>''')

    html_file = open('user_page.html', 'w')
    html_file.write(html_contents + '\n')
    html_file.close()
    print("File has been written to HTML document")


main()



# cold

import os


def main():
    while True:
        found = False

        search = input("Enter name: ")
        new_age = input("Enter new age: ")
        infile = open('try.txt', 'r')
        temp_file = open('temp.txt', 'w')
        name = infile.readline().rstrip('\n')
        while name != '':
            age = infile.readline().rstrip('\n')

            if name == search:
                temp_file.write(name + '\n')
                temp_file.write(new_age + '\n')
                found = True

            else:
                temp_file.write(name + '\n')
                temp_file.write(age + '\n')

            name = infile.readline().rstrip('\n')

        infile.close()
        temp_file.close()

        os.remove('try.txt')
        os.rename('temp.txt', 'try.txt')

        if found:
            print("Name found. New age stored...")
        if not found:
            print('Name not found!!')
            print("Enter a valid name!!")
            continue

        again = input("Again(y/n): ")
        if again != 'y'.lower():
            print("Program quiting...")
            break





