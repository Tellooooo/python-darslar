A = float(input("A = "))
N = int(input("N = "))
S = 1
for i in range(1 , N):
    s = (A - i * N)
    S = S * s
print("S = ", S)