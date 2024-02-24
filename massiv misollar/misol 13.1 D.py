from math import *
import random


N = int(input("N = "))
A = []
S = 0
for i in range(1 , N + 1):
    z = random.randint(1 , N)
    A.append(z)
    S = S + pow(z , 2)
print("A = " , A)
print("S = " , S)