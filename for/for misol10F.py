from math import *



N = int(input("N = "))
s = 0
P = 0
for i in range(1 , N + 1):
    for J in range(1 , i + 1):
        S = sin(N)
        s = S + S
    P = 1 / S
    s = 0
print("P = ", P)