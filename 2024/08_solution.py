import numpy as np
from utils import *


def step_1(filename):

    f = open(filename)
    antennas = {}
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line.strip()):
            if char == ".":
                continue
            if char in antennas:
                antennas[char].add((i, j))
            else:
                antennas[char] = {(i, j)}
    height, width = i + 1, j + 1
    antinodes = set([])
    for antenna_pos in antennas.values():

        for i, pos in enumerate(antenna_pos):
            for j, other_pos in enumerate(antenna_pos):
                if i == j:
                    continue
                new_pos = (2 * pos[0] - other_pos[0], 2 * pos[1] - other_pos[1])
                if in_bound(*new_pos, height, width):
                    antinodes.add(new_pos)

    f.close()

    return len(antinodes)


def step_2(filename):
    f = open(filename)
    antennas = {}
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line.strip()):
            if char == ".":
                continue
            if char in antennas:
                antennas[char].add((i, j))
            else:
                antennas[char] = {(i, j)}
    height, width = i + 1, j + 1
    antinodes = set([])

    for antenna_pos in antennas.values():
        if len(antenna_pos) > 1:
            for i in antenna_pos:
                antinodes.add(i)
        for i, pos in enumerate(antenna_pos):
            for j, other_pos in enumerate(antenna_pos):
                if i == j:
                    continue
                dir = (pos[0] - other_pos[0], pos[1] - other_pos[1])
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                while in_bound(*new_pos, height, width):
                    antinodes.add(new_pos)
                    new_pos = (new_pos[0] + dir[0], new_pos[1] + dir[1])

    f.close()

    return len(antinodes)


print(step_1("2024/08_test.txt"))
print(step_1("2024/08_input.txt"))

print(step_2("2024/08_test.txt"))
print(step_2("2024/08_input.txt"))
