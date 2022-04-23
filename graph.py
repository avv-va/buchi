import math
from tkinter import N 

class Node:
    def __init__(self, index):
        self.index = index

class Graph:
    def __init__(self, edges, S1, S2):
        self.E = edges
        self.S = [node for node in edges.keys()]
        self.S1 = S1
        self.S2 = S2

        self.n = len(self.S)
        m = 0
        for n in self.E.keys():
            m += len(self.E[n])
        self.m = m



# G = Graph(edges)
# B = [node4]

# m = len(G.edges)
# n = len(G.nodes)
# S_0 = G.nodes
# C = [s for s in S_0 if s not in B]
# W = {}
# i = 0
# W[i] = {}

# # G[i] = graph # G_0 = G
# S[i] =G.nodes


# while (i!=0 or len(W[i])!=0):
#     if len(source(W[i], G)) >= m/math.log(n):
#         W[i+1] = avoid_set_classical()


