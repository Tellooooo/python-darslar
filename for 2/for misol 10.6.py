N = int(input("N = "))
P = 1
a0 , a1 = 1 , 1
if N >= 2:
    for i in range(2 , N + 1):
        A = a0 + (a1 / (2 ** (i - 1)))
        a0 = a1
        a1 = A
        P = P * A
    print("P = " , P)
else:
    print("Kechirasiz")