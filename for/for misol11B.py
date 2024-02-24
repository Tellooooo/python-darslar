from math import *



N = int(input("N = "))
S = 0
P = 0
for i in range(1 , N + 1):
    S = 1 / pow(i , 3)
    P += S
print("P = ", P)