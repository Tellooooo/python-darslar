N = int(input("N = "))
A = []
B = 1
C = N
for i in range(N-1):
    A.append(0)

for j in range(N - 1):
    A[-j] = 0
    A[j] = B
    A[j - 1] = 0
    A[-j - 1]=C
    B = B + 1
    C = C - 1
    print(A)