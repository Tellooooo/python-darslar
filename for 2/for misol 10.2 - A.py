N = int(input("N = "))
X = float(input("X = "))
S = 0
P = 1

for j in range(1 ,N + 1):
        for i in range(1 , j + 1):
                P = P * i
        i = 1
        S = S + (X ** i) / P 
        P = 1
        
print("S = " , S)
    