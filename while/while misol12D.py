A = float(input("A = "))
N = int(input("N = "))
i = 0
S = 1
while i < N:
    Z = (A - i * N)
    S = S * Z
    i += 1
print("S = ", S)