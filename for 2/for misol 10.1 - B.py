N = int(input("N = "))
S = 0
for k in range(1 , N + 1):
    S = S + 1 / k ** 5
    
print("S = " , S)