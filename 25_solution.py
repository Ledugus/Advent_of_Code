class Graph:
    def __init__(self, nodes, edges) -> None:
        self.nodes = nodes
        self.edges = edges

    def __str__(self) -> str:
        return f"Graph : \nNodes: {self.nodes}\n Edges: {self.edges}"


def get_graph(filename) -> Graph:
    f = open(filename)
    edges = []
    nodes = []
    for line in f.readlines():
        node, adj_list = line.strip().split(": ")
        adj_list = adj_list.split()
        edges.extend([(node, adj)
                     for adj in adj_list if (adj, node) not in edges])
        nodes.append(node)

    nodes = list(set(nodes))
    return Graph(nodes, edges)


def step_1(filename):
    graph = get_graph(filename)
    return graph


print(step_1('25_test.txt'))
