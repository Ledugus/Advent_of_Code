import math
import numpy as np


def get_all_hails_vectors(filename, coo: int):
    f = open(filename, "r")
    return [tuple(map(lambda x: list(
            map(int, x.split(", ")))[:coo], (line.strip().split(" @ ")))) for line in f.readlines()]


def are_colinear(v1, v2):
    return abs(v1[0]/v2[0] - v1[1]/v2[1]) < (10**(-10))


class Line:
    def __init__(self, origin: tuple, dir: tuple) -> None:
        """Forme ax + by + c = 0"""
        self.origin = np.array(origin)
        self.dir = np.array(dir)

    def get_intersection_point(self, other: 'Line'):

        A = np.matrix([-self.dir, other.dir]).transpose()
        det_A = (other.dir[0]*self.dir[1]-self.dir[0]*other.dir[1])
        if det_A == 0:
            return are_colinear(self.origin-other.origin, self.dir)

        return np.dot(np.linalg.inv(A), (self.origin-other.origin).transpose())

    def __repr__(self) -> str:
        return f"Line from {self.origin} longs {self.dir} direction"


def intersect_in_boundary(min: int, max: int, line1: Line, line2: Line):
    point = line1.get_intersection_point(line2)
    if type(point) == np.bool_:
        return point
    t, s = point[0, 0], point[0, 1]
    if t > 0 and s > 0:
        intersection_point = line1.origin + t*line1.dir
        return min <= intersection_point[0] <= max and min <= intersection_point[1] <= max
    return False


def hails_states_to_line(b, v):
    """b: vecteur de base, v: vecteur vitesse
    """
    return Line(b, v)


def step_1(filename):
    hails_states = get_all_hails_vectors(filename, 2)
    lines = [hails_states_to_line(coo, vel) for coo, vel in hails_states]
    print(lines)
    count = 0
    for x in range(len(lines)):
        for y in range(x+1, len(lines)):
            if intersect_in_boundary(200000000000000, 400000000000000, lines[x], lines[y]):
                print(f"Lines {x} and {y} intersect")
                count += 1
            else:
                print(f"Lines {x} and {y} DO NOT intersect")
    return count


def step_2(filename):
    hails_states = get_all_hails_vectors(filename, 3)
    lines = [hails_states_to_line(coo, vel) for coo, vel in hails_states]
    print(lines)


print(step_2('24_test.txt'))
