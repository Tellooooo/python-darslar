from math import  *



N = int(input("N = "))
s = 0
P = 0
g = 0
for i in range(1 , N + 1):
    for J in range(1 , N + 1):
        S = sin(J)
        G = cos(J)
        s = S + s
        g = G + g
    P = (g / s) + P
    g = 0
    s = 0
print("P = ", P)