def get_galaxy_pos(filename):
    rows = []
    cols = []
    f = open(filename)
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):

            col = j
            if char == "#":
                rows.append(i)
                cols.append(j)

    return rows, cols, len(lines), len(lines[0].strip())


def step_1(filename):
    rows, cols, len_rows, len_cols = get_galaxy_pos(filename)

    empty_rows = [row for row in range(len_rows) if row not in rows]
    empty_cols = [col for col in range(len_cols) if col not in cols]
    new_galaxy_rows = []
    for galaxy_row in rows:
        new_galaxy_row = galaxy_row
        for row in empty_rows:
            if galaxy_row > row:
                new_galaxy_row += 999999
        new_galaxy_rows.append(new_galaxy_row)
    new_galaxy_cols = []
    for galaxy_col in cols:
        new_galaxy_col = galaxy_col
        for col in empty_cols:
            if galaxy_col > col:
                new_galaxy_col += 999999
        new_galaxy_cols.append(new_galaxy_col)
    total_distance = 0
    num_galaxy_comp = 0
    for first in range(len(new_galaxy_rows)):
        for second in range(first+1, len(new_galaxy_cols)):
            num_galaxy_comp += 1
            distance = abs(new_galaxy_rows[first]-new_galaxy_rows[second]) + abs(
                new_galaxy_cols[first]-new_galaxy_cols[second])
            total_distance += distance
    return total_distance, num_galaxy_comp


print(step_1('11_input.txt'))
