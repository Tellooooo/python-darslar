import random



N = int(input("N = "))
A = []
S = 1
for i in range(1 , N + 1):
    Z = random.randint(1 , 10)
    A.append(Z)
print(A)
k = A[0]
for j in A:
    S = S + 1
    if S % 2 != 0:
        if k > j:
            k = j
print(k)