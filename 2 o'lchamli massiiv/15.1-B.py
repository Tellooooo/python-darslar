N = int(input("N = "))
a = []
s = N
for i in range(1 , N + 1):
    for j in range(1 , N + 1):
        if i == (N + 1) - j:
            a.append(s)
        else:
            a.append(0)
    s -= 1
    print(a)
    a = []