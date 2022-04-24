from graph import Graph
from input import get_input

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
            if set(G.E(s)).intersection(R_[i]):
                R_temp1.append(s)
        for s in S_s:
            if set(G.E(s)).issubset(R_[i]):
                R_temp2.append(s)
        
        R_[i+1] = list(set(R_temp1)) + list(set(R_temp2)) + list(set(R_[i]))
        if R_[i+1] == R_[i]:
            break
        i = i + 1

    return R_[i+1]



def play_buchi_game(G, B):
    i = 0
    G_ = {}
    G_[i] = G
    S_ = {}
    S_[i] = G.S
    C = [s for s in G.S if s not in B]
    W_ = {}
    W_[i] = []

    while (i!=0 or len(W_[i])==0):
        C_, C1_, C2_ = [], [], []

        C_ = set(C).intersection(S_[i]) 

        for s in set(G.S1).intersection(C_[i]):
            if set(G.E[s]).intersection(S_[i]).issubset(C_[i]):
                C1_.append(s)
        
        for s in set(G.S2).intersection(C_[i]):
            if set(G.E[s]).intersection(C_[i]):
                C2_.append(s)

        X_ = attr(2, C1_[i] + C2_[i], G_[i])
        Z_ = set(X_[i]).intersection(C_[i])

        S_wo_Z = [s for s in S_[i] if s not in Z_]
        X_wo_Z = [s for s in X_ if s not in Z_]

        D_temp1, D_temp2 = [], []
        for s in set(G.S1).intersection(Z_):
            if set(G.E[s]).intersection(S_[i]).intersection(S_wo_Z):
                D_temp1.append(s)
        for s in set(G.S2).intersection(Z_):
            if set(G.E[s]).intersection(S_[i]).issubset(X_wo_Z + S_wo_Z):
                D_temp2.append(s)
        D = D_temp1 + D_temp2

        G_X = find_sub_graph(G_[i], X_)

        L = attr(1, D, G_X)
        Tr = [s for s in Z_ if s not in L]
        W_[i+1] = attr(2, Tr, G_[i])
        S_[i+1] = [s for s in S_[i] if s not in W_[i+1]]
        G_[i+1] = find_sub_graph(G, S_[i+1])
        i = i + 1
    

if __name__ == "__main__":
    G, B = get_input()
    winning_set = play_buchi_game(G, B)
    