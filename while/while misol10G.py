from math import *



N = int(input("N = "))
i = 1
J = 1
P = 0
S = 0
G = 0

while i <= N:
    while J <= i:
        g = cos(J)
        s = sin(J)
        G = g + G
        S = s + S
        J += 1

    P = (G / S) + P
    G = 0
    S = 0
    J = 1
    i += 1

print("P = ", P)