a = [1, 2, 3, 4]
print(a)
print(a[-1])
b = a * 2
print(b)

import numpy as np

a = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(a)
b = np.array([1, 2, 3, 4])
print(a * b)

c = a.tolist()
print(c)

import pandas as pd

data = pd.read_csv("/home/jannusch/Documents/uni/python_course/tasks/week_seven/data.csv")
data2 = pd.read_excel("/home/jannusch/Documents/uni/python_course/tasks/week_seven/data.xlsx")
datanp = np.array(data)

np.save("/home/jannusch/Documents/uni/python_course/tasks/week_seven/data.npy", datanp)
np.savetxt("/home/jannusch/Documents/uni/python_course/tasks/week_seven/data.txt", datanp)


def is_even(number):
    return ((number % 2) == 0)

def is_odd(number):
    return not is_even(number)

def is_divisible_by_3(number):
    return ((number % 3) == 0)

def print_numbers(func, numbers):
    print(func.__name__)
    for number in numbers:
        if func(number):
            print(number)

numbers = range(11)

print_numbers(is_odd, numbers)

print_numbers(lambda x: x % 2 == 0, numbers)