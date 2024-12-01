def descend(values):
    current_values = values
    list_of_results = [values]
    count = 0
    while any(current_values):
        current_values = [current_values[x+1]-current_values[x]
                          for x in range(len(current_values)-1)]
        list_of_results.append(current_values)
        count += 1
    return list_of_results


def extrapolate(list_diffs: list[list]):
    for index in range(len(list_diffs)-1):
        list_diffs[-2-index].append(list_diffs[-2-index]
                                    [-1]+list_diffs[-1-index][-1])
    return list_diffs[0][-1]


def extrapolate_2(list_diffs):
    total = 0
    for list in list_diffs[::-1]:
        total = list[0]-total
    return total


def step_1(filename):
    f = open(filename, "r")
    total = 0
    number = 1
    for line in f.readlines():
        values = list(map(int, line.strip().split()))

        list_diffs = descend(values)
        score = extrapolate_2(list_diffs)
        print(number, score)
        total += score
        number += 1
    return total


print(step_1("9_input.txt"))
