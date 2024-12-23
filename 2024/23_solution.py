import numpy as np
import matplotlib.pyplot as plt
from time import time
from utils import *
import networkx as nx


def step_1(filename):
    exec_time = time()
    f = open(filename)
    links = list(
        map(lambda x: tuple(x.strip().split("-")), f.read().strip().split("\n"))
    )
    f.close()

    neightbours = {}
    triangles = set()
    nodes_with_t = set()
    for link in links:
        if link[0] not in neightbours:
            neightbours[link[0]] = set()
        if link[1] not in neightbours:
            neightbours[link[1]] = set()
        neightbours[link[0]].add(link[1])
        neightbours[link[1]].add(link[0])
        if link[0][0] == "t":
            nodes_with_t.add(link[0])
        if link[1][0] == "t":
            nodes_with_t.add(link[1])
    for node in nodes_with_t:
        # check if there is a triangle with this node
        for neightbour in neightbours[node]:
            for neightbour_neightbour in neightbours[neightbour]:
                if neightbour_neightbour in neightbours[node]:
                    # add the triangle to the set
                    triangles.add(
                        tuple(sorted([node, neightbour, neightbour_neightbour]))
                    )

    print("Part 1 exec time :", time() - exec_time)
    return len(triangles)


def step_2(filename):
    exec_time = time()

    f = open(filename)
    G = nx.Graph()
    for link in map(
        lambda x: tuple(x.strip().split("-")), f.read().strip().split("\n")
    ):
        G.add_nodes_from(link)
        G.add_edge(link[0], link[1])
    f.close()
    max_clique = max(list(nx.find_cliques(G)), key=lambda x: len(x))
    formatted_result = ",".join(sorted(max_clique))
    print("Part 2 exec time :", time() - exec_time)
    return formatted_result


# print(step_1("2024/23_test.txt"))
print(step_1("2024/23_input.txt"))

# print(step_2("2024/23_test.txt"))
print(step_2("2024/23_input.txt"))
