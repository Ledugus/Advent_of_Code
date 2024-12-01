def hash(string):
    current = 0
    for char in string:
        current += ord(char)
        current = (17*current) % 256
    return current


def step_1(filename):
    f = open(filename)
    line = f.readline().strip().split(",")
    total = 0
    for instruction in line:
        total += hash(instruction)
    return total


def parse(string):
    if string[-1].isdigit():
        return string[:-2], True
    return string[:-1], False


def step_2(filename):
    f = open(filename)
    instructions = f.readline().strip().split(",")
    total = 0
    boxes = [[] for x in range(256)]
    for instruction in instructions:
        label, is_add = parse(instruction)
        current_box = boxes[hash(label)]
        pos = [x for x in range(len(current_box))
               if current_box[x][0] == label]
        if is_add:
            power = int(instruction[-1])
            if pos:
                current_box[pos[0]] = (label, power)
            else:
                current_box.append((label, power))
        elif pos:
            del current_box[pos[0]]
    total = 0
    for num_box, box in enumerate(boxes):
        for num_lens, lens in enumerate(box):
            total += lens[1] * (num_lens+1) * (num_box+1)
    print(boxes)
    return total


print(step_2('15_input.txt'))
