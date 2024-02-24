from math import *



N = int(input(" N = "))
i = 1
S = 0
while i <= N:
    S = 1 / (pow(2 * i , 2)) + S
    i += 1

print( " S = ", S)