def get_matrix(filename) -> tuple[list[list[str]], tuple[int, int]]:
    matrix = []
    s_pos = (0, 0)
    for row, line in enumerate(open(filename)):
        matrix_row = []
        for col, char in enumerate(line.strip()):
            matrix_row.append(char)
            if char == "S":
                s_pos = (row, col)
        matrix.append(matrix_row)

    return matrix, s_pos


def print_grid(grid, highlight_pos=(0, 0), char="X"):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) == highlight_pos:
                col = char
            print(col, end=" ")
        print()


next = {
    "|": [(1, 0), (-1, 0)],
    "J": [(-1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
    "-": [(0, -1), (0, 1)],
    ".": []
}


def step_1(filename):

    grid, s_pos = get_matrix(filename)

    count = 1
    current_pos = (s_pos[0]-1, s_pos[1])
    origin = (1, 0)
    cycle = [s_pos]
    while current_pos not in cycle:
        cycle.append(current_pos)

        row, col = current_pos
        count += 1
        next_pos_list = next[grid[row][col]]

        rel_row, rel_col = next_pos_list[1-next_pos_list.index(origin)]
        print(rel_row, rel_col)
        origin = (-rel_row, -rel_col)
        current_pos = (row+rel_row, col+rel_col)
        print("new current pos", current_pos)
    print("s", s_pos)
    return len(cycle) // 2


print(step_1('10_input.txt'))
