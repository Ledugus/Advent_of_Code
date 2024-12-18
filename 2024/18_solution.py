import numpy as np
from utils import *

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # East  # North  # West  # South


def run_dijkstra(wall_pos, grid_size):
    distances = {}
    current = (0, 0)  # (position, facing)
    distances[current] = 0
    visited = set([])
    end = (grid_size - 1, grid_size - 1)
    while end not in visited:
        # check directions forward -> update distance
        for dir in DIRECTIONS:
            pos_forward = (current[0] + dir[0], current[1] + dir[1])
            if not in_bound(pos_forward[0], pos_forward[1], grid_size, grid_size):
                continue
            if (
                pos_forward not in wall_pos
                and distances.get(pos_forward, np.inf) > distances[current] + 1
            ):
                distances[pos_forward] = distances[current] + 1

        visited.add(current)
        candidates = [pos for pos in distances if pos not in visited]
        if candidates == []:
            return end in visited
        current = min(
            candidates,
            key=lambda key_: distances.get(key_, np.inf),
        )
    return distances[end]


def step_1(filename):
    f = open(filename)
    wall_pos = set([])
    test = filename == "2024/18_test.txt"
    grid_size = 10 if test else 71
    line_length = 12 if test else 1024

    for line in f.readlines()[:line_length]:
        wall_pos.add(tuple(map(int, line.strip().split(","))))

    return run_dijkstra(wall_pos, grid_size)


def step_2(filename):
    f = open(filename)
    wall_pos = []
    test = filename == "2024/18_test.txt"
    grid_size = 7 if test else 71

    for line in f.readlines():
        wall_pos.append(tuple(map(int, line.strip().split(","))))

    min = 0
    max = len(wall_pos)
    mid = len(wall_pos) // 2
    while min < max:
        mid = (min + max) // 2
        result = run_dijkstra(wall_pos[:mid], grid_size)
        if result:
            min = mid + 1
        else:
            max = mid

    f.close()
    return str(wall_pos[min - 1][0]) + "," + str(wall_pos[min - 1][1])


print(step_1("2024/18_test.txt"))
print(step_1("2024/18_input.txt"))

print(step_2("2024/18_test.txt"))
print(step_2("2024/18_input.txt"))
