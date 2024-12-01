class Brick():
    def __init__(self, id: int, coo1: tuple[int, ...], coo2: tuple[int, ...]) -> None:
        self.id = id
        self.falling = True
        self.height = abs(coo1[2]-coo2[2])+1
        self.shadow = self.get_shadow(coo1, coo2)
        self.layer = min(coo1[2], coo2[2])

    def get_shadow(self, coo1: tuple[int, ...], coo2: tuple[int, ...]) -> list:
        if self.height != 1:
            print(self.id, (coo1[0], coo1[1]))
            return [((coo1[0], coo1[1]), self.id)]
        begin_coo = min(coo1, coo2)
        end_coo = max(coo1, coo2)
        shadow = []
        for x in range(begin_coo[0], end_coo[0]+1):
            for y in range(begin_coo[1], end_coo[1]+1):
                shadow.append(((x, y), self.id))

        return shadow

    def get_coo_shadow(self):
        return [i[0] for i in self.shadow]

    def __str__(self) -> str:
        stability = "falling" if self.falling else "stable"
        return f"Brick at {self.layer} layer {self.shadow} : {stability}"

    def __repr__(self) -> str:
        return self.__str__()


def get_all_bricks(filename) -> list[Brick]:
    f = open(filename)
    bricks = []
    for i, line in enumerate(f.readlines()):
        coo1, coo2 = line.strip().split("~")
        coo1 = tuple([int(coo) for coo in coo1.split(",")])
        coo2 = tuple([int(coo) for coo in coo2.split(",")])
        bricks.append(Brick(i, coo1, coo2))
    return bricks


def get_new_layer(brick: Brick, layer_dict: dict[int, list[tuple[int, int]]]):
    occupied_layers = sorted(
        (i for i in layer_dict.keys() if i <= brick.layer), reverse=True)
    intersections = []
    shadow_coos = brick.get_coo_shadow()
    for layer in occupied_layers:
        intersects = False
        for cube in layer_dict[layer]:
            coo, brick_id = cube
            if coo in shadow_coos:
                intersects = True
                intersections.append(brick_id)

        if intersects:
            return layer + 1, list(set(intersections))
    return 1, []


def add_brick_to_layer(brick: Brick, bottom_layer, stable_layer_dict: dict[int, list[tuple[int, int]]]):
    for layer in range(bottom_layer, bottom_layer+brick.height):
        # print(f"Adding {brick.id} to layer {layer}")
        current_layer = stable_layer_dict.get(layer, [])
        current_layer.extend(brick.shadow)
        stable_layer_dict[layer] = current_layer
    return stable_layer_dict


def get_rest_on_dict(list_bricks: list[Brick]):
    layer_dict = {}
    rest_on_dict = {}
    for current_brick in list_bricks:
        layer, list_rest_on = get_new_layer(current_brick, layer_dict)
        layer_dict = add_brick_to_layer(current_brick, layer, layer_dict)
        rest_on_dict[current_brick.id] = list_rest_on
    return rest_on_dict


def step_1(filename):
    bricks = sorted(get_all_bricks(filename), key=lambda x: x.layer)
    rest_on_dict = get_rest_on_dict(bricks)
    count = 0
    for x in range(len(bricks)):
        if [x] not in rest_on_dict.values():
            count += 1
    return count


def falling_chain(rest_on_dict: dict[int, list[int]], brick_id: int):
    fallable_dict = {}
    for id, rest_on_list in rest_on_dict.items():
        if len(rest_on_list) == 1:
            x = rest_on_list[0]
            falling_from_x = fallable_dict.get(x, [])
            falling_from_x.append(id)
            fallable_dict[x] = falling_from_x

    falling = fallable_dict[brick_id]
    count = 1
    while falling:
        print("Currently falling bricks", falling)
        next_falling = []
        for falling_brick in falling:
            caused_falling = fallable_dict.get(falling_brick, [])
            print(caused_falling)
            next_falling.extend(caused_falling)
            count += len(caused_falling)
        falling = next_falling
    return count


def step_2(filename):
    bricks = sorted(get_all_bricks(filename), key=lambda x: x.layer)
    rest_on_dict = get_rest_on_dict(bricks)
    count = 0
    for x in range(len(bricks)):
        if [x] in rest_on_dict.values():
            print("Currently trying brick", x)
            count += falling_chain(rest_on_dict, x)
    return count


print(step_2('22_test.txt'))
