from graph import Node, Graph


def make_arbitrary_graph1():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    all_nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10]

    edges = {
        node1:  [node8, node2, node6],
        node2:  [node3],
        node3:  [node2, node4, node7],
        node4:  [node5],
        node5:  [node4],
        node6:  [node3],
        node7:  [node5, node1],
        node8:  [node9],
        node9:  [node10],
        node10: [node5, node1]
    }

    S1 = [node1, node3, node9, node5]
    S2 = [s for s in all_nodes if s not in S1]
    B = [node5]
    
    G = Graph(edges, S1, S2)
    return G, B


def get_input(i):
    if i == 1:
        G, B = make_arbitrary_graph1()
    return G, B
