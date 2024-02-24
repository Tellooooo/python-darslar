N = int(input("N = "))
V1 , V2 = 0 , 0
V3 = 1.5
if N >= 4:
    for i in range(4 , N + 1):
        V4 = ((i + 1) / ((i ** 2) + 1)) * V3 - V2 * V1
        V1 = V2
        V2 = V3
        V3 = V4
    print("V4 = " , V4)
else:
    print("Kechirasiz")