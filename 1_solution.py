def step_1():
    total = 0

    for line in open("1_input.txt"):
        digits = [int(ch) for ch in line if ch.isdigit()]
        total += (10*(digits[0]) + digits[-1])
    print(total)


def step_2():
    total = 0
    alpha_digits = ["zero", "one", "two", "three",
                    "four", "five", "six", "seven", "eight", "nine"]

    for line in open("1_input.txt", "r"):
        digits = []
        for index in range(len(line)):
            if line[index].isdigit():
                digits.append(int(line[index]))
                continue
            for dig_index, digit in enumerate(alpha_digits):
                try:
                    if line[index:index+len(digit)] == digit:
                        digits.append(dig_index)
                except:
                    pass
        total += (10*(digits[0]) + digits[-1])
    print(total)


step_2()
