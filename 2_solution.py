MAXIMAL = {'red': 12, 'green': 13, 'blue': 14}


def is_line_possible(line):
    tirages = line.split("; ")
    for tirage in tirages:
        couleurs = tirage.split(", ")
        for couple in couleurs:
            nombre, couleur = couple.split()
            if int(nombre) > MAXIMAL[couleur]:
                return False
    return True


def step_1():
    total_ids = 0
    current = 1
    for line in open("2_input.txt"):
        possible = True
        tirages = line.split(": ")[1]
        if is_line_possible(tirages):
            total_ids += current

        current += 1
    print(total_ids)


def get_minimum_set_power(tirages):
    minimum_set = {'red': 0, 'green': 0, 'blue': 0}
    product = 1
    tirages = tirages.split("; ")
    for tirage in tirages:
        couleurs = tirage.split(", ")
        for couple in couleurs:
            nombre, couleur = couple.split()
            if int(nombre) > minimum_set[couleur]:
                minimum_set[couleur] = int(nombre)
    for nombre in minimum_set.values():
        product = product * nombre
    return product


def step_2():
    total_powers = 0
    for line in open("2_input.txt"):
        tirages = line.split(": ")[1]

        total_powers += get_minimum_set_power(tirages)
    print(total_powers)


print(get_minimum_set_power(
    '1 green, 6 red, 4 blue; 2 blue, 6 green, 7 red; 3 red, 4 blue, 6 green; 3 green; 3 blue, 2 green, 1 red'))
step_2()
