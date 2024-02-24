N = int(input("N = "))
a = []
S = N
for i in range(1 , N + 1):
    for j in range(1 , N + 1):
        if i == j:
            a.append(S)
        else:
            a.append(0)
    S -= 1
    print(a)
    a = []