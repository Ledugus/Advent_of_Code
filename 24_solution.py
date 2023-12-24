import math


def get_all_hails_vectors(filename, coo: int):
    f = open(filename)
    return [tuple(map(lambda x: list(
            map(int, x.split(", ")))[:2], (line.strip().split(" @ ")))) for line in f.readlines()]


class Rational:
    def __init__(self, n: int, m: int = 1) -> None:
        self.n, self.m = self.get_reduced_form(n, m)

    @staticmethod
    def get_reduced_form(n: int, m: int):
        return n//math.gcd(n, m), m // math.gcd(n, m)

    def __eq__(self, __value: 'Rational') -> bool:
        return self.n == __value.n and self.m == __value.m

    def __repr__(self) -> str:
        return str(self.n) if self.m == 1 else str(self.n/self.m)


class Line:
    def __init__(self, a: int, b: int, c: int) -> None:
        """Forme ax + by + c = 0"""
        self.a = a
        self.b = b
        self.c = c
        try:
            self.m = -b/a
        except ZeroDivisionError:
            self.m = math.inf

    def get_intersection_point(self, other: 'Line'):
        if self.m == other.m:
            return self.c == other.c

        x = ((self.b*other.c - self.c*other.b) /
             (self.a * other.b - self.b * other.a))
        y = ((other.a*self.c-self.a*other.c) /
             (self.a*other.b-other.a*self.b))
        return (x, y)

    def __repr__(self) -> str:
        return f"Line {self.a}x + {self.b}y + {self.c} = 0"


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


print(step_1('24_test.txt'))
