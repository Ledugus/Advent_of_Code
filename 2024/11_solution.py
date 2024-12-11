def increment_stones(stones):
    new_stones = []

    for stone in stones:
        size = len(str(stone))
        if stone == 0:
            new_stones.append(1)
        elif size % 2 == 0:
            new_stones.append(int(str(stone)[: size // 2]))
            new_stones.append(int(str(stone)[size // 2 :]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


def step_1(filename):
    f = open(filename)
    stones = list(map(int, f.readline().strip().split()))
    f.close()

    for _ in range(25):
        stones = increment_stones(stones)
    return len(stones)


def step_2(filename):
    f = open(filename)
    stones_list = list(map(int, f.readline().strip().split()))
    f.close()

    transition_dictionary = {}
    nb_occurences = {}
    for i in range(0, 10):
        transition_dictionary[i] = increment_stones([i])
        nb_occurences[i] = 0
    for _ in range(4):
        for i in list(transition_dictionary.values()):
            for j in i:
                transition_dictionary[j] = increment_stones([j])
                nb_occurences[j] = 0

    total = 0

    # treat each stone in the input individually
    for begin_stone in stones_list:
        stones = [begin_stone]

        for key in transition_dictionary:
            nb_occurences[key] = 0

        if begin_stone in nb_occurences:
            nb_occurences[begin_stone] += 1
            stones = []

        for _ in range(75):
            new_occurences_count = {}
            new_stones = []

            for key in nb_occurences:
                new_occurences_count[key] = 0

            for stone_id, nb_stones in nb_occurences.items():
                for next_stone in transition_dictionary[stone_id]:
                    new_occurences_count[next_stone] += nb_stones

            for stone_id in stones:
                size = len(str(stone_id))
                if stone_id in transition_dictionary:
                    for next_stone in transition_dictionary[stone_id]:
                        new_occurences_count[next_stone] += 1

                elif size % 2 == 0:
                    new_stones.append(int(str(stone_id)[: size // 2]))
                    new_stones.append(int(str(stone_id)[size // 2 :]))
                else:
                    new_stones.append(stone_id * 2024)

            stones = new_stones
            nb_occurences = new_occurences_count

        total += sum(nb_occurences.values()) + len(stones)
    return total


print(step_1("2024/11_test.txt"))
print(step_1("2024/11_input.txt"))

print(step_2("2024/11_test.txt"))
print(step_2("2024/11_input.txt"))
