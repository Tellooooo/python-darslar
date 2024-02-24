N = int(input("N = "))
A = []
for i in range(1,N+1):
    A.append(0)
    
for j in range(1,N+1):
    A[j - 1] = 2
    A[j] = 1
    A[j - 2] = 1
    A[j - 3] = 0
    print(A)
    
    
    
    
    
    