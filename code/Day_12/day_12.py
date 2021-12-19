from typing import NewType


with open("code/Day_12/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

EDGES = [l.strip() for l in lines]

class Agent(object):
    def __init__(self, network):
        self.network = network
        self.start = network.start
        self.goal = network.end

    def traverse(self, nxt, path, routes, revisit):
        for nb in nxt.neighborgs:
            if nb.name == self.goal.name:
                path.append(nb.name)
                routes.append(path[:])
                path.pop()
            elif nb.name == self.start.name:
                continue

            elif nb.small and nb.name in path:
                if not revisit[0]:
                    revisit = (True, nb.name)
                    path.append(nb.name)
                    revisit, routes = self.traverse(nb, path, routes, revisit)
            else:
                path.append(nb.name)
                revisit, routes = self.traverse(nb, path, routes, revisit)
        if path.pop() == revisit[1]:
            revisit = (False, None)
        return revisit, routes
    
    def explore(self):
        path = [self.start.name]
        nxt = self.start
        routes = []
        revisit = (False, None)
        _, routes = self.traverse(nxt, path, routes, revisit)
        return routes


class Node(object):
    def __init__(self, name, next = None, small = False):
        self.name = name
        self.small = small
        if next is not None:
            self.neighborgs = [next]
        else:
            self.neighborgs = []
    
    def append(self, other):
        self.neighborgs.append(other)


    def __str__(self):
        string = "{}: [".format(self.name)
        for nb in self.neighborgs:
            string += " {} ".format(nb.name)
        return string + " ]"

    def __repr__(self):
        string = "{}: [".format(self.name)
        for nb in self.neighborgs:
            string += " {} ".format(nb.name)
        return string + " ]"




class Network(object):
    def __init__(self, edges):
        self.nodes = self.parse_edges(edges)
        self.start = [s for s in self.nodes if s.name == "start"][0]
        self.end = [e for e in self.nodes if e.name == "end"][0]    

    def parse_edges(self, edges):
        edges = [e.split("-") for e in edges]
        nodes = set([n for e in edges for n in e])
        edge_dict = {}
        network = []
        for node in nodes:
            if node not in edge_dict.keys():
                edge_dict[node] = []
            for edge in edges:
                if node in edge:
                    edge_dict[node].append([n for n in edge if n != node][0])
            if node.islower():
                small=True
            else:
                small=False
            network.append(Node(node, small=small))
        for nd in network:
            nbs = edge_dict[nd.name]
            for other in [o for o in network if o.name in nbs]:
                nd.append(other)
        return network
            
 

if __name__=="__main__":
    net = Network(EDGES)
    explorer = Agent(net)
    routes = explorer.explore()
    print(len(routes))