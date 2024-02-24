import random
from math import *



A = []
S = 1
N = int(input("N = "))
for i in range(1 , N + 1):
    Z = random.randint(-10 , 10)
    A.append(fabs(Z))
print(A)
for i in A:
    S = S * i
print(S)