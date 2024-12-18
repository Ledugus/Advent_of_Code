import numpy as np
from time import time
from utils import *

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # East  # North  # West  # South


def step_1(filename):
    f = open(filename)
    map = []
    end = start = (0, 0)
    free_space = 0
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == ".":
                free_space += 1
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)
    print(map)
    f.close()

    # implement dijkstra
    distances = {}
    current = (start, 0)  # (position, facing)
    distances[current] = 0
    visited = set([])
    while end not in visited:
        position, facing = current
        # check directions forward -> update distance
        dir_forward = DIRECTIONS[facing]
        pos_forward = (position[0] + dir_forward[0], position[1] + dir_forward[1])
        if (
            map[pos_forward] != "#"
            and distances.get((pos_forward, facing), np.inf) > distances[current] + 1
        ):
            distances[(pos_forward, facing)] = distances[current] + 1

        # check directions left-right-> update distance

        for facing_side in [-1, 1]:
            facing_left = (facing + facing_side) % 4
            dir_left = DIRECTIONS[facing_left]
            pos_left = (position[0] + dir_left[0], position[1] + dir_left[1])
            if (
                map[pos_left] != "#"
                and distances.get((pos_left, facing_left), np.inf)
                > distances[current] + 1001
            ):
                distances[(pos_left, facing_left)] = distances[current] + 1001

        # set current as visited
        visited.add(current)
        if current[0] == end:
            break
        # set current as min distance not visited
        current = min(
            [key_ for key_ in distances if key_ not in visited],
            key=lambda key_: distances.get(key_, np.inf),
        )
    min_dist = min([distances.get((end, dir), np.inf) for dir in range(4)])
    return min_dist


def step_2(filename):
    f = open(filename)
    map = []
    end = start = (0, 0)
    free_space = 0
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == ".":
                free_space += 1
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)
    f.close()

    # implement dijkstra
    distances = {}
    current = (start, 0)  # (position, facing)
    distances[current] = 0
    previous = {current: []}
    visited = set([])
    t = time()
    while end not in visited:
        position, facing = current
        # check directions forward -> update distance
        dir_forward = DIRECTIONS[facing]
        pos_forward = (position[0] + dir_forward[0], position[1] + dir_forward[1])

        if (
            map[pos_forward] != "#"
            and distances.get((pos_forward, facing), np.inf) > distances[current] + 1
        ):
            distances[(pos_forward, facing)] = distances[current] + 1
            previous[(pos_forward, facing)] = [current]
        elif (
            map[pos_forward] != "#"
            and distances.get((pos_forward, facing), np.inf) == distances[current] + 1
        ):
            l = previous.get((pos_forward, facing), [])
            l.append(current)
            previous[(pos_forward, facing)] = l

        # check directions left-right-> update distance

        for facing_side in [-1, 1]:
            facing_left = (facing + facing_side) % 4
            dir_left = DIRECTIONS[facing_left]
            pos_left = (position[0] + dir_left[0], position[1] + dir_left[1])
            if (
                map[pos_left] != "#"
                and distances.get((pos_left, facing_left), np.inf)
                > distances[current] + 1001
            ):
                distances[(pos_left, facing_left)] = distances[current] + 1001
                previous[(pos_left, facing_left)] = [current]
            elif (
                map[pos_left] != "#"
                and distances.get((pos_left, facing_left), np.inf)
                == distances[current] + 1001
            ):
                l = previous.get((pos_left, facing_left), [])
                l.append(current)
                previous[(pos_left, facing_left)] = l

        # set current as visited
        visited.add(current)
        if current[0] == end:
            break
        # set current as min distance not visited
        current = min(
            [key_ for key_ in distances if key_ not in visited],
            key=lambda key_: distances.get(key_, np.inf),
        )
    opti_paths = set()
    to_visit = [(end, dir) for dir in range(4)]
    while to_visit:
        current = to_visit.pop()
        value = previous.get(current, [])
        for v in value:
            opti_paths.add(v[0])
            to_visit.append(v)
    return len(opti_paths) + 1


print(step_1("2024/16_test.txt"))
print(step_1("2024/16_input.txt"))

print(step_2("2024/16_test.txt"))
print(step_2("2024/16_input.txt"))
