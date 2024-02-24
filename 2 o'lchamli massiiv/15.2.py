import random
M = int(input("M = "))
N = int(input("N = "))
A = []
a = []
for i in range(M):
    S = 0
    for i in range(N):
        z = random.randint(1 , 5)
        S += z
        A.append(z)
    A.append(S)
    print(A)
    A = []