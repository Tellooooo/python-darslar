from math import *



N = int(input(" N = "))
i = 2
S = sqrt(2)

while i <= N:
    S = sqrt(S + 2)
    i += 1
print("S = ", S)