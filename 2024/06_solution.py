from types import new_class
import numpy as np
from utils import *


def get_new_pos(guard_pos, dir, map, height, width):
    """Trouver la position suivante du garde, sachant sa position, direction et la carte"""

    new_dir = dir
    new_guard_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])
    if in_bound(*new_guard_pos, height, width):
        if map[*new_guard_pos] == "#":
            new_dir = (dir[1], -1 * dir[0])
            new_guard_pos = (guard_pos[0] + new_dir[0], guard_pos[1] + new_dir[1])
            if not in_bound(*new_guard_pos, height, width):
                return False
    # si la prochaine direction est hors de la grille, arrêter
    else:
        return False
    return new_guard_pos, new_dir


def step_1(filename):
    f = open(filename)

    guard_pos = (0, 0)
    dir = [-1, 0]
    map = []
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == "^":
                guard_pos = (i, j)
                map_line.append(".")
                continue
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)
    f.close()
    height = len(map)
    width = len(map[0])
    count = 0
    steps = 0
    path_matrix = np.array([[False for i in range(width)] for _ in range(height)])
    while True:
        if not path_matrix[guard_pos]:
            path_matrix[guard_pos] = True
            count += 1

        result = get_new_pos(guard_pos, dir, map, height, width)
        if not result:
            break
        guard_pos, dir = result

        steps += 1
    return count


def step_2(filename):
    f = open(filename)
    # get matrix from file
    # get guard position
    map = []
    guard_pos = (0, 0)
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == "^":
                guard_pos = (i, j)
                map_line.append(".")
                continue
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)
    f.close()

    dir = (-1, 0)
    height = len(map)
    width = len(map[0])
    count = 0
    # get path
    path_dict = {guard_pos: set([])}
    running = True
    new_guard_pos = (0, 0)
    while running:
        result = get_new_pos(guard_pos, dir, map, height, width)
        if not result:
            running = False
        else:
            new_guard_pos, dir = result

        # mettre à jour le chemin
        current_node = path_dict.get(guard_pos, False)
        if current_node != False:
            current_node.add(new_guard_pos)
        else:
            path_dict[guard_pos] = set([new_guard_pos])

        # passer à la prochaine position
        guard_pos = new_guard_pos

    # passer en revue le chemin
    # pour chaque élément, partir à droite (-> changer de dir) !! intersections !!
    # suivre la route, tester si on retombe sur une partie du chemin.
    # Si oui -> count += 1
    step = 0
    for depart_pos, next_positions in path_dict.items():
        print()

        if next_positions == set([depart_pos]):
            print("i break because == set")
            continue
        for next_pos in next_positions:
            print()
            print(depart_pos, next_pos, dir, " Chemin suivi ")
            dir = (next_pos[0] - depart_pos[0], next_pos[1] - depart_pos[1])
            dir = (dir[1], -1 * dir[0])
            # faire le trajet à partir de depart_pos jusqu'à sortir ou retomber sur depart_pos
            new_guard_pos = (depart_pos[0] + dir[0], depart_pos[1] + dir[1])
            if not in_bound(*new_guard_pos, height, width):
                break
            running = True
            while new_guard_pos != depart_pos and running:
                print(new_guard_pos, dir)

                # passer à la prochaine position
                result = get_new_pos(guard_pos, dir, map, height, width)
                if not result:
                    running = False
                else:
                    new_guard_pos, dir = result

                guard_pos = new_guard_pos
            if new_guard_pos == depart_pos:
                count += 1

            step += 1
    return count


print(step_1("2024/06_test.txt"))
print(step_1("2024/06_input.txt"))

print(step_2("2024/06_test.txt"))
# print(step_2("2024/06_input.txt"))
