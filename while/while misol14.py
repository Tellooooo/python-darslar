N = int(input("N = "))
A = float(input("A = "))
X = float(input("X = "))
U = 2
Y = 1
Y = (X + A) ** 2

while U <= N:
    Y = ((Y + A) ** 2)
    U += 1

print("Y = ", Y)