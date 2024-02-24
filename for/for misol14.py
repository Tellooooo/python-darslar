N = int(input("N = "))
A = float(input("A = "))
X = float(input("X= "))
P = 1
P = (X + A) ** 2
for i in range(2 , N + 1):
    P = ((P + A) ** 2)
print("P = ", P)