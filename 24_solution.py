import math
import numpy as np


def get_all_hails_vectors(filename, coo: int):
    f = open(filename)
    return [tuple(map(lambda x: list(
            map(int, x.split(", ")))[:2], (line.strip().split(" @ ")))) for line in f.readlines()]


def are_colinear(v1, v2):
    return abs(v1[0]/v2[0] - v1[1]/v2[1]) < (10**(-10))


class Line:
    def __init__(self, origin: tuple, dir: tuple) -> None:
        """Forme ax + by + c = 0"""
        self.origin = np.array(origin)
        self.dir = np.array(dir)

    def get_intersection_point(self, other: 'Line'):
        if are_colinear(self.dir, other.dir):

            return are_colinear(self.origin-other.origin, self.dir)
        return

    def __repr__(self) -> str:
        return f"Line from {self.origin} longs {self.dir} direction"


def intersect_in_boundary(min: int, max: int, line1: Line, line2: Line):
    point = line1.get_intersection_point(line2)
    if type(point) == bool:
        return point

    return min <= point[0] <= max and min <= point[1] <= max


def hails_states_to_line(b, v):
    """b: vecteur de base, v: vecteur vitesse
    """
    return Line(v[1], -v[0], -v[1]*b[0]+v[0]*b[1])


def step_1(filename):
    hails_states = get_all_hails_vectors(filename, 2)
    lines = [hails_states_to_line(coo, vel) for coo, vel in hails_states]
    print(lines)
    count = 0
    for x in range(len(lines)):
        for y in range(x+1, len(lines)):
            if intersect_in_boundary(7, 27, lines[x], lines[y]):
                print(f"Lines {x} and {y} intersect")
                count += 1
            else:
                print(f"Lines {x} and {y} DO NOT intersect")
    print(count)
    return hails_states


l1 = Line()
print()
print(step_1('24_test.txt'))
