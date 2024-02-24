import random



N = int(input("N = "))
A = []
for i in range(1 , N + 1):
    Z = random.randint(1 , 10)
    A.append(Z)
print(A)
k = A[0]
for j in A:
    if k < j:
        k = j
print(k)