N = int(input("N = "))
P = 1
for i in range(2 , N + 1):
    P = ( i + 1) / (i + 2) * P
print("P = ", P)