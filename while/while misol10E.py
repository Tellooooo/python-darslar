from math import *



N = int(input("N = "))
i = 0
S = 0
P = 0
while i < N:
    S = (3 *( N - i ))
    P = sqrt(S + P)
    i += 1
    S = sqrt(0)
print("P = ", P)