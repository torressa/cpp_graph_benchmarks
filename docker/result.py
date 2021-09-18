#!/usr/bin/python

from numpy import mean as mean
from numpy import std as std


def makeTable(Fs, Es):
    As = []
    for E in Es:
        Rs = []
        for F in Fs:
            Ls = open("logs/" + E + ".dat-" + F + ".log")

            Ds = []
            for L in Ls:
                A = L.split()
                if A[0] == 'Time':
                    Ds.append(float(A[1]))

            Rs.append([mean(Ds), std(Ds)])
        As.append(Rs)
    return As


def printTable(Fs, As):
    for F in Fs:
        print(
            "|",
            F,
        )
    print()
    for A in As:
        for R in A:
            print(str(round(R[0], 3)) + "(%.3f)" % round(R[1], 2), )
        print()


# Start the script here
Fs = ["dijkstra", "dijkstra_bgl", "dijkstra_lemon", "dijkstra_or-tools"]
Es = ["rand_10000_100000", "rand_10000_1000000", "rand_10000_10000000"]
Gs = [  # "dijkstra",
    "Dijkstra_bgl", "Dijkstra_lemon"
]
Hs = [
    "USA-d.W", "USA-d.E", "USA-d.LKS", "USA-d.CAL", "USA-d.NE", "USA-d.NW",
    "USA-d.FLA", "USA-d.COL", "USA-d.BAY", "USA-d.NY"
]
# Is = ["dijkstra_binary", "dijkstra_ternary", "dijkstra_skew", "dijkstra_lemon"]

for A, B in [  # [Fs, Es],
    [Gs, Hs],
        #[Is, Hs]
]:
    Ts = makeTable(A, B)
    printTable(A, Ts)
    print()
