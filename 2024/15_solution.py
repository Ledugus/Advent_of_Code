import numpy as np
from utils import *

DIRECTIONS = {
    "^": Position(-1, 0),
    "v": Position(1, 0),
    "<": Position(0, -1),
    ">": Position(0, 1),
}


def step_1(filename):
    with open(filename, "r") as f:
        content = f.read()
    map_lines, moves = list(map(lambda x: x.strip().split("\n"), content.split("\n\n")))
    map_2d = []

    robot_pos = Position(0, 0)
    for i, line in enumerate(map_lines):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == "@":
                robot_pos = Position(i, j)
            map_line.append(char)
        map_2d.append(map_line)
    map_2d = np.array(map_2d)
    moves = "".join(moves)

    for move in moves:
        dir = DIRECTIONS[move]
        pushing_obj = []
        pos = robot_pos + dir
        char = map_2d[pos.tuple]
        while char != "#":
            if char == ".":
                for obj_pos in pushing_obj:
                    map_2d[(obj_pos + dir).tuple] = "O"
                map_2d[(robot_pos).tuple] = "."
                robot_pos += dir
                map_2d[(robot_pos).tuple] = "@"
                break
            if char == "O":
                pushing_obj.append(pos)
                pos += dir
                char = map_2d[pos.tuple]

    count = 0
    for i in range(len(map_2d)):
        for j in range(len(map_2d[0])):
            if map_2d[i, j] == "O":
                count += 100 * i + j

    return count


def step_2(filename):
    with open(filename, "r") as f:
        content = f.read()
    map_lines, moves = list(map(lambda x: x.strip().split("\n"), content.split("\n\n")))
    map_2d = []

    robot_pos = Position(0, 0)
    for i, line in enumerate(map_lines):
        map_line = []
        for j, char in enumerate(line.strip()):
            if char == "@":
                robot_pos = Position(i, 2 * j)
                map_line.append("@")
                map_line.append(".")
            elif char == "O":
                map_line.append("[")
                map_line.append("]")
            elif char == ".":
                map_line.append(".")
                map_line.append(".")
            elif char == "#":
                map_line.append("#")
                map_line.append("#")

        map_2d.append(map_line)
    map_2d = np.array(map_2d)
    moves = "".join(moves)
    print_matrix(map_2d)

    for move in moves:
        if move in ["^", "v", "<"]:
            continue
        print("Making move", move)
        dir = DIRECTIONS[move]
        pushing_obj = []
        print(dir)
        pos = robot_pos + dir
        char = map_2d[pos.tuple]
        while char != "#":
            print("Following char : ", char)
            print(dir)
            print_matrix(map_2d)
            if char == ".":
                for obj_pos in pushing_obj[::-1]:
                    map_2d[(obj_pos + dir).tuple] = map_2d[obj_pos.tuple]
                map_2d[(robot_pos).tuple] = "."
                robot_pos += dir
                map_2d[(robot_pos).tuple] = "@"
                break
            elif char == "[":

                pushing_obj.append(pos)
                pushing_obj.append(pos + dir)
                pos += dir + dir
                char = map_2d[pos.tuple]

    count = 0
    for i in range(len(map_2d)):
        for j in range(len(map_2d[0])):
            if map_2d[i, j] == "O":
                count += 100 * i + j

    return count


# print(step_1("2024/15_test.txt"))
# print(step_1("2024/15_input.txt"))

print(step_2("2024/15_test.txt"))
# print(step_2("2024/15_input.txt"))
