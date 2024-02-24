N = int(input("N = "))
S = 0
P = 1
for i in range(2 , N + 1):
    for J in range(i , (i * 2) + 1):
        P = P * J
    S = S + P
    P = 1
print("S = ", S + 2)