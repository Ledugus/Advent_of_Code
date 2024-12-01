from itertools import combinations


def respects_groups(pattern, group_sizes):
    groups = pattern.split(".")
    groups = [group for group in groups if group]
    for i, group_size in enumerate(group_sizes):
        if len(groups[i]) != group_size:
            return False
    return True


def count_arrangement(pattern, groups_sizes):
    count = 0
    total_length = len(pattern)
    tags = pattern.count("#")
    missing_tags = sum(groups_sizes) - tags
    unknom_pos = [x for x in range(total_length) if pattern[x] == "?"]
    print(unknom_pos)
    subsets = combinations(unknom_pos, missing_tags)
    for subset in subsets:

        string = ""
        for x in range(total_length):
            if x in subset:
                string = string + "#"
                continue
            if x in unknom_pos:
                string = string + "."
                continue
            string = string + pattern[x]

        if respects_groups(string, groups_sizes):
            count += 1

    print(pattern, count)
    return count


def step_1(filename):
    total = 0
    f = open(filename)
    for line in f:
        pattern, groups = line.strip().split()
        groups = list(map(int, groups.split(",")))
        total += count_arrangement(pattern, groups)

    return total


def step_2(filename):
    total = 0
    f = open(filename)
    for line in f.readlines()[:10]:
        pattern, groups = line.strip().split()
        groups = list(map(int, groups.split(",")))
        pattern = "?".join([pattern]*5)
        groups = groups * 5
        print(pattern, groups)
        total += count_arrangement(pattern, groups)


print(step_2('12_test.txt'))
