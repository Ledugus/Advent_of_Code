import numpy as np
from utils import *


def get_region(map, seen, i, j, area, region, perimeter, color):
    if not in_bound(i, j, len(map), len(map[0])) or map[(i, j)] != color:
        return seen, area, perimeter + 1, region
    if seen[(i, j)]:
        return seen, area, perimeter, region
    if map[(i, j)] == color:
        seen[(i, j)] = True
        area += 1
        region.add((i, j))
        seen, area, perimeter, region = get_region(
            map, seen, i + 1, j, area, region, perimeter, color
        )
        seen, area, perimeter, region = get_region(
            map, seen, i - 1, j, area, region, perimeter, color
        )
        seen, area, perimeter, region = get_region(
            map, seen, i, j + 1, area, region, perimeter, color
        )
        seen, area, perimeter, region = get_region(
            map, seen, i, j - 1, area, region, perimeter, color
        )
    return seen, area, perimeter, region


# LIST OF SQUARES
SQUARES = [
    ((0, 1), (1, 0), (1, 1)),
    ((0, -1), (1, 0), (1, -1)),
    ((0, -1), (-1, 0), (-1, -1)),
    ((0, 1), (-1, 0), (-1, 1)),
]


def count_sides(region):
    """This function actually counts corners, not sides, but it's the same thing"""
    sides = 0
    for pos in region:
        i, j = pos
        for square in SQUARES:
            nb_cases = np.count_nonzero([(i + x, j + y) in region for x, y in square])
            if nb_cases % 2 == 0:
                sides += 1 / (nb_cases + 1)
            # prendre en compte les régions qui s'auto-ferment par un coin
            x, y = square[-1]
            if nb_cases == 1 and (i + x, j + y) in region:
                sides += 1
    return np.round(sides)


def step_1(filename):
    f = open(filename)
    map = []
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)
    f.close()

    count = 0
    seen = np.zeros_like(map, dtype=bool)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if not seen[(i, j)]:
                seen, area, perimeter, region = get_region(
                    map, seen, i, j, 0, set(), 0, map[i, j]
                )
                count += area * perimeter
    return count


def step_2(filename):
    f = open(filename)
    map = []
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)
    f.close()

    count = 0
    seen = np.zeros_like(map, dtype=bool)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if not seen[(i, j)]:
                seen, area, perimeter, region = get_region(
                    map, seen, i, j, 0, set(), 0, map[i, j]
                )
                count += area * count_sides(region)
    return count


print(step_1("2024/12_test.txt"))
print(step_1("2024/12_input.txt"))

print(step_2("2024/12_test.txt"))
print(step_2("2024/12_input.txt"))
