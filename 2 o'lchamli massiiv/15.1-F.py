N = int(input("N = "))
a = []
s = 1
for i in range(1 , N + 1):
    for j in range(1 , N + 1):
        if j <= (N + 1) - i:
            a.append(s)
        else:
            a.append()
    s += 1
    print(a)
    a = []