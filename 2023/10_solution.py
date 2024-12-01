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


def step_2(filename):

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
    count = 0
    for x in range(len(grid)):
        inside = False
        last_turn = ""
        for y in range(len(grid[0])):
            if (x, y) in cycle:

                char = grid[x][y]
                if char == "S":
                    char = "J"
                if char == "-":
                    continue
                if char == "|":
                    inside = not inside
                elif char in ["F", "L"]:
                    last_turn = char
                elif char == "J":
                    if last_turn == "F":
                        inside = not inside
                        last_turn = ""
                elif char == "7":
                    if last_turn == "L":
                        inside = not inside
                        last_turn = ""

            elif inside:
                count += 1
            print((x, y), "inside :", inside, "last turn :", last_turn)

    return count


print(step_2('10_input.txt'))
