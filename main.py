from cmath import log
from input import get_input
from math import log

def source(W, G):
    s = {}
    for node in G.S:
        for succ_node in G.E[node]:
            if succ_node in W:
                s.add(node)
                break


def attr(B_, G_): pass


def avoid_set_classical(G_, B_, S_, i):
    R = attr(1, B_, G_[i])
    Tr = [s for s in S_[i] if s not in R]
    W = attr(2, Tr, G_[i])
    return W



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
        if (len(source(W_[i], G))) >= G.m/log(G.n):
            W_[i+1] = avoid_set_classical(G_[i], set(B).intersection(S_[i]))
        else: pass

        S_[i+1] = [s for s in S_[i] if s not in W_[i+1]]
        # G_[i+1] = G
        i = i + 1

    

if __name__ == "__main__":
    G, B = get_input()
    winning_set = play_buchi_game(G, B)
    