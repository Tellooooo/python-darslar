import random


N = int(input("N = "))
A = []
S = 1
for i in range(1 , N + 1):
    z = random.randint(1 , N)
    A.append(z)
    S = S * z
print("A = " , A)
print("S = " , S)