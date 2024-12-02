import numpy as np


def check(line):
    if line[0] == line[1]:
        return False

    sign = np.sign(int(line[0]) - int(line[1]))
    for i in range(1, len(line)):
        if not (0 < sign * (line[i - 1] - line[i]) <= 3):
            return False
    return True


def check2(line):
    for i in range(len(line)):
        new_line = line[:]
        del new_line[i]
        if check(new_line):
            return True
    return False


def step_1(filename):
    f = open(filename)
    sum = 0
    for line in f.readlines():
        l = list(map(int, line.split(" ")))
        if check(l):
            sum += 1
    f.close()
    return sum


def step_2(filename):
    f = open(filename)
    sum = 0
    for line in f.readlines():
        l = list(map(int, line.split(" ")))
        if check2(l):
            sum += 1
    f.close()
    return sum


print(step_1("2024/02_input.txt"))

print(step_2("2024/02_input.txt"))
