import random
M = int(input("M = "))
N = int(input("N = "))
A = []
for i in range(M):
    S = 0
    for i in range(N):
        z = random.randint(1 , 5)
        A.append(z)
        if z > S:
            S = z
    A.append(S)
    print(A)
    A = []