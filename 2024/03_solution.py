import numpy as np


def step_1(filename):
    f = open(filename)

    text = f.read()
    sum = 0
    number1 = ""
    get_number1 = False
    number2 = ""
    get_number2 = False
    i = 0
    while i < len(text):

        char = text[i]
        if text[i : i + 4] == "mul(":
            get_number1 = True
            number1 = ""
            number2 = ""
            i += 4
            continue

        if get_number1 and char.isdigit():
            number1 += char
            i += 1
            continue
        if get_number1 and char == "," and number1 != "":
            get_number1 = False
            get_number2 = True
            i += 1
            continue
        if get_number2 and char.isdigit():
            number2 += char
            i += 1
            continue
        if get_number2 and char == ")" and number2 != "":
            sum += int(number1) * int(number2)
            get_number2 = False
            number1 = ""
            number2 = ""
            i += 1
            continue
        number1 = ""
        number2 = ""
        get_number2 = False
        get_number1 = False
        i += 1

    f.close()
    return sum


def step_2(filename):
    f = open(filename)

    text = f.read()
    sum = 0
    number1 = ""
    number2 = ""
    get_number1 = False
    get_number2 = False
    i = 0
    enable = True
    while i < len(text):
        char = text[i]
        if text[i : i + 4] == "do()":
            enable = True
            i += 4
            continue
        if text[i : i + 7] == "don't()":
            enable = False
            i += 7
            continue
        if text[i : i + 4] == "mul(":
            get_number1 = True
            i += 4
            continue

        if get_number1 and char.isdigit():
            number1 += char
            i += 1
            continue
        if get_number1 and char == "," and number1 != "":
            get_number1 = False
            get_number2 = True
            i += 1
            continue
        if get_number2 and char.isdigit():
            number2 += char
            i += 1
            continue
        if get_number2 and char == ")" and number2 != "":
            if enable:
                sum += int(number1) * int(number2)
            number1 = ""
            number2 = ""
            get_number2 = False
            i += 1
            continue
        number1 = ""
        number2 = ""
        get_number1 = False
        get_number2 = False
        i += 1

    f.close()
    return sum


print(step_1("2024/03_input.txt"))

print(step_2("2024/03_input.txt"))
