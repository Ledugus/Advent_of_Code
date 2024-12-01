import numpy as np


def get_score(numbers, winning):
    count_right_numbers = 0
    for number in numbers:
        if number in winning:
            count_right_numbers += 1
    if count_right_numbers != 0:
        return 2 ** (count_right_numbers - 1)
    return 0


def step_1(filename):
    total_win = 0
    for line in open(filename):

        data = line.split(": ")[1].split(" | ")
        winning = list(map(int, data[0].split()))
        numbers = list(map(int, data[1].split()))
        total_win += get_score(numbers, winning)
    return total_win


def step_2(filename):

    list_scratchcards = [1] * len(open(filename).readlines())
    print(list_scratchcards)
    for line_index, line in enumerate(open(filename)):
        data = line.split(": ")[1].split(" | ")
        winning = list(map(int, data[0].split()))
        numbers = list(map(int, data[1].split()))
        score = 0
        for number in numbers:
            if number in winning:
                score += 1

        print(f"score_of_line {line_index} is {score}")
        for rel_index in range(1, score + 1):
            try:
                list_scratchcards[line_index +
                                  rel_index] += list_scratchcards[line_index]
            except:
                print("index out of range", line_index,
                      score, line_index+rel_index)
    return sum(list_scratchcards)


print(step_2("4_input.txt"))
