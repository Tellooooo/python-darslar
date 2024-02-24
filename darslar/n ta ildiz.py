from math import *


N = int(input("N = "))
S = sqrt(2)

for i in range(1 , N + 1):
    S = (sqrt (S + 2))
print(S)