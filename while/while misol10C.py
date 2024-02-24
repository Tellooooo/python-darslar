from math import *



N = int(input(' N = '))
i = 1
S = 0
P = 1
while i <= N:
    S = (1 + (1 / pow(i , 2)))
    P = P * S
    i += 1

print(" P = ", P)