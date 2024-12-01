gears_dico = {}


def get_matrix(filename) -> list[list[str]]:
    matrix = []
    for row, line in enumerate(open(filename)):
        matrix_row = []
        for col, char in enumerate(line):
            matrix_row.append(char)
            if char == "*":
                gears_dico[(row, col)] = []
        matrix.append(matrix_row)

    return matrix


def check_neighbours(matrix, row, col) -> bool:

    neighbours_rel_pos = [(1, 1), (1, 0), (1, -1), (0, -1),
                          (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    for rel_x, rel_y in neighbours_rel_pos:
        try:
            char = matrix[row+rel_x][col+rel_y]
        except:
            continue
        if not char.isdigit() and char != ".":
            return True
    return False


def step_1():
    total_part_numbers = 0
    current_number = ""
    current_number_valid = False
    matrix = get_matrix("3_input.txt")
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col].isdigit():
                current_number = current_number + matrix[row][col]
                if check_neighbours(matrix, row, col):
                    current_number_valid = True
                continue

            if current_number and current_number_valid:
                total_part_numbers += int(current_number)
            current_number = ""
            current_number_valid = False
        if current_number and current_number_valid:
            total_part_numbers += int(current_number)
        current_number = ""
        current_number_valid = False
    return total_part_numbers


def get_gears_neighbours(matrix, row, col):
    set_gears = set()
    neighbours_rel_pos = [(1, 1), (1, 0), (1, -1), (0, -1),
                          (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    for rel_x, rel_y in neighbours_rel_pos:
        try:
            char = matrix[row+rel_x][col+rel_y]
        except:
            continue
        if char == "*":
            set_gears.add((row+rel_x, col+rel_y))
    return set_gears


def step_2():

    matrix = get_matrix("3_input.txt")
    current_number_gears = set()
    current_number = ""
    for row in range(len(matrix)):
        for gear_pos in current_number_gears:
            gears_dico[gear_pos].append(int(current_number))
        current_number = ""
        current_number_gears = set()
        for col in range(len(matrix[row])):
            if matrix[row][col].isdigit():
                current_number = current_number + matrix[row][col]
                current_number_gears = current_number_gears.union(
                    get_gears_neighbours(matrix, row, col))
                continue

            for gear_pos in current_number_gears:
                gears_dico[gear_pos].append(int(current_number))
            current_number = ""
            current_number_gears = set()

    total_gear_ratios = 0
    for list_numbers in gears_dico.values():
        if len(list_numbers) == 2:
            total_gear_ratios += list_numbers[0] * list_numbers[1]
    return total_gear_ratios


print(step_2())
