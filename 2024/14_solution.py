import numpy as np
from matplotlib import pyplot as plt
from utils import *


def get_quadrant(pos, width, height):
    left, down = pos
    if left < width // 2:
        if down < height // 2:
            return 0
        elif down >= height // 2 + 1:
            return 1
    elif left >= width // 2 + 1:
        if down < height // 2:
            return 2
        elif down >= height // 2 + 1:
            return 3
    return 4


def step_1(filename, width=101, height=103):
    f = open(filename)

    quadrant = np.zeros(5)
    for line in f.readlines():
        pos, v = map(lambda x: x.split("=")[1], line.strip().split(" "))
        pos = np.array(list(map(int, pos.split(","))))
        v = np.array(list(map(int, v.split(","))))
        pos = pos + v * 100
        pos = pos[0] % width, pos[1] % height
        quadrant[get_quadrant(pos, width, height)] += 1
    f.close()
    return np.prod(quadrant[:-1])


def robot_density(robot_pos, width, height):
    density = 0
    for pos in robot_pos:
        if in_bound(pos[0] - width // 4, pos[1] - height // 4, width // 2, height // 2):
            density += 1
    return density / len(robot_pos)


def step_2(filename):
    f = open(filename)
    width, height = 101, 103

    robot_pos = np.zeros((500, 2), dtype=int)
    vs = np.zeros((500, 2), dtype=int)

    for i, line in enumerate(f.readlines()):
        pos, v = map(lambda x: x.split("=")[1], line.strip().split(" "))
        robot_pos[i] = np.array(list(map(int, pos.split(","))))
        vs[i] = np.array(list(map(int, v.split(","))))
    f.close()

    step = 7412
    for i in range(len(robot_pos)):
        robot_pos[i] = robot_pos[i] + vs[i] * 7412
        robot_pos[i][0] = robot_pos[i][0] % width
        robot_pos[i][1] = robot_pos[i][1] % height

    density = robot_density(robot_pos, width, height)
    if density > 0.30:
        plt.clf()
        plt.title(f"Step {step}")
        plt.plot(robot_pos[:, 0], robot_pos[:, 1], "ro")
        plt.show()
    print(step, density)
    return 7412


print(step_1("2024/14_test.txt", width=11, height=7))
print(step_1("2024/14_input.txt"))

print(step_2("2024/14_input.txt"))
