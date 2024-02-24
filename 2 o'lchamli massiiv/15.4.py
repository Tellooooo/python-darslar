import random
M = int(input("M = "))
N = int(input("N = "))
A = []
b = []
for i in range(M):
    for i in range(N):
        z = random.randint(1 , 5)
        A.append(z)
    print(A)
    b.append(A)
    A = []
a = []
for k in range(len(b)):
    S = 0
    for l in range(len(b)):
        # print(b[l][k])
        if S < b[l][k]:
            S = b[l][k]
    a.append(S)
print(a)