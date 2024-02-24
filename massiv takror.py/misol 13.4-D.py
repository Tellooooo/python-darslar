import random



N = int(input("N = "))
A = []
S = 1
for i in range(1 , N + 1):
    Z = random.randint(1 , 10)
    A.append(Z)
print(A)
for j in A:
    S = S * j
    B = len(A)
    P = S ** 1 / B
print(S)
print(P)