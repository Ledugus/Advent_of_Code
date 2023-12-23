import numpy as np
import math
import networkx as nx

GOOD_DIR = [">.", "<.", ".", "v."]


def get_matrix(filename):
    matrix = []
    f = open(filename)
    for i, line in enumerate(f.readlines()):
        matrix_row = []
        for j, char in enumerate(line.strip()):
            matrix_row.append(char)
        matrix.append(matrix_row)
    return np.array(matrix, np.str_)


def get_valid_neighbours(pos, grid: np.ndarray, valid=False):
    possible = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    voisins = []
    shape = grid.shape
    for i in range(len(possible)):
        new_pos = (pos[0] + possible[i][0], pos[1] + possible[i][1])
        try:
            if valid:

                if grid[new_pos] in GOOD_DIR[i]:
                    voisins.append(new_pos)
            else:
                if grid[new_pos] != "#":  # in GOOD_DIR[i]:
                    voisins.append(new_pos)
        except:
            pass
    return voisins


class Path:
    id = 0

    def __init__(self, start, second, grid) -> None:
        self.start = start
        self.second = second
        self.length, self.end = self.get_path_length(grid)
        self.previous = []
        self.id = Path.id
        Path.id += 1

    def get_path_length(self, grid):
        previous_pos = self.start
        current_pos = self.second
        length = 1
        while True:
            neighbours = get_valid_neighbours(current_pos, grid)
            if len(neighbours) == 2:
                length += 1
                new_pos = neighbours[1-neighbours.index(previous_pos)]
                previous_pos = current_pos
                current_pos = new_pos
            else:
                break
        return length, current_pos

    def __str__(self) -> str:
        return f"Path from {self.start} to {self.end} ({self.length})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: 'Path') -> bool:
        return self.start == __value.start and self.end == __value.end


def step_1(filename):
    grid = get_matrix(filename)
    start_pos = (0, 1)
    finish_pos = (grid.shape[0]-1, grid.shape[1]-2)
    # initialiser le premier chemin
    open_paths = [Path(start_pos, (1, 1), grid)]
    path_starts_here: dict[tuple[int, int], list[Path]] = {finish_pos: []}
    total_paths = open_paths
    # tant qu'il y a de nouveaux chemins
    while open_paths:

        new_paths = []
        # pour chaque chemin ouvert
        for path in open_paths:

            liste = path_starts_here.get(path.start, [])
            liste.append(path)
            path_starts_here[path.start] = liste
            if path.end != finish_pos:
                for voisin in get_valid_neighbours(path.end, grid, valid=True):
                    new_path = Path(path.end, voisin, grid)
                    new_paths.append(new_path)
                    if new_path not in total_paths:
                        total_paths.append(new_path)
        open_paths = new_paths
    edge_list = []

    for path in total_paths:
        edge_list.append((path.start, path.end, path.length))
    G = nx.DiGraph()
    G.add_weighted_edges_from(edge_list)
    return nx.dag_longest_path_length(G)


print(step_1('23_input.txt'))
