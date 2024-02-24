import random



A = []
B = []
S = 0
P = 0
for i in range(1 , 21):
    z = random.randint(1 , 100)
    A.append(z)
print(A)
C = max(A)
for i in A:
    if i >= 20:
        B.append(i)
        S = S + i
        P = S / len(B)
print(C)
print(P)