import numpy as np
from utils import *


def process_block(block):
    buttonA = np.array(
        list(
            map(
                lambda x: int(x.split("+")[-1]),
                block.split("\n")[0].split(": ")[1].split(", "),
            )
        )
    )
    buttonB = np.array(
        list(
            map(
                lambda x: int(x.split("+")[-1]),
                block.split("\n")[1].split(": ")[1].split(", "),
            )
        )
    )
    prize_pos = np.array(
        list(
            map(
                lambda x: int(x.split("=")[-1]),
                block.split("\n")[2].split(": ")[1].split(", "),
            )
        )
    )
    return buttonA, buttonB, prize_pos


def solve_linear_system(A, B, P):

    det = A[0] * B[1] - A[1] * B[0]
    x = (P[0] * B[1] - P[1] * B[0]) / det
    y = (A[0] * P[1] - A[1] * P[0]) / det
    if x.is_integer() and y.is_integer():
        return int(x) * 3 + int(y)
    return 0


def step_1(filename):
    f = open(filename)
    count = 0
    blocks = f.read().split("\n\n")
    for block in blocks:
        A, B, P = process_block(block)
        count += solve_linear_system(A, B, P)
    f.close()
    return count


def step_2(filename):
    f = open(filename)
    count = 0
    blocks = f.read().split("\n\n")
    f.close()
    for block in blocks:
        A, B, P = process_block(block)
        P += 10000000000000
        count += solve_linear_system(A, B, P)

    return count


print(step_1("2024/13_test.txt"))
print(step_1("2024/13_input.txt"))

print(step_2("2024/13_test.txt"))
print(step_2("2024/13_input.txt"))

