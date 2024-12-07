import numpy as np
from utils import *


def calculate_operations_on_numbers(ops, numbers, sum_):
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == "1":
            result *= numbers[i + 1]
        elif op == "2":
            result = int(str(result) + str(numbers[i + 1]))
        else:
            result += numbers[i + 1]
        if result > sum_:
            return False

    return result == sum_


def step_1(filename):
    f = open(filename)
    count = 0
    c = 0
    for line in f.readlines():

        c += 1
        sum_, numbers = line.strip().split(": ")
        sum_, numbers = int(sum_), list(map(int, numbers.split(" ")))

        for i in range(2 ** (len(numbers) - 1)):
            o = format(i, f"0{len(numbers)-1}b")
            if calculate_operations_on_numbers(o, numbers, sum_):
                count += sum_
                break

    f.close()
    return count, c


def step_2(filename):
    f = open(filename)
    count = 0
    c = 0
    for line in f.readlines():

        sum_, numbers = line.strip().split(": ")
        sum_, numbers = int(sum_), list(map(int, numbers.split(" ")))

        c += 1
        for i in range(3 ** (len(numbers) - 1)):
            print(c, i)
            str_ternary = np.base_repr(i, base=3)
            o = "0" * (len(numbers) - 1 - len(str_ternary)) + str_ternary
            if calculate_operations_on_numbers(o, numbers, sum_):
                count += sum_
                break

    f.close()
    return count, c


print(step_1("2024/07_test.txt"))
print(step_1("2024/07_input.txt"))

print(step_2("2024/07_test.txt"))
print(step_2("2024/07_input.txt"))
