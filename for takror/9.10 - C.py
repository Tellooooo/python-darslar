N = int(input("N = "))
S = 0
for i in range(1 , N + 1):
    S = S + (1 + (1 / (i ** 2)))
print("S = " , S)