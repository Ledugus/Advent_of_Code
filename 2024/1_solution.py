import numpy as np


def step_1(filename):

    f = open(filename)
    l1 = []
    l2 = []
    for line in f.readlines():
        n, m = line.split()
        l1.append(int(n))
        l2.append(int(m))
    l1 = np.array(sorted(l1))
    l2 = np.array(sorted(l2))

    f.close()
    return sum(np.abs(l1 - l2))


def step_2(filename):
    f = open(filename)

    l1 = set([])
    l2 = []
    sum = 0
    for line in f.readlines():
        n, m = line.split()
        l1.add(int(n))
        l2.append(int(m))

    l2.sort()

    for i in l1:
        sum += i * l2.count(i)
    f.close()
    return sum


print(step_1("2024/1_input.txt"))
print(step_2("2024/1_input.txt"))

