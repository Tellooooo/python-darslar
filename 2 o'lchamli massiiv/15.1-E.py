N = int(input("N = "))
a = []
for i in range(1 , N + 1):
    for j in range(1 , N + 1):
        if j == i:
            a.append(2)
        elif j == (i + 1) or j == (i - 1):
            a.append(1)
        else:
            a.append(0)
    print(a)
    a = []