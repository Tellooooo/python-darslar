import random



N = int(input("N = "))
z = 0
S = z / 1
P = 1
A = []
for i in range(1 , N + 1):
    z = random.randint(1 , 10)
    P = P * i
    A.append(z)
    S = (z / P) + S
    
print(A)
print(S)
    