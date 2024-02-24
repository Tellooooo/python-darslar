N = int(input("N = "))
S = 0
for i in range( 1 , N + 1):
    if N % i == 0:
        S += 1
if S == 2:
    print("tub son")
else:
    print("tub son emas")