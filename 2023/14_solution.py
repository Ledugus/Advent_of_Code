def get_matrix(filename) -> list[list[str]]:
    matrix = []
    list_grids = []
    f = open(filename)
    for line in f.readlines():
        matrix_row = []
        for char in line.strip():
            matrix_row.append(char)
        matrix.append(matrix_row)
    return [list(row) for row in zip(*matrix)]


def cascade(row):
    for index in range(len(row)):
        if row[index] != "O":
            continue
        new_index = index - 1
        while new_index >= 0 and row[new_index] not in ["O", "#"]:
            new_index -= 1
        row[index] = "."
        row[new_index+1] = "O"

    return row


def step_1(filename):
    total_weight = 0
    grid = get_matrix(filename)
    for i in range(len(grid)):
        grid[i] = cascade(grid[i])
        row_weight = sum(
            len(grid[i])-x for x in range(len(grid[i])) if grid[i][x] == "O")
        print(row_weight)
        total_weight += row_weight
    return total_weight


def step_2(filename):
    total_weight = 0
    grid = get_matrix(filename)
    for i in range(len(grid)):
        grid[i] = cascade(grid[i])
        row_weight = sum(
            len(grid[i])-x for x in range(len(grid[i])) if grid[i][x] == "O")
        print(row_weight)
        total_weight += row_weight
    return total_weight


print(step_1('14_input.txt'))
