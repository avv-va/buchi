def print_nodes(txt, S):
    print(f"Printing nodes for {txt}:")
    for s in S:
        print(s.index, end=", ")
    print()


def print_graph(txt, G):
    print_nodes(txt, G.S)
    for n in G.E:
        for nn in G.E[n]:
            print(f"{n.index}->{nn.index}", end=", ")
    print()
    print_nodes(f"{txt} S1", G.S1)
    print_nodes(f"{txt} S2", G.S2)