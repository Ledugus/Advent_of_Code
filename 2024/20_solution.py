import numpy as np
from utils import *

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # East  # North  # West  # South


def run_dijkstra(map, grid_size, start):
    distances = {}
    current = start
    distances[current] = 0
    visited = set([])
    while set(distances.keys()) != visited:
        # check directions forward -> update distance
        for dir in DIRECTIONS:
            pos_forward = (current[0] + dir[0], current[1] + dir[1])
            if not in_bound(pos_forward[0], pos_forward[1], grid_size, grid_size):
                continue
            if (
                map[pos_forward] != "#"
                and distances.get(pos_forward, np.inf) > distances[current] + 1
            ):
                distances[pos_forward] = distances[current] + 1

        visited.add(current)
        candidates = [pos for pos in distances if pos not in visited]
        if candidates == []:
            continue
        current = min(
            candidates,
            key=lambda key_: distances.get(key_, np.inf),
        )
    return distances


def step_1(filename):

    min_shortcut_save = 100 if "input" in filename else 20
    f = open(filename)

    map = []
    to_visit = set([])
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char != "#":
                to_visit.add((i, j))
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)

    count = 0
    distances = run_dijkstra(map, len(map), end)
    for pos, distance_to_end in distances.items():
        for i, j in DIRECTIONS:
            cheat_distance_to_end = distances.get(
                (pos[0] + 2 * i, pos[1] + 2 * j), np.inf
            )
            if distance_to_end >= (min_shortcut_save + cheat_distance_to_end + 2) >= 0:
                count += 1

    f.close()
    return count


def step_2(filename):
    min_shortcut_save = 100 if "input" in filename else 70
    f = open(filename)

    map = []
    end = (0, 0)
    to_visit = set([])
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char != "#":
                to_visit.add((i, j))
            if char == "E":
                end = (i, j)
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)

    count = 0
    distances = run_dijkstra(map, len(map), end)
    accessible_pos = set(
        [
            (i, j)
            for i in range(-20, 21)
            for j in range(-20, 21)
            if 0 < abs(i) + abs(j) <= 20
        ]
    )
    for pos, distance_to_end in distances.items():
        if distance_to_end < min_shortcut_save:
            continue
        for i, j in accessible_pos:
            cheat_distance_to_end = distances.get((pos[0] + i, pos[1] + j), np.inf)
            if distance_to_end >= (
                min_shortcut_save + cheat_distance_to_end + (abs(i) + abs(j))
            ):
                count += 1

    f.close()
    return count


print(step_1("2024/20_test.txt"))
print(step_1("2024/20_input.txt"))

print(step_2("2024/20_test.txt"))
print(step_2("2024/20_input.txt"))
