import networkx as nx
from itertools import combinations


def get_graph(filename):
    f = open(filename)
    edges = []
    for line in f.readlines():
        node, adj_list = line.strip().split(": ")
        adj_list = adj_list.split()
        edges.extend([(node, adj)
                     for adj in adj_list if (adj, node) not in edges])
    graph = nx.Graph()
    graph.add_edges_from(edges)
    return graph


def step_1(filename):
    graph = get_graph(filename)
    count = 1
    nodes = list(graph.nodes())
    part1 = nodes[:len(nodes)//2]
    part2 = nodes[len(nodes)//2:]
    partitions = nx.community.girvan_newman(graph)
    for partition in partitions:
        if len(partition) == 2:
            for x in partition:
                print(len(x), x)
                count = count * len(x)
            return count
        else:
            print("not good partition", len(partition))
    return count

    c = 0
    for edge in graph.edges():
        print("#######################",  c)
        c += 1
        c1 = 0
        graph.remove_edges_from([edge])
        for edge2 in graph.edges():
            print("C1", c1)
            c1 += 1
            graph.remove_edges_from([edge2])
            for edge3 in graph.edges():
                graph.remove_edges_from([edge3])
                connected_comps = list(nx.connected_components(graph))
                if len(connected_comps) == 2:
                    for x in connected_comps:
                        count = count * len(x)
                    return count
                graph.add_edges_from([edge3])
            graph.add_edges_from([edge2])
        graph.add_edges_from([edge])


print(step_1('25_input.txt'))
