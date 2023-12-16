import numpy as np
from numpy import ndarray


def get_matrix(filename) -> ndarray:
    matrix = []
    list_grids = []
    f = open(filename)
    for line in f.readlines():
        matrix_row = []
        for char in line.strip():
            matrix_row.append(char)
        matrix.append(matrix_row)
    return np.array(matrix)


#             right    left      up     down
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
char_to_heading = {
    '.': [0, 1, 2, 3],
    "/": [2, 3, 0, 1],
    "\\": [3, 2, 1, 0],
    "|": [2, 2, 2, 3],
    "-": [0, 1, 0, 0]
}


def add(tuple1, tuple2):
    return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])


def print_(grid, list_tiles):
    list_tiles = [tile[0] for tile in list_tiles]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) in list_tiles:
                print("#", end="")
            else:
                print(".", end="")
        print()


def step_1(filename, grid=None, first_beam=((0, 0), 0)):
    if grid is None:
        grid = get_matrix(filename)
    list_tiles = []
    new_beams = [first_beam]
    print(first_beam[0][0])
    while new_beams:
        beams = new_beams[:]
        new_beams = []
        for beam in beams:
            pos, heading = beam
            if beam in list_tiles:
                continue
            if not (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
                continue
            char = grid[pos]
            new_heading = char_to_heading[char][heading]
            new_beams.append((add(pos, directions[new_heading]), new_heading))
            list_tiles.append((pos, heading))

            if char == '-' and heading in [2, 3]:
                new_beams.append((add(pos, directions[1]), 1))
            if char == '|' and heading in [0, 1]:
                new_beams.append((add(pos, directions[3]), 3))
    tiles = []
    for tile in list_tiles:
        if tile[0] not in tiles:
            tiles.append(tile[0])
    return len(tiles)


def step_2(filename):
    """
    Force brute, il se fait que la config était le long de la
    colonne de droite, que j'ai testé en premier. Idée d'opti :
    trouver les téléportations (lignes de points) pour chaque noeud de direction
    puis additionner tous les tronçons empruntés.
    """
    result_list = []
    grid = get_matrix(filename)
    # loop sauvage mais ça a fonctionné XD
    for x in range(100):
        result_list.append(step_1(filename, grid=grid, first_beam=((x, 0), 0)))
    return max(result_list)


print(step_2('16_input.txt'))
