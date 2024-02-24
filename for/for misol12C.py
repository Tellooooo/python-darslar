A = float(input("A = "))
N = int(input("N = "))
S = 0
s = 1
for i in range(1 , N + 1):
    for J in range(1 , i + 1):
        M = (A - 1 + J)
        s = s * M
    S = S + (1 / s)
    s = 1
print("S = ", S)