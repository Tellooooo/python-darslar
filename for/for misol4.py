N = int(input("N = "))
S = 0 
for i in range(1 , N + 1):
    for J in range(1 , i):
        if i % J == 0:
            S += J
    if S == i:
        print("S = ", S)
    S = 0