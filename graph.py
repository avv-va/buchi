class Node:
    def __init__(self, index):
        self.index = index

class Graph:
    def __init__(self, edges, S1, S2):
        self.E = edges

        temp_S = set()
        for node in edges.keys():
            temp_S.add(node)
            for node_next in edges[node]:
                temp_S.add(node_next)

        self.S = list(temp_S)

        self.S1 = S1
        self.S2 = S2

        self.n = len(self.S)
        m = 0
        for n in self.E.keys():
            m += len(self.E[n])
        self.m = m
