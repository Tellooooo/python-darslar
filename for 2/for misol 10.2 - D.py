from math import *


N = int(input("N = "))
X = float(input("X = "))
S = 0
P = 1

for j in range(1 ,N + 1):
        for i in range(1 , j + 1):
                P = P * i
        i = 1
        S = S + (1 + (sin(i * X)) / P)
        P = 1
if N == 0:
    print("SHART XATO") 
else:
    print("S = " , S)


