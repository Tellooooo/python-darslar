N = int(input("N = "))
A = []
a = N
for i in range(N):
    A.append(0)
    
for j in range(N):
    A[j] = a
    A[j - 1] = 0
    a -= 1
    print(A)