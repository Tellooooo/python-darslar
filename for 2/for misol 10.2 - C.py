from math import *



N = int(input("N = "))
X = float(input("X = "))
S = 0

for i in range(1 , N + 1):
    
    S = S + (X + cos(i * X)) / (2 ** i)
    
print("S = ", S)