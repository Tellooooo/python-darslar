from math import *



N = int(input("P = "))
S = 0
for i in range(1 , N + 1):
    S = pow(1 / (2 * i) , 2) + S
print("S = ", S)