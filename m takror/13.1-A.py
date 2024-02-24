import random



N = int(input("N = "))
A = []
S = 0
for i in range(1 , N + 1):
    z = random.randint(1 , 10)
    A.append(z)
    S = S + z
    
print(A)
print(S)