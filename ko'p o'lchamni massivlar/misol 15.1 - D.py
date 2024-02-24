N = int(input("N = "))
A = []

for i in range(N):
    A.append(0)
  
for j in range(N):
    # A[j] = N - 1
    # A[j - 1] = 0 
    A[j] = (j + 1) * (j + 2) 
    A[j - 1] = 0
    print(A)