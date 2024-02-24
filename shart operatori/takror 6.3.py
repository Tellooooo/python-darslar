X = int(input("X = "))
Y = int(input("Y = "))
Z = int(input("Z = "))

A = X + Y + Z
B = X * Y * Z

if A > B:
    print("A katta")
elif A < B:
    print("B katta")
else:
    print("Kichik yoki teng")


N = (X + Y + Z) / 2
M = X * Y * Z

if N < M:
    print("N kichik" , N ** 2 + 1)
elif N > M:
    print("M kichik" , M ** 2 + 1)
else:
    print("Kichik yoki teng")