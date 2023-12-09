def get_map(lines):
    maps = {}
    for line in lines:
        name = line.strip().split(" = ")[0]
        values = line.strip().split(" = ")[1].strip("()").split(", ")
        maps[name] = values
    return maps


def step_1(filename):
    f = open(filename)
    directions = f.readline()
    f.readline()
    maps = get_map(f.readlines())
    count = 0
    current = "AAA"
    while True:
        if current == "ZZZ":
            return count
        if directions[count % (len(directions)-1)] == "L":
            current = maps[current][0]
        else:
            current = maps[current][1]
        count += 1


def get_cycle(maps, node, directions, state):
    cycle = [(node, directions[state])]
    current = maps[node][directions[state]]
    while (current, directions[state]) not in cycle:

        cycle.append((current, directions[state]))
        state = (state+1) % len(directions)
        current = maps[current][directions[state]]
    contains_endpoint = False
    for state in cycle:
        if state[0][2] == "Z":
            contains_endpoint = True
    print(cycle.index((current, directions[state])))
    precycle = cycle[cycle.index((current, directions[state])):]
    cycle = cycle[cycle.index((current, directions[state])):]
    return len(cycle), len(precycle), contains_endpoint


def all_end_z(current):
    for value in current:
        if value[2] != 'Z':
            return False
    return True


def step_2(filename):
    f = open(filename)
    directions = [0 if char == "L" else 1 for char in f.readline().strip()]
    f.readline()
    maps = get_map(f.readlines())
    currents = [key for key in maps.keys() if key[2] == "A"]
    for current in currents:
        print(len(get_cycle(maps, current, directions, 0)))
    count = 0

    while count < 100 and not all_end_z(currents):
        state = count % (len(directions))
        currents = [maps[current][directions[state]] for current in currents]
        count += 1
        finish_with_Z = [current for current in currents if current[2] == "Z"]
        if finish_with_Z:
            print(directions[state], state)
            print(count, currents)

    return count


print(step_2("8_input.txt"))
