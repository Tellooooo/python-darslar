import random



A = []
S = 1
N = int(input("N = "))
for j in range(1 , N + 1):
    Z = random.randint(-5 , 5)
    A.append(Z)
print(A)
for i in A:
    if i < 0:
        break
    S = S * i
print(S)