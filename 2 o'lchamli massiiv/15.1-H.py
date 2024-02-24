N = int(input("N = "))
a = []
for i in range(1 , N + 1):
    for j in range(1 , N + 1):
        if j == (N + 1) - i:
            a.append(N)
        else:
            a.append(0)
    print(a)
    a = []