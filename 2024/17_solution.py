import numpy as np
from utils import *


def apply_program(register):
    out = ""
    while register[0] != 0:
        # 1. (2 | 4) -> b = a % 8
        # 2. (1 | 5) -> b = b ^ 5
        register[1] = (register[0] % 8) ^ 5

        # 3. (7 | 5) -> c = a // (2**b)
        register[2] = register[0] // (2 ** register[1])
        # on peut tout réduire modulo 8, même si c'est pas l'opération décrite dans l'énoncé

        # 4. (1 | 6) -> b = b ^ 6
        register[1] = register[1] ^ 6

        # 5. (0 | 3) -> a = a // 8
        register[0] = register[0] // 8

        # 6. (4 | 2) -> b = b ^ c
        register[1] = register[1] ^ register[2]

        # 7. (5 | 5) -> out b % 8
        out += str(register[1] % 8) + ","
        # 8. (3 | 0) -> jump to 1. if a != 0

    return out[:-1]


def step_1(filename):
    with open(filename) as f:
        x = f.read()
    register = x.split("\n\n")[0]
    register = list(
        map(lambda x: int(x.strip().split()[-1]), register.strip().split("\n"))
    )

    return apply_program(register)


def step_2(filename):
    with open(filename, "r") as f:
        instructions = list(
            map(int, f.read().split("\n\n")[1].split(": ")[1].split(","))
        )
    possible_A = [0]
    for i in range(16):
        new_possible_A = []
        for possible_A_value in possible_A:
            for j in range(8):

                result = apply_program([possible_A_value * 8 + j, 0, 0])
                if not result:
                    continue
                result = list(map(int, result.split(",")))
                if result == instructions[-1 - i :]:
                    new_possible_A.append(possible_A_value * 8 + j)
        possible_A = new_possible_A
    return min(possible_A)


print(step_1("2024/17_input.txt"))

print(step_2("2024/17_input.txt"))

