import numpy as np
from utils import *
from time import time


def step_1(filename):
    with open(filename) as f:
        towels, patterns = f.read().split("\n\n")
    towels = towels.strip().split(", ")
    patterns = patterns.strip().split("\n")
    count = 0
    for pattern in patterns:
        possible_length = {0: True}
        for pattern_length in range(1, len(pattern) + 1):
            possible_length[pattern_length] = False
            for towel in towels:
                if (
                    possible_length.get(pattern_length - len(towel), False)
                    and pattern[pattern_length - len(towel) : pattern_length] == towel
                ):
                    possible_length[pattern_length] = True
                    break
        if possible_length.get(len(pattern), False):
            count += 1

    return count


def step_2(filename):
    with open(filename) as f:
        towels, patterns = f.read().split("\n\n")
    towels = towels.strip().split(", ")
    patterns = patterns.strip().split("\n")
    count = 0
    for pattern in patterns:
        ways_to_do_lengths = {0: 1}
        for pattern_length in range(1, len(pattern) + 1):
            ways_to_do_lengths[pattern_length] = 0
            for towel in towels:
                if (
                    pattern_length - len(towel) >= 0
                    and pattern[pattern_length - len(towel) : pattern_length] == towel
                ):
                    ways_to_do_lengths[pattern_length] += ways_to_do_lengths[
                        pattern_length - len(towel)
                    ]

        count += ways_to_do_lengths.get(len(pattern), 0)

    return count


print(step_1("2024/19_test.txt"))
print(step_1("2024/19_input.txt"))

print(step_2("2024/19_test.txt"))
print(step_2("2024/19_input.txt"))

