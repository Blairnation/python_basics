from functools import reduce

def main():
    numbers = [5, 2, 3, 4, 5, 6]
    letters = ['a', 'b']
    doubler = map(lambda x, y: x * y, letters, numbers)
    print(list(doubler))


age_check = lambda age: True if age >= 18 else False
print(age_check(18))

doubler = lambda x: x * 2
print(doubler(7))


# From functools import reduce
add_list = [1, 2, 3, 4, 5]
adder = reduce(lambda x, y: x + y, add_list)
print(adder)

check_even = lambda x: True if x % 2 == 0 else False
print(check_even(6))

full_name = lambda first_name, last_name: first_name + ' ' + last_name
print(full_name("Tony", 'Blair'))
