import time
import threading


def eat():
    time.sleep(3)
    print('You eat breakfast')


def drink():
    time.sleep(4)
    print('you drank coffee')


def sleep():
    time.sleep(5)
    print('You slept')


x = threading.Thread(target=eat, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=sleep, args=())
z.start()

# starts child thread before main thread
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())

# using daemon threads to stop infinite loops
import time
import threading


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('Logged in for', count, 'seconds')


x = threading.Thread(target=timer, daemon=True)
x.start()

print(threading.main_thread())

print(threading.active_count())
print(threading.enumerate())

obect = input('Do you want ot exit: ')

# Multiprocessing (taking each processor to perform task)

import time
from multiprocessing import Process, cpu_count


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    a = Process(target=counter, args=(112500,))
    b = Process(target=counter, args=(112500,))
    # share processing among CPU's
    # c = Process(target=counter, args=(112500,))
    # d = Process(target=counter, args=(112500,))

    a.start()
    b.start()
    # c.start()
    # d.start()

    a.join()
    b.join()
    # c.join()
    # d.join()

    print('Finished in:', time.perf_counter(), 'seconds')
    print(cpu_count())


if __name__ == '__main__':
    main()

# function determining the number of your cpu to perform task
import time
from multiprocessing import Process, cpu_count


def counter(num):
    count = 0
    for i in range(num):
        count += i * i


def main():
    processes = []
    arg = 1000000000
    for cpu in range(cpu_count()):
        p = Process(target=counter, args=(arg,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print('Finished in:', time.perf_counter(), 'seconds')
    print(cpu_count())


if __name__ == '__main__':
    main()
