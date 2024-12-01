import math
import numpy as np


def get_matrix(filename):
    matrix = []
    list_grids = []
    f = open(filename)
    for line in f.readlines():
        matrix_row = []
        for char in line.strip():
            matrix_row.append(int(char))
        matrix.append(matrix_row)
    return np.array(matrix)


def print_(grid, list_tiles):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) in list_tiles:
                print(".", end="")
            else:
                print(grid[x][y], end="")
        print()


def get_neighbours(pos, shape):
    possible = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    voisins = []
    for i in range(len(possible)):
        new_pos = (pos[0] + possible[i][0], pos[1] + possible[i][1])
        if 0 <= new_pos[0] < shape[0] and 0 <= new_pos[1] < shape[1]:
            voisins.append((*new_pos, i))
    return voisins


def in_line_4(pos1, pos2):
    if abs(pos1[0]-pos2[0]) == 4:
        return True
    if abs(pos1[1]-pos2[1]) == 4:
        return True
    return False


def dijkstra(grid: np.ndarray, start_pos: tuple[int, int, int], end_pos: tuple[int, int]) -> int:
    height, width = grid.shape
    visited = []
    unvisited: list[tuple[int, int, int]] = [
        (x, y, dir) for x in range(height)
        for y in range(width)
        for dir in range(4)
    ]
    distances = np.full((height, width, 4), math.inf)
    distances[start_pos] = 0
    previous = {start_pos: start_pos}
    current_pos = start_pos
    while unvisited:
        current_pos = min(unvisited, key=lambda pos: distances[pos])
        print("Currently watching node :", current_pos,
              "with distance : ", distances[current_pos])
        unvisited.remove(current_pos)
        visited.append(current_pos)
        for voisin in get_neighbours(current_pos, grid.shape):
            if voisin in visited:
                continue
            current = current_pos
            for _ in range(3):
                current = previous[current]
            if in_line_4(current, voisin):
                continue
            # print(distances[voisin], grid[voisin])
            if distances[voisin] > distances[current_pos] + grid[voisin[:2]]:
                distances[voisin] = distances[current_pos] + grid[voisin[:2]]
                # print(f"setting {current_pos} as previous of {voisin}")
                previous[voisin] = current_pos

    path = []
    while current_pos != start_pos:
        path.append(current_pos)
        current_pos = previous[current_pos]
    print_(grid, [pos[:2] for pos in path])
    return min([distances[(*end_pos, x)] for x in range(4)])


def step_1(filename):
    grid = get_matrix(filename)
    start_pos = (0, 0, 0)
    end_pos = (len(grid)-1, len(grid[0])-1)

    return dijkstra(grid, start_pos, end_pos)


print(step_1('17_test.txt'))
