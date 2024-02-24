N = int(input("N = "))
S = 0
for k in range(1 , N + 1):
    S = S + 1 / (2 * k + 1) ** 2
    
print("S = " , S)