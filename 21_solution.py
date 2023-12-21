import numpy as np
import math


def get_matrix(filename):
    matrix = []
    list_grids = []
    start = []
    f = open(filename)
    for i, line in enumerate(f.readlines()):
        matrix_row = []
        for j, char in enumerate(line.strip()):
            matrix_row.append(char)
            if char == "S":
                start = (i, j)
        matrix.append(matrix_row)
    return np.array(matrix), start


def print_(grid, list_tiles):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) in list_tiles:
                print("O", end="")
            else:
                print(grid[x][y], end="")
        print()


def get_neighbours(pos, shape):
    possible = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    voisins = []
    for i in range(len(possible)):
        new_pos = (pos[0] + possible[i][0], pos[1] + possible[i][1])
        if 0 <= new_pos[0] < shape[0] and 0 <= new_pos[1] < shape[1]:
            voisins.append(new_pos)
    return voisins


def dijkstra(grid: np.ndarray, start_pos, dist_limit: int) -> int:
    height, width = grid.shape
    visited = []
    unvisited: list[tuple[int, int]] = [
        (x, y) for x in range(height)
        for y in range(width)
    ]
    distances = np.full((height, width), math.inf)
    distances[start_pos] = 0
    previous = {start_pos: start_pos}
    current_pos = start_pos
    while unvisited:
        current_pos = min(unvisited, key=lambda pos: distances[pos])
        if distances[current_pos] > dist_limit:
            break
        print("Currently watching node :", current_pos,
              "with distance : ", distances[current_pos])
        unvisited.remove(current_pos)
        visited.append(current_pos)
        for voisin in get_neighbours(current_pos, grid.shape):
            if voisin in visited:
                continue
            if grid[voisin] == '#':
                continue
            # print(distances[voisin], grid[voisin])
            if distances[voisin] > distances[current_pos] + 1:
                distances[voisin] = distances[current_pos] + 1
                # print(f"setting {current_pos} as previous of {voisin}")
                previous[voisin] = current_pos
    print([pos for pos in visited if grid[pos] == "#"])
    attainable_pos = [pos for pos in visited if distances[pos]
                      <= dist_limit and distances[pos] % 2 == dist_limit % 2]
    print_(grid, attainable_pos)
    print(attainable_pos)
    return len(attainable_pos)


def step_1(filename):
    grid, s_pos = get_matrix(filename)

    return dijkstra(grid, s_pos, 64)


print(step_1('21_input.txt'))
