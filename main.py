from graph import Graph
from input import get_input


def print_nodes(txt, S):
    print(f"Printing nodes for {txt}:")
    for s in S:
        print(s.index, end=", ")
    print()

def find_sub_graph(G, S_):
    edges_n = {}
    for s in S_:
        if s in G.E:
            edges_n[s] = []
            for n in G.E[s]:
                if n in S_:
                    edges_n[s].append(n)
    S1_n = [s for s in G.S1 if s in S_]
    S2_n = [s for s in G.S2 if s in S_]
    return Graph(edges_n, S1_n, S2_n)


def attr(l, U, G):
    i = 0
    R_ = {}
    R_[i] = U

    S_f = G.S1 if l==1 else G.S2
    S_s = G.S2 if l==1 else G.S1

    while 1:
        R_temp1, R_temp2 = [], []
        for s in S_f:
            if set(G.E[s]).intersection(R_[i]):
                R_temp1.append(s)
        for s in S_s:
            if set(G.E[s]).issubset(R_[i]):
                R_temp2.append(s)
        
        R_[i+1] = list(set(R_temp1 + R_temp2 + R_[i]))
        if R_[i+1] == R_[i]:
            break
        i = i + 1

    
    return R_[i+1]


def print_graph(txt, G):
    print_nodes(txt, G.S)
    for n in G.E:
        for nn in G.E[n]:
            print(f"{n.index}->{nn.index}", end=", ")
    print()
    print_nodes(f"{txt} S1", G.S1)
    print_nodes(f"{txt} S2", G.S2)

def play_buchi_game(G, B):
    i = 0
    G_ = {}
    G_[i] = G
    S_ = {}
    S_[i] = G.S
    C = [s for s in G.S if s not in B]
    W_ = {}
    W_[i] = []

    while (i<=10):
        C_, C1_, C2_ = [], [], []

        C_ = set(C).intersection(S_[i])
        print_nodes("C_", C_)

        for s in set(G.S1).intersection(C_):
            if set(G.E[s]).intersection(S_[i]).issubset(C_):
                C1_.append(s)
        print_nodes("C1_", C1_)
        
        for s in set(G.S2).intersection(C_):
            if set(G.E[s]).intersection(C_):
                C2_.append(s)
        print_nodes("C2_", C2_)

        X_ = attr(2, C1_ + C2_, G_[i])
        print_nodes("X_", X_)

        Z_ = set(X_).intersection(C_)
        print_nodes("Z_", Z_)

        S_wo_Z = [s for s in S_[i] if s not in Z_]
        print_nodes("S_wo_Z", Z_)

        X_wo_Z = [s for s in X_ if s not in Z_]
        print_nodes("W_wo_Z", X_wo_Z)

        D_temp1, D_temp2 = [], []
        for s in set(G.S1).intersection(Z_):
            if set(G.E[s]).intersection(S_[i]).intersection(S_wo_Z):
                D_temp1.append(s)
        for s in set(G.S2).intersection(Z_):
            if set(G.E[s]).intersection(S_[i]).issubset(X_wo_Z + S_wo_Z):
                D_temp2.append(s)
        D = D_temp1 + D_temp2
        print_nodes("D", D)

        G_X = find_sub_graph(G_[i], X_)
        print_graph('G_X', G_X)
    

        L = attr(1, D, G_X)
        print_nodes("L", L)

        Tr = [s for s in Z_ if s not in L]
        print_nodes("Tr", Tr)

        W_[i+1] = attr(2, Tr, G_[i])
        print_nodes(f"W_[{i+1}]", W_[i+1])

        S_[i+1] = [s for s in S_[i] if s not in W_[i+1]]
        print_nodes(f"S_[{i+1}]", S_[i+1])

        G_[i+1] = find_sub_graph(G, S_[i+1])
        print_graph(f"G_[{i+1}]", G_[i+1])
        i = i + 1

    W = []
    for j in range(0, i):
        W = W + W_[j]
    return W




if __name__ == "__main__":
    G, B = get_input(1)

    winning_set = play_buchi_game(G, B)
    print_nodes("winning set", winning_set)
    