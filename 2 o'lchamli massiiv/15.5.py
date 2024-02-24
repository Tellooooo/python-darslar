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
index = 0
joyi = 0
for k in range(0 , len(b)):
    for l in range(0 , len(b)):
        if S > b[k][l]:
            S = b[k][l]
        index = k
    joyi = k
# a.append(S)
print("indeksi=" , index , "joyi=" , joyi , "Soni=" , S)