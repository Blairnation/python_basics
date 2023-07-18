# creating steps file

import random


def generate_random_nums():
    steps_list = []
    for index in range(365):
        numbers = random.randint(1000, 2000)
        steps_list.append(str(numbers))
    return steps_list


def create_file(steps_list):
    with open('steps.txt', 'w') as outfile:
        outfile.write('\n'.join(steps_list))


steps = generate_random_nums()
create_file(steps)

# checking steps file


def main():
    with open("steps.txt", 'r') as outfile:
        count = 0
        file = outfile.readline().strip()
        while file != '':
            count += 1
            print(f'#{count}: {file}')
            file = outfile.readline().strip()


main()


# checking step average for months
def read_steps_file():
    steps_list = []
    with open('steps.txt', 'r') as infile:
        for line in infile:
            line = line.strip()
            steps_list.append(int(line))
        return steps_list


def calc_average(step_list):
    averages = []
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    for index in range(0, len(step_list), 30):
        step_sum = sum(step_list[index:index + 30])
        average = step_sum / 30
        averages.append(average)
    return zip(months, averages)


def display_month_averages(averages):
    for month, average in averages:
        print(f'Average of {month}: {average:.2f}')


def main():
    file = read_steps_file()
    averages = calc_average(file)
    display_month_averages(averages)


main()


# question
# A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
# burned, heart rate, sleeping patterns, and so on. One common physical activity that most
# of these devices track is the number of steps you take each day.
# If you have downloaded this book’s source code from the Premium Companion Website,
# you will find a file named steps.txt in the Chapter 06 folder. (The Premium Companion
# Website can be found at www.pearsonglobaleditions.com/gaddis.) The steps.txt file
# contains the number of steps a person has taken each day for a year. There are 365 lines
# in the file, and each line contains the number of steps taken during a day. (The first line is
# the number of steps taken on January 1st, the second line is the number of steps taken on
# January 2nd, and so forth.) Write a program that reads the file, then displays the average
# number of steps taken for each month. (The data is from a year that was not a leap year,
# so February has 28 days.)
