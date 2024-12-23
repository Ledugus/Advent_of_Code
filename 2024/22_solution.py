import numpy as np
from time import time
from utils import *

SPECIAL_MOD = 2**24 - 1


def evolve_number(number):
    number = (number ^ (number << 6)) & SPECIAL_MOD
    number = (number ^ (number >> 5)) & SPECIAL_MOD
    number = (number ^ (number << 11)) & SPECIAL_MOD
    return number


def step_1(filename):
    t = time()
    f = open(filename)
    secret_numbers = [int(x.strip()) for x in f.read().splitlines()]
    f.close()

    count = 0
    for secret_number in secret_numbers:
        for i in range(2000):
            secret_number = evolve_number(secret_number)
        count += secret_number

    print("Part 1 exec time", time() - t)
    return count


def step_2(filename):
    t = time()
    f = open(filename)
    secret_numbers = [int(x.strip()) for x in f.read().splitlines()]
    f.close()
    total_of_sequences = {}
    for secret_number in secret_numbers:
        seen_sequences = set()
        previous_price = secret_number % 10
        sequence = tuple([0] * 4)
        for i in range(1, 2001):
            secret_number = evolve_number(secret_number)
            current_price = secret_number % 10
            sequence = (*sequence[1:], current_price - previous_price)
            if i >= 4:
                condition = sequence not in seen_sequences
                if condition:
                    total_of_sequences[sequence] = (
                        total_of_sequences.get(sequence, 0) + current_price
                    )
                    seen_sequences.add(sequence)
            previous_price = current_price

    print("Part 2 exec time :", time() - t, "secondes")
    return max(total_of_sequences.values())


# print(step_1("2024/22_test.txt"))
# print(step_1("2024/22_input.txt"))

# print(step_2("2024/22_test.txt"))
print(step_2("2024/22_input.txt"))
