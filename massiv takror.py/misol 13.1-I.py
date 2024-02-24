from math import *
import random


N = int(input("N = "))
z = 0
A = []
S = z / 1
P = 1
for i in range(1 , N + 1):
    z = random.randint(1 , N)
    P = P * i
    A.append(z)
    S = (z / P) + S
print("A = " , A)
print("S = " , S)