import numpy as np


def in_bound(i, j, height, width):
    return 0 <= i < height and 0 <= j < width


def count_xmas(i, j, matrix):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    count = 0
    for dir in dirs:
        l = [
            matrix[i + x * dir[0]][j + x * dir[1]]
            for x in range(1, 4)
            if in_bound(i + x * dir[0], j + x * dir[1], len(matrix), len(matrix[0]))
        ]

        if l == ["M", "A", "S"]:
            count += 1

    return count


def step_1(filename):
    f = open(filename)

    lines = []
    for line in f.readlines():
        lines.append(line.strip())

    count_x = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "X":
                count_x += count_xmas(i, j, lines)
    f.close()
    return count_x


def count_mas_mas(i, j, matrix):
    dirs = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
    count = 0

    l = [
        matrix[i + dir[0]][j + dir[1]]
        for dir in dirs
        if in_bound(i + dir[0], j + dir[1], len(matrix), len(matrix[0]))
    ]

    if len(l) == 4 and sorted(l[:2]) == ["M", "S"] and sorted(l[2:]) == ["M", "S"]:
        count += 1

    return count


def step_2(filename):
    f = open(filename)

    lines = []
    for line in f.readlines():
        lines.append(line.strip())

    count_x = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "A":
                count_x += count_mas_mas(i, j, lines)
    f.close()
    return count_x


print(step_1("2024/04_input.txt"))

print(step_2("2024/04_input.txt"))
