from math import *



N = int(input("N = "))
S = 1
A = 1
for i in range(0.1 , N + 1 , 0.1):
    
    S = (A + (sin(i))) * S
    
print("S = ", S)