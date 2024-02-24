#N = int(input("N = "))
N = 5
A = []
a = []
for i in range(N):
    a = []
    for j in range(N):
        a.append(0)
    A.append(a)
print(A)

for j in range(0 , N):
    
    for k in range(0 , N):
        x = 1
        if k == j:
            a[j] = N
        elif k == j - x:
            a[j] = N - 1
        x += 1

    print(a)