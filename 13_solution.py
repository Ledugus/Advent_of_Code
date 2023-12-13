def get_matrix(filename) -> list[list[str]]:
    matrix = []
    list_grids = []
    f = open(filename)
    for line in f.readlines():
        if not line.strip():
            list_grids.append(matrix)
            matrix = []
            continue
        matrix_row = []
        for char in line.strip():
            matrix_row.append(char)
        matrix.append(matrix_row)
    list_grids.append(matrix)
    return list_grids


def is_mirror(row_index, grid):
    for ecart in range(1, min(row_index+1, len(grid)-row_index+1)):
        print("ecart", ecart)
        print("checking rows", row_index - ecart, row_index - 1 + ecart)
        if grid[row_index - ecart] != grid[row_index - 1 + ecart]:
            print("rows not equal")
            return False
    return True


def get_nb_diffs(line1, line2):
    count = 0
    for x in range(len(line1)):
        if line1[x] != line2[x]:
            count += 1
    return count


def is_mirror_2(row_index, grid):
    has_changed = False
    for ecart in range(1, min(row_index+1, len(grid)-row_index+1)):
        print("ecart", ecart)
        print("checking rows", row_index - ecart, row_index - 1 + ecart)
        nb_diffs = get_nb_diffs(
            grid[row_index - ecart], grid[row_index - 1 + ecart])
        if nb_diffs == 1 and not has_changed:
            has_changed = True
        if nb_diffs > 1:
            print("Too much errors in line")
            return False

    if has_changed:
        return True


def get_mirror_col(grid):
    transpose = [list(row) for row in zip(*grid)]
    return get_mirror_row(transpose)


def get_mirror_row(grid):
    for row in range(1, len(grid)):
        print()
        print("test row", row)
        if is_mirror_2(row, grid):
            return row
    return None


def step_1(filename):
    total = 0
    list_grids = get_matrix(filename)
    for grid in list_grids:
        row = get_mirror_row(grid)
        if row:
            total += 100*row
            continue

        col = get_mirror_col(grid)
        if col:
            total += col
    return total


print(step_1('13_input.txt'))
