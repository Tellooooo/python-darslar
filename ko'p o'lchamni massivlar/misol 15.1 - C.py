N = int(input("N = "))
A = []
B = N
for i in range(N):
    A.append(0)

for j in range(N):

    A[j] = B
    A[j - 1] = 0 
    B = B - 1
    # B = B + 1
    print(A)