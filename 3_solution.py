def get_matrix(filename) -> list[list[str]]:
    matrix = []
    for line in open(filename):
        line = list(line.strip())
        matrix.append(line)
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
    print(total_part_numbers)


def step_2():
    total_gear_ratios = 0
    matrix = get_matrix("3_input.txt")
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            

    print(total_gear_ratios)


step_1()
