N = int(input("N = "))
A = []
a = 1
for i in range(N):
    A.append(0)
    
for j in range(N):
    A[-j - 1] = a
    A[-j] = 0
    a += 1
    print(A)