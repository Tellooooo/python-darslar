from math import *



N = int(input(' N = '))
S = 0
P = 1
for i in range(1 , N + 1):
    S = (1 + (1 / pow(i , 2)))
    P = P * S

print("P = ", P)