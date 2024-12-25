import numpy as np
from time import time
from utils import *


def step_1(filename):
    exec_time = time()
    f = open(filename)
    patterns = f.read().split("\n\n")
    f.close()
    locks = []
    keys = []
    for pattern in patterns:
        if pattern[0] == "#":
            # it's a lock !
            lock = np.array([0] * 5)
            for i in range(5):
                for j in range(5):
                    if pattern[6 + i * 6 + j] == "#":
                        lock[j] += 1
            locks.append(lock)

        else:
            # it's a key !
            key = np.array([0] * 5)
            for i in range(5):
                for j in range(5):
                    if pattern[30 - i * 6 + j] == "#":
                        key[j] += 1
            keys.append(key)

    count = 0
    for lock in locks:
        for key in keys:
            if np.all(lock + key <= 5):
                count += 1

    print("Part 1 exec time :", time() - exec_time)
    return count


print(step_1("2024/25_test.txt"))
print(step_1("2024/25_input.txt"))

