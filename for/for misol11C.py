N = int(input("N = "))
S = 0
P = 1
for J in range(1 , N + 1):
    for i in range(1 , J + 1):
        P = P * i
    S = ( 1 / P) + S
    P = 1
print("P = ", P)