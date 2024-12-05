import numpy as np
from functools import cmp_to_key


def is_sorted(arr, rules):
    new_array = sorted(arr, key=cmp_to_key(lambda x, y: -1 if [x, y] in rules else 1))
    return new_array == arr, new_array


def step_1(filename):
    f = open(filename)
    rules, updates = map(lambda x: x.strip().split("\n"), f.read().split("\n\n"))
    rules = list(map(lambda x: list(map(int, x.split("|"))), rules))
    updates = list(map(lambda x: list(map(int, x.split(","))), updates))

    f.close()
    return sum(
        update[len(update) // 2] for update in updates if is_sorted(update, rules)[0]
    )


def step_2(filename):
    f = open(filename)

    rules, updates = map(lambda x: x.strip().split("\n"), f.read().split("\n\n"))
    rules = list(map(lambda x: list(map(int, x.split("|"))), rules))
    updates = list(map(lambda x: list(map(int, x.split(","))), updates))
    count = 0

    for update in updates:
        correct, corrected_update = is_sorted(update, rules)
        if not correct:
            count += corrected_update[len(corrected_update) // 2]
    f.close()
    return count


print(step_1("2024/05_input.txt"))

print(step_2("2024/05_input.txt"))
