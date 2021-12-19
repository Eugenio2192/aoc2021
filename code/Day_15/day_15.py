from numpy import array, zeros, sum
from enum import Enum
import networkx as nx
def get_input():
    with open("code/Day_15/input.txt","r", encoding="utf-8-sig") as file:
        lines = file.readlines()
    lines= [l.strip("\n") for l in lines]
    mapped = array([[int(el) for el in l] for l in lines])
    return mapped

def dist(a,b):
    return 1

def part_1():
    data = get_input()
    path_array = zeros(data.shape, dtype=bool)
    G = nx.grid_graph(dim=data.shape)
    G = nx.DiGraph(G)
    nx.set_edge_attributes(G, {e: data[e[1]] for e in G.edges()}, "cost")
    path = nx.astar_path(G, (0, 0), (data.shape[0]-1, data.shape[1]-1), heuristic=dist, weight="cost")
    for element in path:
        path_array[element] = 1
    print(sum(path_array * data) -1 )

def part_2():
    data = get_input() 
    dims = data.shape
    bigger = zeros((dims[0] * 5, dims[1] * 5))
    bigger[0:dims[0], 0:dims[1]] = data
    for i in range(4):
        bigger[((i+1)*dims[0]):((i+2)*dims[0]), 0:dims[1]] = (bigger[(i*dims[0]):((i+1)*dims[0]), 0:dims[1]]%9) + 1
    for i in range(5):
        for j in range(4):
            bigger[(i*dims[0]):((i+1)*dims[0]), ((j+1)*dims[1]):((j+2)*dims[1])] = (bigger[(i*dims[0]):((i+1)*dims[0]), (j*dims[1]):((j+1)*dims[1])] % 9) + 1
    for b in bigger:
        string = ""
        for n in b:
            string += str(int(n))

    path_array = zeros(bigger.shape, dtype=bool)
    G = nx.grid_graph(dim=bigger.shape)
    G = nx.DiGraph(G)
    nx.set_edge_attributes(G, {e: bigger[e[1]] for e in G.edges()}, "cost")
    path = nx.astar_path(G, (0, 0), (bigger.shape[0]-1, bigger.shape[1]-1), heuristic=dist, weight="cost")
    for element in path:
        path_array[element] = 1
    print(sum(path_array * bigger) -1 )
if __name__ == "__main__":
    part_2()