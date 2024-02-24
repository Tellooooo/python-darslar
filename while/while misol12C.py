from math import *



A = float(input("A = "))
N = int(input("N = "))
i = 1
S = 0

j = 1
P = 1
while i <= N:
    while j <= i:
        M = (A - 1 + j)
        P = P * M
        j += 1
    S = S + ( 1 / P)
    i += 1
    j = 1
    P = 1
print("S = ", S)