import numpy as np
from utils import *


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_score_1(map, height, width, pos, value, arrival_pos):
    if value == 9:
        return pos
    for dir in DIRECTIONS:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if not in_bound(*new_pos, height, width):
            continue
        if map[new_pos] == value + 1:
            arrival_pos.add(
                get_score_1(map, height, width, new_pos, value + 1, arrival_pos)
            )
    if value == 0:
        return arrival_pos


def get_score_2(map, height, width, pos, value):
    if value == 9:
        return 1
    current_score = 0
    for dir in DIRECTIONS:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if not in_bound(*new_pos, height, width):
            continue
        if map[new_pos] == value + 1:
            current_score += get_score_2(map, height, width, new_pos, value + 1)
    return current_score


def step_1(filename):

    f = open(filename)
    trailheads = set()
    map = []
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == "0":
                trailheads.add((i, j))
            map_line.append(int(char))
        map.append(map_line)
    map = np.array(map)
    f.close()

    height = len(map)
    width = len(map[0])
    count = 0
    for trailhead in trailheads:
        count += len(get_score_1(map, height, width, trailhead, 0, set())) - 1
    return count


def step_2(filename):
    f = open(filename)
    trailheads = set()
    map = []
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == "0":
                trailheads.add((i, j))
            map_line.append(int(char))
        map.append(map_line)
    map = np.array(map)
    f.close()

    height = len(map)
    width = len(map[0])
    count = 0
    for trailhead in trailheads:
        count += get_score_2(map, height, width, trailhead, 0)
    return count


print(step_1("2024/10_test.txt"))
print(step_1("2024/10_input.txt"))

print(step_2("2024/10_test.txt"))
print(step_2("2024/10_input.txt"))
