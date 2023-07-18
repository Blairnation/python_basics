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
