AXES = ["x", "y", "z"]


class Coo:
    def __init__(self, coo: list[int]) -> None:
        self.coo = coo

    def __eq__(self, __value: 'Coo') -> bool:
        return self.coo == __value.coo

    def __lt__(self, __value: 'Coo') -> bool:
        for x in range(3):
            if self.coo[x] < __value.coo[x]:
                return True
        return False

    def __gt__(self, __value: 'Coo') -> bool:
        for x in range(3):
            if self.coo[x] > __value.coo[x]:
                return True
        return False

    def __str__(self) -> str:
        return f"({','.join([str(comp) for comp in self.coo])})"

    def __repr__(self) -> str:
        return self.__str__()


class Brick():
    def __init__(self, coo1: Coo, coo2: Coo) -> None:
        self.falling = True
        self.begin_coo = min(coo1, coo2)
        self.layer = self.begin_coo.coo[2]
        self.axe = [x for x in range(3) if coo1.coo[x] != coo2.coo[x]][0]
        self.length = abs(coo1.coo[self.axe]-coo2.coo[self.axe])+1
        self.rest_on = []
    def get_cubes(self):
        pass
    def intersects(self, other: 'Brick'):
        pass

    def __str__(self) -> str:
        stability = "falling" if self.falling else "stable"
        return f"Brick at {self.begin_coo} to len {self.length} ({AXES[self.axe]}) : {stability}"

    def __repr__(self) -> str:
        return self.__str__()


def get_all_bricks(filename) -> list[Brick]:
    f = open(filename)
    bricks = []
    for line in f.readlines():
        coo1, coo2 = line.strip().split("~")
        coo1 = Coo([int(coo) for coo in coo1.split(",")])

        coo2 = Coo([int(coo) for coo in coo2.split(",")])
        bricks.append(Brick(coo1, coo2))
    return bricks


def step_1_old(filename):
    bricks = get_all_bricks(filename)
    nb_bricks = len(bricks)
    stable_layer_dict = {}
    rest_on_dict = {}
    while len(stable) != nb_bricks:
        for current_brick in sorted([brick for brick in bricks if brick.falling], key=lambda x: x.layer):
            while True:
                if current_brick.layer == 1:
                    stable
                intersection_list = []
                for stable_brick in stable:
                    if current_brick.intersects(stable_brick):
                        intersection_list.append(stable_brick)
        break


def step_1(filename):
    bricks = sorted(get_all_bricks(filename), key=lambda x: x.layer)

    print(bricks)
    for brick in bricks:

    nb_bricks = len(bricks)
    stable = []


print(step_1('22_test.txt'))
