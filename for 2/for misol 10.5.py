q = float(input("q = "))
r = float(input("r = "))
c = float(input("c = "))
d = float(input("d = "))
b = float(input("b = "))
N = int(input("N = "))
X0 = c
X1 = d
if N >= 2:
    for i in range(2 , N + 1):
        X = q * X1 + r * X0 + b
        X0 = X1
        X1 = X
    print("X = " , X)
else:
    print("Kechirasiz")
