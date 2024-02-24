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
S = b[0][0]
p = 5
for k in range(0 , len(b)):
    for l in range(0 , len(b)):
        if S > b[k][l]:
            S = b[k][l]
