def hash(string):
    current = 0
    print(f">{string}<")
    for char in string:
        current += ord(char)
        current = (17*current) % 256
    return current


def step_1(filename):
    f = open(filename)
    line = f.readline().strip().split(",")
    total = 0
    for instruction in line:
        hash_ = hash(instruction)
        total += hash_
        print(hash_)
    print(len(line))
    return total


print(step_1('15_input.txt'))
