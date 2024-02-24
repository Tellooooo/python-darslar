from math import *
import random


N = int(input("N = "))
A = []
S = 0
P = 1
for i in range(1 , N + 1):
    z = random.randint(1 , N)
    A.append(z)
    S = (pow(-1, i) * z) / P + S
    P = P * i

print("A = " , A)
print("S = " , S)