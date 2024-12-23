import numpy as np
from utils import *

KEYBOARD_FINAL = {
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "gap": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}
KEYBOARD = {
    "gap": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def get_min_instructions(code_string, keyboard):
    # Convert string to type to list of coordinates, beginning at A in keyboard
    code_string = "A" + code_string
    coordinates = list(map(lambda x: keyboard[x], code_string))
    # For all pos interval
    instructions = ""
    for i in range(len(coordinates) - 1):
        delta = (
            coordinates[i + 1][0] - coordinates[i][0],
            coordinates[i + 1][1] - coordinates[i][1],
        )
        move = ""
        up = -delta[0] if delta[0] < 0 else 0
        down = delta[0] if delta[0] > 0 else 0
        left = -delta[1] if delta[1] < 0 else 0
        right = delta[1] if delta[1] > 0 else 0

        # if i'm on the same line as the gap and my destination is up or down the gap
        if (
            coordinates[i][0] == keyboard["gap"][0]
            and coordinates[i + 1][1] == keyboard["gap"][1]
        ):
            # i must first go up or down
            move += "^" * up
            move += "v" * down
            # then left or right
            move += "<" * left
            move += ">" * right

        # else, i can go left as much as i want to begin
        else:
            move += "<" * left
            if up > 0:
                move += ">" * right
                move += "^" * up
            else:
                move += "v" * down
                move += ">" * right

        # Add a move to push the button "A"
        instructions += move + "A"

    return instructions


def step_1(filename):
    with open(filename) as f:
        codes = f.read().strip().split("\n")

    count = 0
    for code in codes:
        instructions = get_min_instructions(code, KEYBOARD_FINAL)
        new_instructions = get_min_instructions(instructions, KEYBOARD)
        last_instructions = get_min_instructions(new_instructions, KEYBOARD)
        code_number = int(code[:-1])
        count += code_number * len(last_instructions)

    f.close()
    return count


def step_2(filename):
    f = open(filename)

    count = 0

    f.close()
    return count


print(step_1("2024/21_test.txt"))
print(step_1("2024/21_input.txt"))

# print(step_2("2024/21_test.txt"))
# print(step_2("2024/21_input.txt"))

