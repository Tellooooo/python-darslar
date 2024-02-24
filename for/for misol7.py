N = int(input("N = "))
S = 0
for i in range(1 , N):
    for J in range(1 , i + 1):
        if i % J == 0:
            S += 1
    if S == 2:
        print( J)
    S = 0