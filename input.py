from graph import Node, Graph


def make_arbitrary_graph():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    edges = {
        node1: [node2],
        node2: [node2, node3],
        node3: [node1]
    }
    S1 = [node1, node3]
    S2 = [node2]
    return edges, S1, S2


def make_arbitrary_buchi_obj(G):
    return [G.S[0]]


def get_input():
    edges, S1, S2 = make_arbitrary_graph()
    G = Graph(edges, S1, S2)
    B = make_arbitrary_buchi_obj(G)
    return G, B
