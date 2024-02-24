A = float(input("A = "))
N = int(input("N = "))
S = 1
for i in range(1 , N + 1):
    s = (A + i - 1)
    S = S * S
print("S = ", S)