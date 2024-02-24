from math import *



N = int(input(" N = "))
i = 1
J = 1
P = 0
S = 0

while i <= N:
    while J <= i:
        S = sin(N)
        s = S + S
        J += 1
    
    P = 1 / s
    s = 0
    J = 1
    i += 1

print("P = ", P)