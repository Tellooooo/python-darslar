from math import *
import random

N = int(input("N = "))
A = []
S = 1
for i in range(1 , N + 1):
    z = random.randint(-5 , N)
    A.append(z)
    S = S * (fabs(z))
print("A = " , A)
print("S = " , S)