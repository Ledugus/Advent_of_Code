LIST_OF_MAPPINGS = []


def map_seed(seed):
    for mapping in LIST_OF_MAPPINGS:
        if seed in range(mapping[1], mapping[1]+mapping[2]):
            return mapping[0] + seed-mapping[1]
    return seed


def step_1(filename):
    global LIST_OF_MAPPINGS
    f = open(filename)
    seeds = list(map(int, f.readline().split(": ")[1].split()))
    for line in f.readlines():
        line = line.strip().split()
        if line and line[0].isdigit():
            LIST_OF_MAPPINGS.append(tuple(map(int, line)))
        else:
            seeds = list(map(map_seed, seeds))
            LIST_OF_MAPPINGS = []
    seeds = list(map(map_seed, seeds))
    return min(seeds)


def step_2(filename):
    global LIST_OF_MAPPINGS
    f = open(filename)
    seeds = list(map(int, f.readline().split(": ")[1].split()))
    for line in f.readlines():
        line = line.strip().split()
        if line and line[0].isdigit():
            LIST_OF_MAPPINGS.append(tuple(map(int, line)))
        else:
            seeds = list(map(map_seed, seeds))
            LIST_OF_MAPPINGS = []
    seeds = list(map(map_seed, seeds))
    return min(seeds)


print(step_1("5_input.txt"))
