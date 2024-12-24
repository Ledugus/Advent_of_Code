import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from time import time
from utils import *


def and_(a, b):
    return str(int(a) & int(b))


def or_(a, b):
    return str(int(a) | int(b))


def xor(a, b):
    return str(int(a) ^ int(b))


def evaluate(wire_values, gates_dict, wire):
    if wire in wire_values:
        return wire_values[wire]
    input1, input2, op = gates_dict[wire]
    wire_values[wire] = op(
        evaluate(wire_values, gates_dict, input1),
        evaluate(wire_values, gates_dict, input2),
    )
    return wire_values[wire]


def step_1(filename):
    exec_time = time()
    ope = {"AND": and_, "OR": or_, "XOR": xor}
    f = open(filename)
    wires, gates = f.read().split("\n\n")
    f.close()
    gates_dict = {}
    wire_values = {}
    z_wires = set()
    for wire in wires.strip().split("\n"):
        wire = wire.split(": ")
        wire_values[wire[0]] = wire[1]
    for gate in gates.strip().split("\n"):
        inputs, output = gate.split(" -> ")
        input1, op, input2 = inputs.split(" ")
        if output[0] == "z":
            z_wires.add(output)
        gates_dict[output] = (input1, input2, ope[op])

    result = ""
    z_wires = sorted(z_wires)
    for z_wire in z_wires:
        result = evaluate(wire_values, gates_dict, z_wire) + result
    print("Part 1 exec time :", time() - exec_time)
    return int(result, 2)


def step_2(filename):
    exec_time = time()
    G = nx.DiGraph()
    f = open(filename)
    wires, gates = f.read().split("\n\n")
    f.close()
    wire_values = {}
    for wire in wires.strip().split("\n"):
        wire = wire.split(": ")
        wire_values[wire[0]] = wire[1]
        G.add_node(wire[0], value=wire[1])
    for gate in gates.strip().split("\n"):
        inputs, output = gate.split(" -> ")
        input1, op, input2 = inputs.split(" ")
        if output[0] == "z":
            G.add_node(output, value=op)
        else:
            G.add_node(output, value=op)
        G.add_edge(input1, output, label=input1)
        G.add_edge(input2, output, label=input2)

    pos = {}
    second_layer_pos = 0
    second_layer = set()
    third_layer_pos = 0
    for node in G.nodes:
        for pred in G.predecessors(node):
            if pred[0] == "x" or pred[0] == "y":
                pos[node] = (10, second_layer_pos)
                second_layer_pos += 4
                second_layer.add(node)
                break
    for node in G.nodes:
        if node in second_layer:
            continue
        for pred in G.predecessors(node):
            if pred in second_layer:
                pos[node] = (20, third_layer_pos)
                third_layer_pos += 4
                break
        if node[0] == "z":
            pos[node] = (40, 4 * int(node[1:]))
        elif node[0] == "x":
            pos[node] = (0, 20 + 4 * int(node[1:]))
        elif node[0] == "y":
            pos[node] = (0, 4 * int(node[1:]))
    pos = nx.spring_layout(G, pos=pos, fixed=pos.keys(), scale=2, k=10)
    nx.draw(G, pos, with_labels=True)

    print("Part 2 exec time :", time() - exec_time)
    plt.show()
    return 0


print(step_1("2024/24_test.txt"))
print(step_1("2024/24_input.txt"))

print(step_2("2024/24_test.txt"))
print(step_2("2024/24_input.txt"))

