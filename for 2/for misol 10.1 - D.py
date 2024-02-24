N = int(input("N = "))
S = 0

for k in range(N + 1):
    S = S + ((-1) ** k) / (2 * k + 1) ** k
    
print("S = " , S)