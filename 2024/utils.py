from re import X
import numpy as np


def in_bound(i, j, height, width):
    return 0 <= i < height and 0 <= j < width


def print_matrix(matrix, delimiter="", special_pos=[]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) in special_pos:
                print("O", end=delimiter)
            else:
                print(str(matrix[i][j]), end=delimiter)
        print()
    print("\n")


def get_matrix_from(filename):
    f = open(filename)
    map = []
    for i, line in enumerate(f.readlines()):
        map_line = []
        for j, char in enumerate(line.strip()):
            map_line.append(char)
        map.append(map_line)
    map = np.array(map)
    f.close()
    return map


class Position:
    """Represents a position on a 2D array"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.tuple = (x, y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __mul__(self, a: int):
        if isinstance(a, int):
            return Position(self.x * a, self.y * a)
        raise Exception(f"Tried mul a {type(other)} to a Position object")

    def __add__(self, other) -> "Position":
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        raise Exception(f"Tried adding a {type(other)} to a Position object")


class Node:
    def __init__(self, value=None, children=[]) -> None:
        self.value = value
        self.children = children

    def __str__(self) -> str:
        return f"Node({self.value}, {self.children})"

    def __repr__(self) -> str:
        return self.__str__()


class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes

    def __str__(self) -> str:
        return f"Graph({len(self.nodes)} nodes)"
