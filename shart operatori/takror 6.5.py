X = float(input("X = "))
Y = float(input("Y = "))
Z = float(input("Z = "))

if X >= Y >= Z:
    print(X ** 2 , Y ** 2 , Z ** 2)
    if X <= -1:
        print(X * (-1))
    else:
        print(X)
    if Y <= -1:
        print(Y * (-1))
    else:
        print(Y)
    if Z <= -1:
        print(Z * (-1))
    else:
        print(Z)
