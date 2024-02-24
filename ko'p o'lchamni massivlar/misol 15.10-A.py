N = int(input("N = "))
A = []
for i in range(N):
    A.append(1)

for j in range(N):

    A[-j - 1] = 0
    # B = B + 1
    print(A)